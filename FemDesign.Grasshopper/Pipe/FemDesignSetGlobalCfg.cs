// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using System.Threading;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Set global configurations using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignSetGlobalCfg : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private List<dynamic> _globCfg;
        private bool _runNode;

        // Output data
        private List<string> _log;
        private bool _success;

        public FemDesignSetGlobalCfg() : base("FEM-Design.SetGlobalConfigurations", "SetGlobalCfg", "Set global settings for current model using shared connection. It defines the calculation settings that will instruct FEM-Design in operation like creating the finite element mesh.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("GlobalConfig", "GlobCfg", "Filepath of global configuration file or GlobConfig objects.\nIf file path is not provided, the component will read the cmdglobalcfg.xml file in the package manager library folder.\n%AppData%\\McNeel\\Rhinoceros\\packages\\7.0\\FemDesign\\", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if global configuration applied.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _globCfg = new List<dynamic>();
            DA.GetDataList("GlobalConfig", _globCfg);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _log = new List<string>();
            _success = false;
        }

        protected override bool ShouldExecute()
        {
            if (!_runNode)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
                return false;
            }
            if (_handle == null)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Connection input is null.");
                return false;
            }
            return true;
        }

        protected override void ExecuteWork(CancellationToken cancellationToken)
        {
            cancellationToken.ThrowIfCancellationRequested();

            FemDesignConnectionHub.InvokeAsync(_handle.Id, connection =>
            {
                void onOutput(string s) { _log.Add(s); }
                connection.OnOutput += onOutput;
                try
                {
                    cancellationToken.ThrowIfCancellationRequested();

                    if (_globCfg.Count == 0)
                    {
                        string assemblyLocation = Assembly.GetExecutingAssembly().Location;
                        var globCfgfilePath = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(assemblyLocation), @"cmdglobalcfg.xml");
                        connection.SetGlobalConfig(globCfgfilePath);
                    }
                    else
                    {
                        foreach (var c in _globCfg)
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

            _success = true;
        }

        protected override void SetOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", _handle);
            DA.SetData("Success", _success);
            DA.SetDataList("Log", _log);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetData("Success", false);
            DA.SetDataList("Log", _log ?? new List<string>());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_Config;
        public override Guid ComponentGuid => new Guid("{C223693E-139D-4A1C-8F02-F8618BEDB4BA}");
        public override GH_Exposure Exposure => GH_Exposure.obscure;
    }
}
