// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Save model using the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignSaveAs_HubBased : FEM_Design_API_Component
	{
		public FemDesignSaveAs_HubBased() : base("FEM-Design.Save (Hub)", "Save", "Save the current model using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("FilePath", "FilePath", "Save the model to .struxml or .str file.", GH_ParamAccess.item);
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if save succeeded.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			string filePath = null;
			DA.GetData("FilePath", ref filePath);

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
						if (string.IsNullOrWhiteSpace(filePath)) throw new Exception("'FilePath' is null or empty.");
						conn.Save(filePath);
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

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_SaveAs;
		public override Guid ComponentGuid => new Guid("7C4F2E2B-5B9A-4F7B-BB38-2E7C6F3A1D42");
		public override GH_Exposure Exposure => GH_Exposure.primary;
	}
}


