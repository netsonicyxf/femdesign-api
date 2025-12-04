// https://strusoft.com/
using System;
using System.Collections.Concurrent;
using System.Threading;
using System.Threading.Tasks;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Manages one or more FemDesignConnection instances with serialized access per instance
    /// on dedicated worker threads. Ensures stable threading across iterations to avoid UI deadlocks.
    /// </summary>
    public static class FemDesignConnectionHub
    {
        private class Instance
        {
            public FemDesign.FemDesignConnection Connection;
            public Thread WorkerThread;
            public BlockingCollection<Action> Queue = new BlockingCollection<Action>();
        }

        private static readonly System.Collections.Concurrent.ConcurrentDictionary<Guid, Instance> _instances = new System.Collections.Concurrent.ConcurrentDictionary<Guid, Instance>();

        /// <summary>
        /// Create a new FemDesign connection instance and return its handle.
        /// </summary>
        public static Guid Create(string fdDir, bool minimized, string outputDir = null, bool deleteOutput = false)
        {
            var id = Guid.NewGuid();
            var inst = new Instance();
            inst.WorkerThread = new Thread(() =>
            {
                inst.Connection = new FemDesign.FemDesignConnection(fdDir, minimized, outputDir: outputDir, tempOutputDir: deleteOutput);
                foreach (var action in inst.Queue.GetConsumingEnumerable())
                {
                    try { action(); }
                    catch { /* Swallow here; exceptions are delivered via TaskCompletionSource */ }
                }
            });

            inst.WorkerThread.IsBackground = true;
            inst.WorkerThread.Name = $"FemDesignConnectionHub-Worker-{id}";

            if (!_instances.TryAdd(id, inst)) 
                throw new InvalidOperationException("Failed to create FemDesign connection instance.");

            inst.WorkerThread.Start();
            return id;
        }

        private static Instance Require(Guid id)
        {
            if (!_instances.TryGetValue(id, out var inst)) 
                throw new InvalidOperationException("Invalid or disposed FemDesign connection handle.");

            return inst;
        }

        public static Task<T> InvokeAsync<T>(Guid id, Func<FemDesign.FemDesignConnection, T> func)
        {
            var inst = Require(id);
            var tcs = new TaskCompletionSource<T>();

            inst.Queue.Add(() =>
            {
                try { tcs.SetResult(func(inst.Connection)); }
                catch (Exception ex) { tcs.SetException(ex); }
            });

            return tcs.Task;
        }

        public static Task InvokeAsync(Guid id, Action<FemDesign.FemDesignConnection> action)
        {
            var inst = Require(id);
            var tcs = new TaskCompletionSource<bool>();
            
            inst.Queue.Add(() =>
            {
                try 
                { 
                    action(inst.Connection); 
                    tcs.SetResult(true); 
                }
                catch (Exception ex) { tcs.SetException(ex); }
            });

            return tcs.Task;
        }

        public static Task DisposeAsync(Guid id) => DisposeAsync(id, false);

        public static Task DisposeAsync(Guid id, bool detach)
        {
            var tcs = new TaskCompletionSource<bool>();
            if (!_instances.TryGetValue(id, out var inst)) 
            { 
                tcs.SetResult(true); 

                return tcs.Task; 
            }

            inst.Queue.Add(() =>
            {
                try 
                { 
                    if(detach)
                    {
                        inst.Connection?.KeepOpen();
                    }
                    inst.Connection?.Dispose(); 
                    inst.Connection = null; 
                }
                catch { /* ignore */ }
                finally { tcs.SetResult(true); }
            });

            inst.Queue.CompleteAdding();
            _instances.TryRemove(id, out _);

            return tcs.Task;
        }
    }
}


