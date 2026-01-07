// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using Grasshopper;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;

using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read load cases and load combinations results using the shared hub connection (standard GH_Component, UI-blocking).
    /// Mirrors PipeReadResults logic but executes via FemDesignConnectionHub.
    /// </summary>
    public class FemDesignGetCaseCombResults : FEM_Design_API_Component
    {
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

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesignHubHandle handle = null;
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

            bool runNode = true;
            DA.GetData("RunNode", ref runNode);

            var log = new List<string>();
            bool success = false;
            var resultsTree = new DataTree<object>();

            if (!runNode)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
                DA.SetData("Connection", null);
                DA.SetDataTree(1, resultsTree);
                DA.SetData("Success", false);
                DA.SetDataList("Log", log);
                return;
            }

            try
            {
                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
                {
                    void onOutput(string s) { log.Add(s); }
                    connection.OnOutput += onOutput;
                    try
                    {
                        int resIndex = 0;
                        foreach (var rt in resultTypes)
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
                        connection.OnOutput -= onOutput;
                    }
                }).GetAwaiter().GetResult();

                success = true;
            }
            catch (Exception ex)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Error, ex.Message);
                log.Add(ex.InnerException?.Message ?? ex.Message);
                success = false;
            }

            DA.SetData("Connection", handle);
            DA.SetDataTree(1, resultsTree);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{51BEFDB6-363C-4F5C-99B1-D75C5FA670F7}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}

 

