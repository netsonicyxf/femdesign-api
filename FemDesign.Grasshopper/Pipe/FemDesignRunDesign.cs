// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;
using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Run design using the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignRunDesign : FEM_Design_API_Component
	{
		public FemDesignRunDesign() : base("FEM-Design.RunDesign", "RunDesign", "Run design on current/open model using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("Design", "Design", "Design settings.", GH_ParamAccess.item);
			pManager.AddGenericParameter("DesignGroup", "DesignGroup", "Optional design groups.", GH_ParamAccess.list);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if design succeeded.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			Design design = null;
			DA.GetData("Design", ref design);

			var designGroups = new List<CmdDesignGroup>();
			DA.GetDataList("DesignGroup", designGroups);

			var log = new List<string>();
			bool success = false;

            // check inputs
            if (design == null) 
				throw new Exception("'Design' input is null.");

            try
            {
                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
				{
					void onOutput(string s) { log.Add(s); }
					connection.OnOutput += onOutput;
					try
					{
						var userModule = design.Mode;
						connection.RunDesign(userModule, design, designGroups);
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

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_RunDesign;
		public override Guid ComponentGuid => new Guid("{0F185ABC-C496-4C6A-A59C-848ADE3A8390}");
		public override GH_Exposure Exposure => GH_Exposure.secondary;
	}
}


