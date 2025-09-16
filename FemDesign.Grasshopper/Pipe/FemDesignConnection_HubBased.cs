// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Configures the shared FemDesignConnectionHub and exposes a lightweight handle.
    /// </summary>
    public class FemDesignConnection_HubBased : FEM_Design_API_Component
    {
        public FemDesignConnection_HubBased() : base("FEM-Design.Connection (Hub)", "Connection", "Create or configure a shared FEM-Design connection.", CategoryName.Name(), SubCategoryName.CatHub())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddTextParameter("FEM-Design dir", "FEM-Design dir", "Path to FEM-Design installation.", GH_ParamAccess.item, @"C:\\Program Files\\StruSoft\\FEM-Design 24\\");
            pManager[pManager.ParamCount - 1].Optional = true;

            pManager.AddBooleanParameter("Minimized", "Minimized", "Start FEM-Design minimized.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;

            pManager.AddTextParameter("OutputDir", "OutputDir", "Directory for scripts/logs. Default: GH file directory or temp.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;

            pManager.AddBooleanParameter("DeleteOutputFolder", "DeleteOutputFolder", "Delete output directory on disconnect.", GH_ParamAccess.item, false);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            string fdDir = @"C:\\Program Files\\StruSoft\\FEM-Design 24\\";
            DA.GetData("FEM-Design dir", ref fdDir);

            bool minimized = true;
            DA.GetData("Minimized", ref minimized);

            string outputDir = null;
            DA.GetData("OutputDir", ref outputDir);

            bool deleteOutput = false;
            DA.GetData("DeleteOutputFolder", ref deleteOutput);

            // Set working directory similarly to existing component behavior
            bool fileExist = OnPingDocument().IsFilePathDefined;
            if (!fileExist)
            {
                string tempPath = System.IO.Path.GetTempPath();
                System.IO.Directory.SetCurrentDirectory(tempPath);
            }
            else
            {
                var filePath = OnPingDocument().FilePath;
                var currentDir = System.IO.Path.GetDirectoryName(filePath);
                System.IO.Directory.SetCurrentDirectory(currentDir);
            }

            FemDesignConnectionHub.Configure(fdDir, minimized, outputDir, deleteOutput);

            // Emit a simple token/handle to wire downstream (no real object needed since hub is static)
            DA.SetData("Connection", new object());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Connection;
        public override Guid ComponentGuid => new Guid("9F2B6F6D-9EB8-4B0A-9B55-9B3E3B5B5D67");
        public override GH_Exposure Exposure => GH_Exposure.primary;
    }
}


