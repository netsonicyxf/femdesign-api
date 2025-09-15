// https://strusoft.com/
using System;
using System.Collections.Concurrent;
using System.Threading;
using System.Threading.Tasks;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Process-wide shared FemDesignConnection with serialized access on a dedicated worker thread.
    /// Ensures stable threading across iterations to avoid UI deadlocks.
    /// </summary>
    public static class FemDesignConnectionHub
    {
        private static FemDesign.FemDesignConnection _connection;
        private static volatile bool _configured;
        private static string _fdDir;
        private static bool _minimized;
        private static string _outputDir;
        private static bool _deleteOutput;

        private static Thread _workerThread;
        private static readonly BlockingCollection<Action> _queue = new BlockingCollection<Action>();
        private static readonly object _startLock = new object();

        public static void Configure(string fdDir, bool minimized, string outputDir = null, bool deleteOutput = false)
        {
            _fdDir = fdDir;
            _minimized = minimized;
            _outputDir = outputDir;
            _deleteOutput = deleteOutput;
            _configured = true;
            EnsureStarted();
        }

        private static void EnsureStarted()
        {
            if (_workerThread != null) return;
            lock (_startLock)
            {
                if (_workerThread != null) return;
                if (!_configured) throw new InvalidOperationException("FemDesignConnectionHub not configured.");

                _workerThread = new Thread(() =>
                {
                    _connection = new FemDesign.FemDesignConnection(_fdDir, _minimized, outputDir: _outputDir, tempOutputDir: _deleteOutput);
                    foreach (var action in _queue.GetConsumingEnumerable())
                    {
                        try { action(); }
                        catch { /* Swallow here; exceptions are delivered via TaskCompletionSource */ }
                    }
                });
                _workerThread.IsBackground = true;
                _workerThread.Name = "FemDesignConnectionHub-Worker";
                _workerThread.Start();
            }
        }

        public static Task<T> InvokeAsync<T>(Func<FemDesign.FemDesignConnection, T> func)
        {
            if (_workerThread == null) EnsureStarted();
            var tcs = new TaskCompletionSource<T>();
            _queue.Add(() =>
            {
                try { tcs.SetResult(func(_connection)); }
                catch (Exception ex) { tcs.SetException(ex); }
            });
            return tcs.Task;
        }

        public static Task InvokeAsync(Action<FemDesign.FemDesignConnection> action)
        {
            if (_workerThread == null) EnsureStarted();
            var tcs = new TaskCompletionSource<bool>();
            _queue.Add(() =>
            {
                try { action(_connection); tcs.SetResult(true); }
                catch (Exception ex) { tcs.SetException(ex); }
            });
            return tcs.Task;
        }

        public static Task DisposeAsync()
        {
            var tcs = new TaskCompletionSource<bool>();
            if (_workerThread == null)
            {
                tcs.SetResult(true);
                return tcs.Task;
            }

            _queue.Add(() =>
            {
                try { _connection?.Dispose(); _connection = null; }
                catch { /* ignore */ }
                finally { tcs.SetResult(true); }
            });

            // complete queue after disposing to end thread
            _queue.CompleteAdding();
            _workerThread = null;
            return tcs.Task;
        }
    }
}


