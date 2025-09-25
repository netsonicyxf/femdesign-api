// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Get the current open model using the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignGetModel_HubBased : FEM_Design_API_Component
	{
		public FemDesignGetModel_HubBased() : base("FEM-Design.GetModel (Hub)", "GetModel", "Get the current open model in FEM-Design using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("Model", "Model", "Current FEM-Design model.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if succeeded.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
			object handle = null;
			DA.GetData("Connection", ref handle);

			var log = new List<string>();
			bool success = false;
			Model model = null;

			try
			{
				FemDesignConnectionHub.InvokeAsync(conn =>
				{
					void onOutput(string s) { log.Add(s); }
					conn.OnOutput += onOutput;
					try
					{
						model = conn.GetModel();
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

			DA.SetData("Connection", new object());
			DA.SetData("Model", model);
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
		public override Guid ComponentGuid => new Guid("B6A1C36B-2B99-4B9F-9C48-8F3D6A9F1E2C");
		public override GH_Exposure Exposure => GH_Exposure.primary;
	}
}


