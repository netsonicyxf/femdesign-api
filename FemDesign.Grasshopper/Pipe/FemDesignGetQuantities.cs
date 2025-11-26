// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using Grasshopper.Kernel;

using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Get quantities using the shared hub connection (standard GH_Component, UI-blocking).
	/// Mirrors PipeGetQuantities behavior.
	/// </summary>
	public class FemDesignGetQuantities: FEM_Design_API_Component
	{
		public FemDesignGetQuantities() : base("FEM-Design.GetQuantities", "GetQuantities", "Get quantities from current model using shared connection. Result files (.csv) are saved into the output directory.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("QuantityType", "QuantityType", "Quantity type:\n\n" +
                nameof(ListProc.QuantityEstimationConcrete) + "\n" +
                nameof(ListProc.QuantityEstimationReinforcement) + "\n" +
                nameof(ListProc.QuantityEstimationSteel) + "\n" +
                nameof(ListProc.QuantityEstimationTimber) + "\n" +
                nameof(ListProc.QuantityEstimationTimberPanel) + "\n" +
                nameof(ListProc.QuantityEstimationMasonry) + "\n" +
                nameof(ListProc.QuantityEstimationGeneral) + "\n" +
                nameof(ListProc.QuantityEstimationProfiledPanel), GH_ParamAccess.item);
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
            FemDesign.Grasshopper.FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			string resultTypeName = null;
			DA.GetData("QuantityType", ref resultTypeName);

			Results.UnitResults units = null;
			DA.GetData("Units", ref units);

			var log = new List<string>();
			bool success = false;
			var results = new List<Results.IResult>();

            // check inputs
            if (string.IsNullOrWhiteSpace(resultTypeName)) 
				throw new Exception("'QuantityType' is null or empty.");

            // try getting the quantity result type
            string typeName = $"FemDesign.Results.{resultTypeName}, FemDesign.Core";
            Type resultType = Type.GetType(typeName);
            if (resultType == null) 
				throw new ArgumentException($"QuantityType '{typeName}' does not exist!");

            try
			{
                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
				{
					void onOutput(string s) { log.Add(s); }
					connection.OnOutput += onOutput;
					try
					{
						var methodName = nameof(FemDesign.FemDesignConnection._getQuantities);
						var method = connection.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(resultType);
						var res = (IEnumerable<Results.IResult>)method.Invoke(connection, new object[] { units, false });
						results.AddRange(res);
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
				log.Add(ex.Message);
				success = false;
			}

			DA.SetData("Connection", handle);
			DA.SetDataList("Quantities", results);
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
		public override Guid ComponentGuid => new Guid("{4498FBC1-1EA9-4885-8658-FF79652C51CB}");
		public override GH_Exposure Exposure => GH_Exposure.tertiary;
	}
}



