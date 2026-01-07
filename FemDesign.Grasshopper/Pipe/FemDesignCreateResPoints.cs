// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Grasshopper.Kernel;

using FemDesign.AuxiliaryResults;
using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Create result points using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignCreateResPoints : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private List<ResultPoint> _resultPoints;
        private bool _runNode;

        // Output data
        private List<string> _log;
        private bool _success;

        public FemDesignCreateResPoints() : base("FEM-Design.CreateResPoints", "CreateResPoints", "Create result points using the shared FEM-Design connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("ResultPoints", "ResultPoints", "ResultPoints.", GH_ParamAccess.list);
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _resultPoints = new List<ResultPoint>();
            DA.GetDataList("ResultPoints", _resultPoints);

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
            if (!_resultPoints.Any())
                throw new Exception("ResultPoints is empty.");

            FemDesignConnectionHub.InvokeAsync(_handle.Id, connection =>
            {
                void onOutput(string s) { _log.Add(s); }
                connection.OnOutput += onOutput;
                try
                {
                    cancellationToken.ThrowIfCancellationRequested();
                    var resPoints = _resultPoints.Select(x => (CmdResultPoint)x).ToList();
                    connection.CreateResultPoint(resPoints);
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
            DA.SetDataList("Log", _log);
            DA.SetData("Success", _success);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetDataList("Log", _log ?? new List<string>());
            DA.SetData("Success", false);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{54EB08E8-69E7-41CB-9152-404245D5B7D6}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}
