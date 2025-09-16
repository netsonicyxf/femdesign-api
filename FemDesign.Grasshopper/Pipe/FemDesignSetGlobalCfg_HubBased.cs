// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
	/// <summary>
	/// Set global configurations using the shared hub connection (standard GH_Component, UI-blocking).
	/// Mirrors PipeSetGlobalCfg behavior.
	/// </summary>
	public class FemDesignSetGlobalCfg_HubBased : FEM_Design_API_Component
	{
		public FemDesignSetGlobalCfg_HubBased() : base("FEM-Design.SetGlobalConfigurations (Hub)", "SetGlobalCfg", "Set global settings for current model using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("GlobalConfig", "GlobCfg", "Filepath of global configuration file or GlobConfig objects.", GH_ParamAccess.list);
			pManager[pManager.ParamCount - 1].Optional = true;
		}

		protected override void RegisterOutputParams(GH_OutputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddBooleanParameter("Success", "Success", "True if global configuration applied.", GH_ParamAccess.item);
			pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
		}

		protected override void SolveInstance(IGH_DataAccess DA)
		{
			object handle = null;
			DA.GetData("Connection", ref handle);

			var globCfg = new List<dynamic>();
			DA.GetDataList("GlobalConfig", globCfg);

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
						if (globCfg.Count == 0)
						{
							string assemblyLocation = Assembly.GetExecutingAssembly().Location;
							var globCfgfilePath = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(assemblyLocation), @"cmdglobalcfg.xml");
							conn.SetGlobalConfig(globCfgfilePath);
						}
						else
						{
							foreach (var c in globCfg)
							{
								if (c is string s)
								{
									conn.SetGlobalConfig(s);
								}
								else if (c != null && c.Value is string)
								{
									string vs = c.Value as string;
                                    conn.SetGlobalConfig(vs);
								}
								else if (c is FemDesign.Calculate.GlobConfig cfgObj)
								{
									conn.SetGlobalConfig(cfgObj);
								}
								else if (c != null && c.Value is FemDesign.Calculate.GlobConfig)
								{
									FemDesign.Calculate.GlobConfig vCfgObj = c.Value as FemDesign.Calculate.GlobConfig;
                                    conn.SetGlobalConfig(vCfgObj);
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
		public override Guid ComponentGuid => new Guid("BC8A2A7D-8F2D-4B7B-9F52-5C6A8E2F3A44");
		public override GH_Exposure Exposure => GH_Exposure.obscure;
	}
}


