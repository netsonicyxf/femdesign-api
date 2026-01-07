// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Threading;
using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;

using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read load cases and load combinations results using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignGetCaseCombResults : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private List<string> _resultTypes;
        private List<string> _caseNames;
        private List<string> _comboNames;
        private List<FemDesign.GenericClasses.IStructureElement> _elements;
        private Results.UnitResults _units;
        private Options _options;
        private bool _runNode;

        // Output data
        private DataTree<object> _resultsTree;
        private List<string> _log;
        private bool _success;

        public FemDesignGetCaseCombResults() : base("FEM-Design.GetCaseCombResults", "CaseCombResults", "Read load cases and load combinations results from current model using shared connection. Result files (.csv) are saved into the output directory.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("ResultType", "ResultType", "Result type names (e.g. 'NodalDisplacement').", GH_ParamAccess.list);
            pManager.AddTextParameter("Case Name", "Case Name", "Optional. Load case names to filter. If empty, all cases are considered.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddTextParameter("Combination Name", "Combo Name", "Optional. Load combination names to filter. If empty, all combinations are considered.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Elements", "Elements", "Optional. Elements for which the results will be returned. Default: all elements.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Options", "Options", "Optional settings for output location. Default is 'ByStep' and 'Vertices'.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Units", "Units", "Optional. Specify result units for specific types." +
                "Default Units are: Length.m, Angle.deg, SectionalData.m, Force.kN, Mass.kg, Displacement.m, Stress.Pa", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Results", "Results", "Results.", GH_ParamAccess.list);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _resultTypes = new List<string>();
            DA.GetDataList("ResultType", _resultTypes);

            _caseNames = new List<string>();
            DA.GetDataList("Case Name", _caseNames);

            _comboNames = new List<string>();
            DA.GetDataList("Combination Name", _comboNames);

            _elements = new List<FemDesign.GenericClasses.IStructureElement>();
            DA.GetDataList("Elements", _elements);

            _units = null;
            DA.GetData("Units", ref _units);

            _options = null;
            DA.GetData("Options", ref _options);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _resultsTree = new DataTree<object>();
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

                    int resIndex = 0;
                    foreach (var rt in _resultTypes)
                    {
                        int caseIndex = 0;
                        int combIndex = 0;

                        string typeName = $"FemDesign.Results.{rt}, FemDesign.Core";
                        Type resultType = Type.GetType(typeName);

                        // Helper to invoke private generic methods on FemDesignConnection
                        List<Results.IResult> InvokeGeneric(string methodName, Type genericType, object[] args)
                        {
                            var mi = connection.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(genericType);
                            var res = (IEnumerable<Results.IResult>)mi.Invoke(connection, args);
                            return res.ToList();
                        }

                        if (!_comboNames.Any() && !_caseNames.Any())
                        {
                            var res = InvokeGeneric(nameof(FemDesign.FemDesignConnection._getResults), resultType, new object[] { _units, _options, _elements, true });
                            _resultsTree.AddRange(res, new GH_Path(resIndex));
                        }

                        if (_caseNames.Any())
                        {
                            foreach (var c in _caseNames)
                            {
                                var res = InvokeGeneric(nameof(FemDesign.FemDesignConnection._getLoadCaseResults), resultType, new object[] { new List<string> { c }, _elements, _units, _options, true });
                                _resultsTree.AddRange(res, new GH_Path(resIndex, caseIndex));
                                caseIndex++;
                            }
                        }

                        if (_comboNames.Any())
                        {
                            combIndex = caseIndex;
                            foreach (var cmb in _comboNames)
                            {
                                var res = InvokeGeneric(nameof(FemDesign.FemDesignConnection._getLoadCombinationResults), resultType, new object[] { new List<string> { cmb }, _elements, _units, _options, true });
                                _resultsTree.AddRange(res, new GH_Path(resIndex, combIndex));
                                combIndex++;
                            }
                        }

                        resIndex++;
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
            DA.SetDataTree(1, _resultsTree);
            DA.SetData("Success", _success);
            DA.SetDataList("Log", _log);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetDataTree(1, new DataTree<object>());
            DA.SetData("Success", false);
            DA.SetDataList("Log", _log ?? new List<string>());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{51BEFDB6-363C-4F5C-99B1-D75C5FA670F7}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}
