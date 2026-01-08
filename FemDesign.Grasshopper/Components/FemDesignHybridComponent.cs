// https://strusoft.com/
using Grasshopper.Kernel;
using System;
using System.Threading;
using System.Threading.Tasks;
using Timer = System.Timers.Timer;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Base component that can run either synchronously or asynchronously
    /// based on global FemDesignSettings.AsyncModeEnabled setting.
    /// 
    /// In sync mode: executes immediately, blocking the UI.
    /// In async mode: executes in a background task, allowing UI to remain responsive.
    /// </summary>
    public abstract class FemDesignHybridComponent : FEM_Design_API_Component
    {
        private CancellationTokenSource _cts;
        private bool _isRunning;
        private bool _hasResult;
        private Exception _asyncException;

        // Spinner animation for async processing
        private Timer _spinnerTimer;
        private int _spinnerFrame;
        private static readonly string[] SpinnerFrames = new[]
        {
            @"\Processing\",
            @"|Processing|",
            @"/Processing/",
            @"-Processing-"
        };

        protected FemDesignHybridComponent(string name, string nickname, string description, string category, string subCategory)
            : base(name, nickname, description, category, subCategory)
        {
            // Initialize spinner timer (updates every 250ms)
            _spinnerTimer = new Timer(250) { AutoReset = true };
            _spinnerTimer.Elapsed += OnSpinnerTick;

            // Set initial message based on current mode
            UpdateAsyncMessage();
        }

        public override void AddedToDocument(GH_Document document)
        {
            base.AddedToDocument(document);

            // Subscribe to async mode changes
            FemDesignSettings.AsyncModeChanged += OnAsyncModeChanged;

            // Update message when added to document
            UpdateAsyncMessage();
        }

        private void OnAsyncModeChanged()
        {
            // Update message when async mode changes (only if not currently running)
            if (!_isRunning)
            {
                UpdateAsyncMessage();

                // Refresh display on UI thread
                Rhino.RhinoApp.InvokeOnUiThread((Action)(() =>
                {
                    OnDisplayExpired(true);
                }));
            }
        }

        private void UpdateAsyncMessage()
        {
            // Show "Async" when async mode is enabled, nothing when sync mode
            Message = FemDesignSettings.AsyncModeEnabled ? "Async" : null;
        }

        private void OnSpinnerTick(object sender, System.Timers.ElapsedEventArgs e)
        {
            if (!_isRunning) return;

            _spinnerFrame = (_spinnerFrame + 1) % SpinnerFrames.Length;
            Message = SpinnerFrames[_spinnerFrame];

            // Update display on UI thread
            Rhino.RhinoApp.InvokeOnUiThread((Action)(() =>
            {
                OnDisplayExpired(true);
            }));
        }

        private void StartSpinner()
        {
            _spinnerFrame = 0;
            Message = SpinnerFrames[0];
            _spinnerTimer?.Start();
        }

        private void StopSpinner()
        {
            _spinnerTimer?.Stop();
        }

        /// <summary>
        /// Override this to collect input data from the DataAccess object.
        /// Store the data in instance fields for use in ExecuteWork.
        /// This is called on the UI thread before async execution starts.
        /// </summary>
        protected abstract void CollectInputData(IGH_DataAccess DA);

        /// <summary>
        /// Override this to implement the actual work logic.
        /// This runs on a background thread in async mode.
        /// Use cancellationToken to check for cancellation in long-running operations.
        /// Store results in instance fields for use in SetOutputData.
        /// </summary>
        protected abstract void ExecuteWork(CancellationToken cancellationToken);

        /// <summary>
        /// Override this to set output data to the DataAccess object.
        /// This is called on the UI thread after ExecuteWork completes.
        /// </summary>
        protected abstract void SetOutputData(IGH_DataAccess DA);

        /// <summary>
        /// Override this to set default/empty output data when RunNode is false or an error occurs.
        /// </summary>
        protected virtual void SetDefaultOutputData(IGH_DataAccess DA) { }

        /// <summary>
        /// Override this to check if the component should execute.
        /// Return false to skip execution (e.g., when RunNode is false).
        /// </summary>
        protected virtual bool ShouldExecute() => true;

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            if (FemDesignSettings.AsyncModeEnabled)
            {
                SolveAsync(DA);
            }
            else
            {
                // Sync mode: collect input data and execute
                CollectInputData(DA);

                // Check if we should execute
                if (!ShouldExecute())
                {
                    SetDefaultOutputData(DA);
                    return;
                }

                SolveSync(DA);
            }
        }

        private void SolveSync(IGH_DataAccess DA)
        {
            // In sync mode, don't show any message annotation
            Message = null;

            try
            {
                ExecuteWork(CancellationToken.None);
                SetOutputData(DA);
            }
            catch (Exception ex)
            {
                AddRuntimeMessage(GH_RuntimeMessageLevel.Error, ex.Message);
                SetDefaultOutputData(DA);
            }
        }

        private void SolveAsync(IGH_DataAccess DA)
        {
            // Second pass: we have results from the async operation
            // DON'T collect input data here - we need to preserve the output data from ExecuteWork
            if (_hasResult)
            {
                if (_asyncException != null)
                {
                    AddRuntimeMessage(GH_RuntimeMessageLevel.Error, _asyncException.Message);
                    SetDefaultOutputData(DA);
                    Message = "Error";
                }
                else
                {
                    SetOutputData(DA);
                    Message = "Async";
                }

                // Reset state for next run
                _hasResult = false;
                _asyncException = null;
                return;
            }

            // Already running, wait for completion
            if (_isRunning)
            {
                return;
            }

            // First pass: collect input data and start async work
            CollectInputData(DA);

            // Check if we should execute
            if (!ShouldExecute())
            {
                SetDefaultOutputData(DA);
                Message = "Async";
                return;
            }

            // Cancel any previous operation
            _cts?.Cancel();
            _cts?.Dispose();
            _cts = new CancellationTokenSource();
            var token = _cts.Token;

            _isRunning = true;
            _asyncException = null;
            StartSpinner();

            // Start background task
            Task.Run(() =>
            {
                try
                {
                    ExecuteWork(token);
                }
                catch (OperationCanceledException)
                {
                    // Cancelled - don't expire solution
                    _isRunning = false;
                    StopSpinner();
                    return;
                }
                catch (Exception ex)
                {
                    _asyncException = ex;
                }
                finally
                {
                    _isRunning = false;
                    _hasResult = true;
                    StopSpinner();
                }

                // Schedule solution update on UI thread
                Rhino.RhinoApp.InvokeOnUiThread((Action)(() =>
                {
                    ExpireSolution(true);
                }));
            }, token);
        }

        protected override void BeforeSolveInstance()
        {
            base.BeforeSolveInstance();

            // If async mode changed or new solve started, cancel any pending work
            if (_isRunning && !_hasResult)
            {
                _cts?.Cancel();
            }
        }

        public override void RemovedFromDocument(GH_Document document)
        {
            // Unsubscribe from async mode changes
            FemDesignSettings.AsyncModeChanged -= OnAsyncModeChanged;

            // Stop spinner and cancel any pending async work
            StopSpinner();
            _spinnerTimer?.Dispose();
            _spinnerTimer = null;

            _cts?.Cancel();
            _cts?.Dispose();
            _cts = null;

            base.RemovedFromDocument(document);
        }

        public override void DocumentContextChanged(GH_Document document, GH_DocumentContext context)
        {
            base.DocumentContextChanged(document, context);

            // Cancel async work when document is closing
            if (context == GH_DocumentContext.Close || context == GH_DocumentContext.Unloaded)
            {
                StopSpinner();
                _spinnerTimer?.Dispose();
                _spinnerTimer = null;

                _cts?.Cancel();
                _cts?.Dispose();
                _cts = null;
            }
        }
    }
}

