// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Open a model using the shared hub connection (standard GH_Component, UI-blocking).
    /// </summary>
    public class FemDesignOpen : FEM_Design_API_Component
    {
        public FemDesignOpen() : base("FEM-Design.OpenModel", "OpenModel", "Open model in FEM-Design using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Model", "Model", "Model to open or file path.", GH_ParamAccess.item);
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Model", "Model", "Opened model (round-tripped).", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

            dynamic modelIn = null;
            DA.GetData("Model", ref modelIn);

            var log = new List<string>();
            bool success = false;
            Model modelOut = null;

            try
            {
                // Block UI while invoking hub (acceptable per requirements)
                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
                {
                    void onOutput(string s) { log.Add(s); }
                    connection.OnOutput += onOutput;
                    try
                    {
                        if (modelIn is string path)
                        {
                            connection.Open(path);
                        }
                        else if (modelIn is Model m)
                        {
                            connection.Open(m);
                        }
                        else if (modelIn != null && modelIn.Value is string)
                        {
                            string vpath = modelIn.Value as string;
                            connection.Open(vpath);
                        }
                        else if (modelIn != null && modelIn.Value is Model)
                        {
                            Model vm = modelIn.Value as Model;
                            connection.Open(vm);
                        }
                        else
                        {
                            throw new Exception("Unsupported 'Model' input. Provide file path or FemDesign.Model.");
                        }

                        modelOut = connection.GetModel();
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
            DA.SetData("Model", modelOut);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_open;
        public override Guid ComponentGuid => new Guid("{667EFCEA-8B2D-4516-ADC5-DBC08585CBA1}");
        public override GH_Exposure Exposure => GH_Exposure.primary;
    }
}


