// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Save documentation using the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignSaveDocumentation_HubBased : FEM_Design_API_Component
	{
		public FemDesignSaveDocumentation_HubBased() : base("FEM-Design.Documentation (Hub)", "SaveDocx", "Save documentation of current model using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("Docx", "Docx", "Docx file path for the documentation output.", GH_ParamAccess.item);
			pManager.AddTextParameter("Template", "Template", ".dsc template file path.", GH_ParamAccess.item);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if documentation saved.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			string docx = null;
			DA.GetData("Docx", ref docx);

			string template = null;
			DA.GetData("Template", ref template);

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
						if (string.IsNullOrWhiteSpace(docx)) throw new Exception("'Docx' path is null or empty.");
						conn.SaveDocx(docx, template);
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

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.Docx;
		public override Guid ComponentGuid => new Guid("C1A1D62B-2B2D-4F81-8C7B-21BC04C4B5B8");
		public override GH_Exposure Exposure => GH_Exposure.primary;
	}
}


