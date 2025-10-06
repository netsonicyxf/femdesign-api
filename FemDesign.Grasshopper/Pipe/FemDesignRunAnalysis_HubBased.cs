// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;
using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Run analysis using the shared hub connection (standard GH_Component, UI-blocking).
    /// </summary>
    public class FemDesignRunAnalysis_HubBased : FEM_Design_API_Component
    {
        public FemDesignRunAnalysis_HubBased() : base("FEM-Design.RunAnalysis (Hub)", "RunAnalysis", "Run analysis on current/open model using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Analysis", "Analysis", "Analysis settings.", GH_ParamAccess.item);
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if analysis succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesign.Grasshopper.FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

            Analysis analysis = null;
            DA.GetData("Analysis", ref analysis);

            var log = new List<string>();
            bool success = false;

            try
            {
                FemDesignConnectionHub.InvokeAsync(handle.Id, conn =>
                {
                    void onOutput(string s) { log.Add(s); }
                    conn.OnOutput += onOutput;
                    try
                    {
                        if (analysis == null) throw new Exception("'Analysis' input is null.");
                        conn.RunAnalysis(analysis);
                    }
                    finally
                    {
                        conn.OnOutput -= onOutput;
                    }
                }).GetAwaiter().GetResult();

                success = true;
            }
            catch (Exception ex)
            {
                log.Add(ex.Message);
                success = false;
            }

            DA.SetData("Connection", handle);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_RunAnalysis;
        public override Guid ComponentGuid => new Guid("E3E3A9B8-68C4-4B9F-BE18-ACC6E9C8B852");
        public override GH_Exposure Exposure => GH_Exposure.primary;
    }
}



