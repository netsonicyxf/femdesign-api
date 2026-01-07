// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Disconnects a specific FEM-Design hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignDisconnect : FEM_Design_API_Component
	{
		public FemDesignDisconnect() : base("FEM-Design.Disconnect", "Disconnect", "Detach and close the connection, but keeps open FEM-Design.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Connection handle to disconnect.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddBooleanParameter("Success", "Success", "True if disconnect succeeded.", GH_ParamAccess.item);
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

			if (!runNode)
			{
				this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
				DA.SetData("Success", false);
				DA.SetDataList("Log", log);
				return;
			}

			try
			{
				if (handle == null) 
					throw new Exception("'Connection' handle is null.");
				
				FemDesignConnectionHub.DisposeAsync(handle.Id, true).GetAwaiter().GetResult();
				success = true;
			}
			catch (Exception ex)
			{
				log.Add(ex.Message);
				success = false;
			}

			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Disconnect;
		public override Guid ComponentGuid => new Guid("{5A52243F-4136-48F0-9279-3E7E3DF82D2E}");
		public override GH_Exposure Exposure => GH_Exposure.primary;
	}
}


