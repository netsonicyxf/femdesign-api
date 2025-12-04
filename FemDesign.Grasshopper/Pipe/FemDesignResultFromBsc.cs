// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using Grasshopper;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Extract results from a model using a .bsc file with the shared hub connection (standard GH_Component, UI-blocking).
	/// </summary>
	public class FemDesignResultFromBsc : FEM_Design_API_Component
	{
		public FemDesignResultFromBsc() : base("FEM-Design.GetResultFromBsc", "ResultFromBsc", "Extract results using a .bsc file with shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("BscFilePath", "BscFilePath", "File path(s) to .bsc batch-file(s).", GH_ParamAccess.list);
			pManager.AddTextParameter("CsvFilePath", "CsvFilePath", "Optional output .csv path(s). If not set, results are saved next to the .bsc file(s).", GH_ParamAccess.list);
			pManager[pManager.ParamCount - 1].Optional = true;
			pManager.AddGenericParameter("Elements", "Elements", "Optional elements filter.", GH_ParamAccess.list);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddTextParameter("Results", "Results", "Results as data tree (CSV paths).", GH_ParamAccess.tree);
			pManager.AddBooleanParameter("Success", "Success", "True if succeeded.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			var bscPaths = new List<string>();
			DA.GetDataList("BscFilePath", bscPaths);

			var csvPaths = new List<string>();
			DA.GetDataList("CsvFilePath", csvPaths);

			var elements = new List<FemDesign.GenericClasses.IStructureElement>();
			DA.GetDataList("Elements", elements);

			var log = new List<string>();
			bool success = false;
			var resultsTree = new DataTree<object>();

			try
			{
				FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
				{
					void onOutput(string s) { log.Add(s); }
					connection.OnOutput += onOutput;
					try
					{
						if (csvPaths == null || csvPaths.Count == 0)
						{
							csvPaths = bscPaths.Select(b => System.IO.Path.ChangeExtension(b, "csv")).ToList();
						}

						var results = bscPaths.Zip(csvPaths, (bsc, csv) => connection.GetResultsFromBsc(bsc, csv, elements));
						int i = 0;
						foreach (var r in results)
						{
							resultsTree.AddRange(r, new GH_Path(i));
							i++;
						}
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
			DA.SetDataTree(1, resultsTree);
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
		public override Guid ComponentGuid => new Guid("{59667BED-D84B-47E7-BC56-B6D99DC5C274}");
		public override GH_Exposure Exposure => GH_Exposure.tertiary;
	}
}



