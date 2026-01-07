// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Threading;
using Grasshopper.Kernel;
using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Run analysis using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignRunAnalysis : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private Analysis _analysis;
        private bool _runNode;

        // Output data
        private List<string> _log;
        private bool _success;

        public FemDesignRunAnalysis() : base("FEM-Design.RunAnalysis", "RunAnalysis", "Run analysis on current/open model using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Analysis", "Analysis", "Analysis settings.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if analysis succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _analysis = null;
            DA.GetData("Analysis", ref _analysis);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
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
            cancellationToken.ThrowIfCancellationRequested();

            // Check inputs
            if (_analysis == null)
                throw new Exception("'Analysis' input is null.");

            FemDesignConnectionHub.InvokeAsync(_handle.Id, connection =>
            {
                void onOutput(string s) { _log.Add(s); }
                connection.OnOutput += onOutput;
                try
                {
                    cancellationToken.ThrowIfCancellationRequested();
                    connection.RunAnalysis(_analysis);
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
            DA.SetData("Success", _success);
            DA.SetDataList("Log", _log);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetData("Success", false);
            DA.SetDataList("Log", _log ?? new List<string>());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_RunAnalysis;
        public override Guid ComponentGuid => new Guid("{166B94CD-DCE9-467A-B693-01405D22D20E}");
        public override GH_Exposure Exposure => GH_Exposure.secondary;
    }
}
