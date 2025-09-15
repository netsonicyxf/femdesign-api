// https://strusoft.com/
using System;
using System.Threading;
using System.Threading.Tasks;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Process-wide shared FemDesignConnection with serialized access.
    /// Ensures the connection is created off the UI thread to avoid deadlocks.
    /// </summary>
    public static class FemDesignConnectionHub
    {
        private static readonly SemaphoreSlim _gate = new SemaphoreSlim(1, 1);
        private static FemDesign.FemDesignConnection _connection;
        private static volatile bool _configured;
        private static string _fdDir;
        private static bool _minimized;
        private static string _outputDir;
        private static bool _deleteOutput;

        public static void Configure(string fdDir, bool minimized, string outputDir = null, bool deleteOutput = false)
        {
            _fdDir = fdDir;
            _minimized = minimized;
            _outputDir = outputDir;
            _deleteOutput = deleteOutput;
            _configured = true;
        }

        private static async Task EnsureCreatedAsync()
        {
            if (_connection != null) return;
            if (!_configured) throw new InvalidOperationException("FemDesignConnectionHub not configured.");

            _connection = await Task.Run(() =>
                new FemDesign.FemDesignConnection(_fdDir, _minimized, outputDir: _outputDir, tempOutputDir: _deleteOutput)
            ).ConfigureAwait(false);
        }

        public static async Task<T> InvokeAsync<T>(Func<FemDesign.FemDesignConnection, T> func)
        {
            await _gate.WaitAsync().ConfigureAwait(false);
            try
            {
                await EnsureCreatedAsync().ConfigureAwait(false);
                return func(_connection);
            }
            finally
            {
                _gate.Release();
            }
        }

        public static async Task InvokeAsync(Action<FemDesign.FemDesignConnection> action)
        {
            await _gate.WaitAsync().ConfigureAwait(false);
            try
            {
                await EnsureCreatedAsync().ConfigureAwait(false);
                action(_connection);
            }
            finally
            {
                _gate.Release();
            }
        }

        public static async Task DisposeAsync()
        {
            await _gate.WaitAsync().ConfigureAwait(false);
            try
            {
                _connection?.Dispose();
                _connection = null;
            }
            finally
            {
                _gate.Release();
            }
        }
    }
}


