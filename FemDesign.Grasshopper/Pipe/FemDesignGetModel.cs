// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Threading;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Get the current open model using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignGetModel : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private bool _runNode;

        // Output data
        private Model _model;
        private List<string> _log;
        private bool _success;

        public FemDesignGetModel() : base("FEM-Design.GetModel", "GetModel", "Get the current open model in FEM-Design using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Model", "Model", "Current FEM-Design model.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _model = null;
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

            FemDesignConnectionHub.InvokeAsync(_handle.Id, conn =>
            {
                void onOutput(string s) { _log.Add(s); }
                conn.OnOutput += onOutput;
                try
                {
                    cancellationToken.ThrowIfCancellationRequested();
                    _model = conn.GetModel();
                }
                finally
                {
                    conn.OnOutput -= onOutput;
                }
            }).GetAwaiter().GetResult();

            _success = true;
        }

        protected override void SetOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", _handle);
            DA.SetData("Model", _model);
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

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{65B2948C-4F04-4038-AC14-694091005DC5}");
        public override GH_Exposure Exposure => GH_Exposure.primary;
    }
}
