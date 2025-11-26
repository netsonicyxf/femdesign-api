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
	public class FemDesignSetGlobalCfg : FEM_Design_API_Component
	{
		public FemDesignSetGlobalCfg() : base("FEM-Design.SetGlobalConfigurations", "SetGlobalCfg", "Set global settings for current model using shared connection. It defines the calculation settings that will instruct FEM-Design in operation like creating the finite element mesh.", CategoryName.Name(), SubCategoryName.Cat8())
		{
		}

		protected override void RegisterInputParams(GH_InputParamManager pManager)
		{
			pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
			pManager.AddGenericParameter("GlobalConfig", "GlobCfg", "Filepath of global configuration file or GlobConfig objects.\nIf file path is not provided, the component will read the cmdglobalcfg.xml file in the package manager library folder.\n%AppData%\\McNeel\\Rhinoceros\\packages\\7.0\\FemDesign\\", GH_ParamAccess.list);
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
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

			var globCfg = new List<dynamic>();
			DA.GetDataList("GlobalConfig", globCfg);

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
						if (globCfg.Count == 0)
						{
							string assemblyLocation = Assembly.GetExecutingAssembly().Location;
							var globCfgfilePath = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(assemblyLocation), @"cmdglobalcfg.xml");
							connection.SetGlobalConfig(globCfgfilePath);
						}
						else
						{
							foreach (var c in globCfg)
							{
								if (c is string s)
								{
									connection.SetGlobalConfig(s);
								}
								else if (c != null && c.Value is string)
								{
									string vs = c.Value as string;
                                    connection.SetGlobalConfig(vs);
								}
								else if (c is FemDesign.Calculate.GlobConfig cfgObj)
								{
									connection.SetGlobalConfig(cfgObj);
								}
								else if (c != null && c.Value is FemDesign.Calculate.GlobConfig)
								{
									FemDesign.Calculate.GlobConfig vCfgObj = c.Value as FemDesign.Calculate.GlobConfig;
                                    connection.SetGlobalConfig(vCfgObj);
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
				log.Add(ex.Message);
				success = false;
			}

            DA.SetData("Connection", handle);
			DA.SetData("Success", success);
			DA.SetDataList("Log", log);
		}

		protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Config;
		public override Guid ComponentGuid => new Guid("{C223693E-139D-4A1C-8F02-F8618BEDB4BA}");
		public override GH_Exposure Exposure => GH_Exposure.obscure;
	}
}


