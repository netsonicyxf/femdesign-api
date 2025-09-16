// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using FemDesign.Calculate;
using FemDesign.Results;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read load cases and load combinations results using the shared hub connection (standard GH_Component, UI-blocking).
    /// Mirrors PipeReadResults logic but executes via FemDesignConnectionHub.
    /// </summary>
    public class FemDesignGetCaseCombResults_HubBased : FEM_Design_API_Component
    {
        public FemDesignGetCaseCombResults_HubBased() : base("FEM-Design.GetCaseCombResults (Hub)", "CaseCombResults", "Read load cases and load combinations results from current model using shared connection.", CategoryName.Name(), SubCategoryName.CatHub())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("ResultType", "ResultType", "Result type names under FemDesign.Results namespace (e.g. 'NodalDisplacement').", GH_ParamAccess.list);
            pManager.AddTextParameter("Case Name", "Case Name", "Optional. Load case names to filter. If empty, all cases are considered.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddTextParameter("Combination Name", "Combo Name", "Optional. Load combination names to filter. If empty, all combinations are considered.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Elements", "Elements", "Optional. Elements for which the results will be returned. Default: all elements.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Options", "Options", "Optional settings for output location. Default is 'ByStep' and 'Vertices'.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Units", "Units", "Optional. Specify result units for specific types.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Results", "Results", "Results.", GH_ParamAccess.list);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            object handle = null;
            DA.GetData("Connection", ref handle);

            var resultTypes = new List<string>();
            DA.GetDataList("ResultType", resultTypes);

            var caseNames = new List<string>();
            DA.GetDataList("Case Name", caseNames);

            var comboNames = new List<string>();
            DA.GetDataList("Combination Name", comboNames);

            var elements = new List<FemDesign.GenericClasses.IStructureElement>();
            DA.GetDataList("Elements", elements);

            Results.UnitResults units = null;
            DA.GetData("Units", ref units);

            Options options = null;
            DA.GetData("Options", ref options);

            var log = new List<string>();
            bool success = false;
            var resultsTree = new DataTree<object>();

            try
            {
                FemDesignConnectionHub.InvokeAsync(conn =>
                {
                    void onOutput(string s) { log.Add(s); }
                    conn.OnOutput += onOutput;
                    try
                    {
                        int resIndex = 0;
                        foreach (var rt in resultTypes)
                        {
                            int caseIndex = 0;
                            int combIndex = 0;

                            string typeName = $"FemDesign.Results.{rt}, FemDesign.Core";
                            Type resultType = Type.GetType(typeName);
                            if (resultType == null)
                                throw new ArgumentException($"Class object of name '{typeName}' does not exist!");

                            // Helper to invoke private generic methods on FemDesignConnection
                            List<Results.IResult> InvokeGeneric(string methodName, Type genericType, object[] args)
                            {
                                var mi = conn.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(genericType);
                                var res = (IEnumerable<Results.IResult>)mi.Invoke(conn, args);
                                return res.ToList();
                            }

                            if (!comboNames.Any() && !caseNames.Any())
                            {
                                var res = InvokeGeneric(nameof(FemDesign.FemDesignConnection._getResults), resultType, new object[] { units, options, elements, true });
                                resultsTree.AddRange(res, new GH_Path(resIndex));
                            }

                            if (caseNames.Any())
                            {
                                foreach (var c in caseNames)
                                {
                                    var res = InvokeGeneric(nameof(FemDesign.FemDesignConnection._getLoadCaseResults), resultType, new object[] { new List<string> { c }, elements, units, options, true });
                                    resultsTree.AddRange(res, new GH_Path(resIndex, caseIndex));
                                    caseIndex++;
                                }
                            }

                            if (comboNames.Any())
                            {
                                combIndex = caseIndex;
                                foreach (var cmb in comboNames)
                                {
                                    var res = InvokeGeneric(nameof(FemDesign.FemDesignConnection._getLoadCombinationResults), resultType, new object[] { new List<string> { cmb }, elements, units, options, true });
                                    resultsTree.AddRange(res, new GH_Path(resIndex, combIndex));
                                    combIndex++;
                                }
                            }

                            resIndex++;
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
                log.Add(ex.InnerException?.Message ?? ex.Message);
                success = false;
            }

            DA.SetData("Connection", new object());
            DA.SetDataTree(1, resultsTree);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("D9B9F6B4-62C3-4D62-9E6B-9E2B1D5B2C8A");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}

 

