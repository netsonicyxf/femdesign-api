// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Open a model using the shared hub connection (standard GH_Component, UI-blocking).
    /// </summary>
    public class FemDesignOpen_HubBased : FEM_Design_API_Component
    {
        public FemDesignOpen_HubBased() : base("FEM-Design.Open (Hub)", "Open", "Open model in FEM-Design using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Model", "Model", "Model object or file path.", GH_ParamAccess.item);
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Model", "Model", "Opened model (round-tripped).", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            object handle = null;
            DA.GetData("Connection", ref handle);

            dynamic modelIn = null;
            DA.GetData("Model", ref modelIn);

            var log = new List<string>();
            bool success = false;
            Model modelOut = null;

            try
            {
                // Block UI while invoking hub (acceptable per requirements)
                FemDesignConnectionHub.InvokeAsync(conn =>
                {
                    void onOutput(string s) { log.Add(s); }
                    conn.OnOutput += onOutput;
                    try
                    {
                        if (modelIn is string path)
                        {
                            conn.Open(path);
                        }
                        else if (modelIn is Model m)
                        {
                            conn.Open(m);
                        }
                        else if (modelIn != null && modelIn.Value is string vpath)
                        {
                            conn.Open(vpath);
                        }
                        else if (modelIn != null && modelIn.Value is Model vm)
                        {
                            conn.Open(vm);
                        }
                        else
                        {
                            throw new Exception("Unsupported 'Model' input. Provide file path or FemDesign.Model.");
                        }

                        modelOut = conn.GetModel();
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

            DA.SetData("Model", modelOut);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_open;
        public override Guid ComponentGuid => new Guid("7E2C6206-7B4A-4C6F-8F39-59B324F11213");
        public override GH_Exposure Exposure => GH_Exposure.primary;
    }
}


