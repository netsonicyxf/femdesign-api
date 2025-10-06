// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Disconnects a specific FEM-Design hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignDisconnect_HubBased : FEM_Design_API_Component
	{
		public FemDesignDisconnect_HubBased() : base("FEM-Design.Disconnect (Hub)", "Disconnect", "Close the FEM-Design instance associated with the given hub connection.", CategoryName.Name(), SubCategoryName.CatHub())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Hub connection handle to disconnect.", GH_ParamAccess.item);
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Same handle (now disposed).", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if disconnect succeeded.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
			FemDesign.Grasshopper.FemDesignHubHandle handle = null;
			DA.GetData("Connection", ref handle);

			var log = new List<string>();
			bool success = false;

			try
			{
				if (handle == null) throw new Exception("'Connection' handle is null.");
				FemDesignConnectionHub.DisposeAsync(handle.Id).GetAwaiter().GetResult();
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

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Connection;
		public override Guid ComponentGuid => new Guid("D1D3C1D9-0E4F-4A5E-8C6B-3C1A4E2B9D61");
		public override GH_Exposure Exposure => GH_Exposure.secondary;
	}
}


