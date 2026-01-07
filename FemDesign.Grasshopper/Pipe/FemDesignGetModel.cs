// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Get the current open model using the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignGetModel : FEM_Design_API_Component
	{
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

		protected override void SolveInstance(IGH_DataAccess DA)
		{
            FemDesign.Grasshopper.FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			bool runNode = true;
			DA.GetData("RunNode", ref runNode);

			var log = new List<string>();
			bool success = false;
			Model model = null;

			if (!runNode)
			{
				this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
				DA.SetData("Connection", null);
				DA.SetData("Model", model);
				DA.SetData("Success", false);
				DA.SetDataList("Log", log);
				return;
			}

			try
			{
                FemDesignConnectionHub.InvokeAsync(handle.Id, conn =>
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
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Error, ex.Message);
                log.Add(ex.Message);
				success = false;
			}

            DA.SetData("Connection", handle);
			DA.SetData("Model", model);
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
		public override Guid ComponentGuid => new Guid("{65B2948C-4F04-4038-AC14-694091005DC5}");
		public override GH_Exposure Exposure => GH_Exposure.primary;
	}
}



