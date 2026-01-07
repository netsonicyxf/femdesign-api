// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Threading;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Open a model using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignOpen : FemDesignHybridComponent
    {
        // Input data (collected on UI thread)
        private FemDesignHubHandle _handle;
        private dynamic _modelIn;
        private bool _runNode;

        // Output data (set by ExecuteWork)
        private Model _modelOut;
        private List<string> _log;
        private bool _success;

        public FemDesignOpen() : base("FEM-Design.OpenModel", "OpenModel", "Open model in FEM-Design using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Model", "Model", "Model to open or file path.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Model", "Model", "Opened model (round-tripped).", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _modelIn = null;
            DA.GetData("Model", ref _modelIn);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _modelOut = null;
            _log = new List<string>();
            _success = false;
        }

        protected override bool ShouldExecute()
        {
            if (!_runNode)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
                return false;
            }
            if (_handle == null)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Connection input is null.");
                return false;
            }
            return true;
        }

        protected override void ExecuteWork(CancellationToken cancellationToken)
        {
            // Check for cancellation before starting
            cancellationToken.ThrowIfCancellationRequested();

            FemDesignConnectionHub.InvokeAsync(_handle.Id, connection =>
            {
                void onOutput(string s) { _log.Add(s); }
                connection.OnOutput += onOutput;
                try
                {
                    // Check for cancellation
                    cancellationToken.ThrowIfCancellationRequested();

                    if (_modelIn is string path)
                    {
                        connection.Open(path);
                    }
                    else if (_modelIn is Model m)
                    {
                        connection.Open(m);
                    }
                    else if (_modelIn != null && _modelIn.Value is string)
                    {
                        string vpath = _modelIn.Value as string;
                        connection.Open(vpath);
                    }
                    else if (_modelIn != null && _modelIn.Value is Model)
                    {
                        Model vm = _modelIn.Value as Model;
                        connection.Open(vm);
                    }
                    else
                    {
                        throw new Exception("Unsupported 'Model' input. Provide file path or FemDesign.Model.");
                    }

                    // Check for cancellation before getting model
                    cancellationToken.ThrowIfCancellationRequested();

                    _modelOut = connection.GetModel();
                }
                finally
                {
                    connection.OnOutput -= onOutput;
                }
            }).GetAwaiter().GetResult();

            _success = true;
        }

        protected override void SetOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", _handle);
            DA.SetData("Model", _modelOut);
            DA.SetData("Success", _success);
            DA.SetDataList("Log", _log);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetData("Model", null);
            DA.SetData("Success", false);
            DA.SetDataList("Log", _log ?? new List<string>());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_open;
        public override Guid ComponentGuid => new Guid("{667EFCEA-8B2D-4516-ADC5-DBC08585CBA1}");
        public override GH_Exposure Exposure => GH_Exposure.primary;
    }
}
