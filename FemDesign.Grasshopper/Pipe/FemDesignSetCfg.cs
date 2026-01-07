// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using System.Threading;
using Grasshopper.Kernel;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Set configurations using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignSetCfg : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private List<dynamic> _cfg;
        private bool _runNode;

        // Output data
        private List<string> _log;
        private bool _success;

        public FemDesignSetCfg() : base("FEM-Design.SetConfigurations", "SetCfg", "Set design settings for current model using shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Config", "Cfg", "Filepath of the configuration file or Config objects.\nIf file path is not provided, the component will read the cfg.xml file in the package manager library folder.\n%AppData%\\McNeel\\Rhinoceros\\packages\\7.0\\FemDesign\\", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if configuration applied.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _cfg = new List<dynamic>();
            DA.GetDataList("Config", _cfg);

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

                    if (_cfg.Count == 0)
                    {
                        string assemblyLocation = Assembly.GetExecutingAssembly().Location;
                        var cfgfilePath = System.IO.Path.Combine(System.IO.Path.GetDirectoryName(assemblyLocation), @"cfg.xml");
                        connection.SetConfig(cfgfilePath);
                    }
                    else
                    {
                        foreach (var c in _cfg)
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
        public override Guid ComponentGuid => new Guid("{24BCEA1D-13E7-47D0-B0F8-4403B0912D44}");
        public override GH_Exposure Exposure => GH_Exposure.obscure;
    }
}
