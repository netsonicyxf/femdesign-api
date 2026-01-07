// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;

using FemDesign.AuxiliaryResults;
using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Create result points using the shared hub connection (standard GH_Component, UI-blocking).
    /// Mirrors PipeResultPoints behavior without the async workaround.
    /// </summary>
    public class FemDesignCreateResPoints : FEM_Design_API_Component
    {
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

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

            var resultPoints = new List<ResultPoint>();
            DA.GetDataList("ResultPoints", resultPoints);

            bool runNode = true;
            DA.GetData("RunNode", ref runNode);

            var log = new List<string>();
            bool success = false;

            if (!runNode)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
                DA.SetData("Connection", null);
                DA.SetDataList("Log", log);
                DA.SetData("Success", false);
                return;
            }

            // check inputs
            if (!resultPoints.Any())
                    throw new Exception("ResultPoints is empty.");

            try
            {
                if (handle == null)
                    throw new Exception("Connection handle is null.");

                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
                {
                    void onOutput(string s) { log.Add(s); }
                    connection.OnOutput += onOutput;
                    try
                    {
                        var resPoints = resultPoints.Select(x => (CmdResultPoint)x).ToList();
                        connection.CreateResultPoint(resPoints);
                    }
                    finally
                    {
                        connection.OnOutput -= onOutput;
                    }
                }).GetAwaiter().GetResult();

                success = true;
            }
            catch (Exception ex)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Error, ex.Message);
                log.Add(ex.Message);
                success = false;
            }

            DA.SetData("Connection", handle);
            DA.SetDataList("Log", log);
            DA.SetData("Success", success);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{54EB08E8-69E7-41CB-9152-404245D5B7D6}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}


