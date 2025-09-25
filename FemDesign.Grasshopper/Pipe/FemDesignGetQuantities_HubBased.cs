// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Get quantities using the shared hub connection (standard GH_Component, UI-blocking).
	/// Mirrors PipeGetQuantities behavior.
	/// </summary>
	public class FemDesignGetQuantities_HubBased : FEM_Design_API_Component
	{
		public FemDesignGetQuantities_HubBased() : base("FEM-Design.GetQuantities (Hub)", "GetQuantities", "Get quantities from current model using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("QuantityType", "QuantityType", "Quantity type name matching FemDesign.Results classes.", GH_ParamAccess.item);
			pManager.AddGenericParameter("Units", "Units", "Optional result units.", GH_ParamAccess.item);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("Quantities", "Quantities", "Quantities.", GH_ParamAccess.list);
			pManager.AddBooleanParameter("Success", "Success", "True if succeeded.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
			object handle = null;
			DA.GetData("Connection", ref handle);

			string resultTypeName = null;
			DA.GetData("QuantityType", ref resultTypeName);

			Results.UnitResults units = null;
			DA.GetData("Units", ref units);

			var log = new List<string>();
			bool success = false;
			var results = new List<Results.IResult>();

			try
			{
				FemDesignConnectionHub.InvokeAsync(conn =>
				{
					void onOutput(string s) { log.Add(s); }
					conn.OnOutput += onOutput;
					try
					{
						if (string.IsNullOrWhiteSpace(resultTypeName)) throw new Exception("'QuantityType' is null or empty.");
						string typeName = $"FemDesign.Results.{resultTypeName}, FemDesign.Core";
						Type resultType = Type.GetType(typeName);
						if (resultType == null) throw new ArgumentException($"Class object of name '{typeName}' does not exist!");

						var methodName = nameof(FemDesign.FemDesignConnection._getQuantities);
						var mi = conn.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(resultType);
						var res = (IEnumerable<Results.IResult>)mi.Invoke(conn, new object[] { units, true });
						results.AddRange(res);
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
			DA.SetDataList("Quantities", results);
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
		public override Guid ComponentGuid => new Guid("1F2D4C7A-6A39-4F73-9F20-1C5E9A7A4B62");
		public override GH_Exposure Exposure => GH_Exposure.tertiary;
	}
}


