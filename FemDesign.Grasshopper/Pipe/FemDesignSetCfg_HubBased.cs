// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Set configurations using the shared hub connection (standard GH_Component, UI-blocking).
	/// Mirrors PipeSetCfg behavior.
	/// </summary>
	public class FemDesignSetCfg_HubBased : FEM_Design_API_Component
	{
		public FemDesignSetCfg_HubBased() : base("FEM-Design.SetConfigurations (Hub)", "SetCfg", "Set design settings for current model using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("Config", "Cfg", "Filepath of configuration file or Config objects.", GH_ParamAccess.list);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if configuration applied.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
			object handle = null;
			DA.GetData("Connection", ref handle);

			var cfg = new List<dynamic>();
			DA.GetDataList("Config", cfg);

			var log = new List<string>();
			bool success = false;

			try
			{
				FemDesignConnectionHub.InvokeAsync(conn =>
				{
					void onOutput(string s) { log.Add(s); }
					conn.OnOutput += onOutput;
					try
					{
						if (cfg.Count == 0)
						{
							string assemblyLocation = Assembly.GetExecutingAssembly().Location;
							var cfgfilePath = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(assemblyLocation), @"cfg.xml");
							conn.SetConfig(cfgfilePath);
						}
						else
						{
							foreach (var c in cfg)
							{
								if (c is string s)
								{
									conn.SetConfig(s);
								}
								else if (c != null && c.Value is string)
								{
									string vs = c.Value as string;
                                    conn.SetConfig(vs);
								}
								else if (c is FemDesign.Calculate.CONFIG cfgObj)
								{
									conn.SetConfig(cfgObj);
								}
								else if (c != null && c.Value is FemDesign.Calculate.CONFIG)
								{
                                    FemDesign.Calculate.CONFIG vCfgObj = c.Value as FemDesign.Calculate.CONFIG;
                                    conn.SetConfig(vCfgObj);
								}
							}
						}
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
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Config;
		public override Guid ComponentGuid => new Guid("A8F2D25E-9D7D-4CF9-8B50-ED8F5C6A3B11");
		public override GH_Exposure Exposure => GH_Exposure.obscure;
	}
}


