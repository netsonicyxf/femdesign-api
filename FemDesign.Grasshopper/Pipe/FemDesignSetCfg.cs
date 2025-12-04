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
	public class FemDesignSetCfg : FEM_Design_API_Component
	{
		public FemDesignSetCfg() : base("FEM-Design.SetConfigurations", "SetCfg", "Set design settings for current model using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("Config", "Cfg", "Filepath of the configuration file or Config objects.\nIf file path is not provided, the component will read the cfg.xml file in the package manager library folder.\n%AppData%\\McNeel\\Rhinoceros\\packages\\7.0\\FemDesign\\", GH_ParamAccess.list);
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
			FemDesignHubHandle handle = null;
			DA.GetData("Connection", ref handle);

			var cfg = new List<dynamic>();
			DA.GetDataList("Config", cfg);

			var log = new List<string>();
			bool success = false;

			try
			{
				FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
				{
					void onOutput(string s) { log.Add(s); }
					connection.OnOutput += onOutput;
					try
					{
						if (cfg.Count == 0)
						{
							string assemblyLocation = Assembly.GetExecutingAssembly().Location;
							var cfgfilePath = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(assemblyLocation), @"cfg.xml");
							connection.SetConfig(cfgfilePath);
						}
						else
						{
							foreach (var c in cfg)
							{
								if (c is string s)
								{
									connection.SetConfig(s);
								}
								else if (c != null && c.Value is string)
								{
									string vs = c.Value as string;
                                    connection.SetConfig(vs);
								}
								else if (c is FemDesign.Calculate.CONFIG cfgObj)
								{
									connection.SetConfig(cfgObj);
								}
								else if (c != null && c.Value is FemDesign.Calculate.CONFIG)
								{
                                    FemDesign.Calculate.CONFIG vCfgObj = c.Value as FemDesign.Calculate.CONFIG;
                                    connection.SetConfig(vCfgObj);
								}
							}
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
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Config;
		public override Guid ComponentGuid => new Guid("{24BCEA1D-13E7-47D0-B0F8-4403B0912D44}");
		public override GH_Exposure Exposure => GH_Exposure.obscure;
	}
}


