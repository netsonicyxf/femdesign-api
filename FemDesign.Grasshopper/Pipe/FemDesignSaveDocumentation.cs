// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Save documentation using the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignSaveDocumentation : FEM_Design_API_Component
	{
		public FemDesignSaveDocumentation() : base("FEM-Design.Documentation", "SaveDocx", "Save documentation of current model using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("Docx", "Docx", "Docx file path for the documentation output.", GH_ParamAccess.item);
			pManager.AddTextParameter("Template", "Template", ".dsc template file path.", GH_ParamAccess.item);
			pManager[pManager.ParamCount - 1].Optional = true;
			pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
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

			bool runNode = true;
			DA.GetData("RunNode", ref runNode);

			var log = new List<string>();
			bool success = false;

			if (!runNode)
			{
				this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
				DA.SetData("Connection", null);
				DA.SetData("Success", false);
				DA.SetDataList("Log", log);
				return;
			}

            // check inputs
            if (string.IsNullOrWhiteSpace(docx)) 
				throw new Exception("'Docx' path is null or empty.");

            try
            {
                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
				{
					void onOutput(string s) { log.Add(s); }
					connection.OnOutput += onOutput;
					try
					{
						connection.SaveDocx(docx, template);
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
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.Docx;
		public override Guid ComponentGuid => new Guid("{B7AD9265-2AAE-4562-9B47-DB178F69839D}");
		public override GH_Exposure Exposure => GH_Exposure.primary;
	}
}


