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
using FemDesign.Results.Utils;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read stability results using the shared hub connection (standard GH_Component, UI-blocking).
    /// Mirrors PipeStabilityResults behavior without the async workaround.
    /// </summary>
    public class FemDesignGetStabilityResults : FEM_Design_API_Component
    {
        public FemDesignGetStabilityResults() : base("FEM-Design.GetStabilityResults", "StabilityResults", "Read stability results from current model using shared connection. Result files (.csv) are saved into the output directory.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("Combination Name", "Combo Name", "Optional parameter. If not defined, all load combinations will be listed.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddIntegerParameter("ShapeId", "ShapeId", "Buckling shape identifier must be greater or equal to 1. Optional parameter. If not defined, all shapes will be listed.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Options", "Options", "Settings for output location. Default is 'ByStep' and 'Vertices'.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Units", "Units", "Specify the Result Units for some specific type.\nDefault Units are: Length.m, Angle.deg, SectionalData.m, Force.kN, Mass.kg, Displacement.m, Stress.Pa", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("BucklingShapes", "Shapes", "Buckling shape results.", GH_ParamAccess.tree);
            pManager.AddGenericParameter("CriticalParameter", "CritParam", "Critical parameters.", GH_ParamAccess.tree);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

            var combos = new List<string>();
            DA.GetDataList("Combination Name", combos);

            var shapeIds = new List<int>();
            DA.GetDataList("ShapeId", shapeIds);

            Options options = null;
            DA.GetData("Options", ref options);

            Results.UnitResults units = null;
            DA.GetData("Units", ref units);

            var log = new List<string>();
            bool success = false;

            var bucklingTree = new DataTree<FemDesign.Results.NodalBucklingShape>();
            var critParameterTree = new DataTree<FemDesign.Results.CriticalParameter>();

            try
            {
                if (handle == null)
                    throw new Exception("Connection handle is null.");

                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
                {
                    void onOutput(string s) { log.Add(s); }
                    connection.OnOutput += onOutput;
                    try
                    {
                        // helper to invoke private generic _getStabilityResults
                        List<IResult> InvokeStabilityResults(Type resultType, string loadCombination = null, int? shapeId = null)
                        {
                            string methodName = nameof(FemDesign.FemDesignConnection._getStabilityResults);
                            MethodInfo genericMethod = connection.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(resultType);
                            var shapeList = shapeId.HasValue ? new List<int> { shapeId.Value } : null;
                            var combList = loadCombination != null ? new List<string> { loadCombination } : null;
                            var res = (IEnumerable<IResult>)genericMethod.Invoke(connection, new object[] { combList, shapeList, units, options, false });
                            return res.ToList();
                        }

                        // read full result sets
                        var bucklingRes = InvokeStabilityResults(typeof(FemDesign.Results.NodalBucklingShape)).Cast<FemDesign.Results.NodalBucklingShape>().ToList();
                        var critParamRes = InvokeStabilityResults(typeof(FemDesign.Results.CriticalParameter)).Cast<FemDesign.Results.CriticalParameter>().ToList();

                        if (bucklingRes.Count == 0)
                            throw new Exception("Stability results have not been found. Have you run the Stability analysis?");

                        // validate filters
                        ValidateCombos(bucklingRes, combos);
                        ValidateShapes(bucklingRes, shapeIds);

                        // build trees and filter
                        var rawBucklingTree = CreateBucklingTree(bucklingRes);
                        bucklingTree = FilterBucklingTree(rawBucklingTree, combos, shapeIds);

                        string critParamPropName = nameof(CriticalParameter.CaseIdentifier);
                        var rawCritTree = critParamRes.CreateResultTree(critParamPropName);
                        critParameterTree = FilterCriticalTree(rawCritTree, combos, shapeIds);
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
            DA.SetDataTree(1, bucklingTree);
            DA.SetDataTree(2, critParameterTree);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        private static void ValidateCombos(List<FemDesign.Results.NodalBucklingShape> results, List<string> combos)
        {
            if (!combos.Any())
                return;

            var caseIds = results.Select(x => x.CaseIdentifier).Distinct().ToList();
            foreach (var comb in combos)
            {
                if (!caseIds.Contains(comb, StringComparer.OrdinalIgnoreCase))
                    throw new ArgumentException($"Incorrect or unknown load combination name: {comb}.");
            }
        }

        private static void ValidateShapes(List<FemDesign.Results.NodalBucklingShape> results, List<int> shapes)
        {
            if (!shapes.Any())
                return;

            var shapeIds = results.Select(x => x.Shape).Distinct().ToList();
            foreach (var shape in shapes)
            {
                if (!shapeIds.Contains(shape))
                    throw new ArgumentException($"ShapeId {shape} is out of range.");
            }
        }

        private static DataTree<FemDesign.Results.NodalBucklingShape> CreateBucklingTree(List<FemDesign.Results.NodalBucklingShape> results)
        {
            var uniqueCaseId = results.Select(x => x.CaseIdentifier).Distinct().ToList();
            var uniqueShape = results.Select(x => x.Shape).Distinct().ToList();
            var resultsTree = new DataTree<FemDesign.Results.NodalBucklingShape>();

            for (int i = 0; i < uniqueCaseId.Count; i++)
            {
                var allResultsByCaseId = results.Where(r => r.CaseIdentifier == uniqueCaseId[i]).ToList();

                for (int j = 0; j < uniqueShape.Count; j++)
                {
                    var pathData = allResultsByCaseId.Where(s => s.Shape == uniqueShape[j]).ToList();
                    resultsTree.AddRange(pathData, new GH_Path(i, j));
                }
            }

            // remove empty branches
            var emptyPath = new List<GH_Path>();
            for (int i = 0; i < resultsTree.BranchCount; i++)
            {
                var path = resultsTree.Paths[i];
                var branch = resultsTree.Branches[i];
                if (!branch.Any())
                    emptyPath.Add(path);
            }

            foreach (var item in emptyPath)
                resultsTree.RemovePath(item);

            return resultsTree;
        }

        private static DataTree<FemDesign.Results.NodalBucklingShape> FilterBucklingTree(DataTree<FemDesign.Results.NodalBucklingShape> tree, List<string> loadCombinations, List<int> shapeIds)
        {
            var removable = new List<GH_Path>();
            var filteredTree = tree;

            for (int i = 0; i < filteredTree.BranchCount; i++)
            {
                var path = filteredTree.Paths[i];
                var branch = filteredTree.Branches[i].ToList();

                if (loadCombinations.Any() && !loadCombinations.Contains(branch[0].CaseIdentifier, StringComparer.OrdinalIgnoreCase))
                    removable.Add(path);

                if (shapeIds.Any() && !shapeIds.Contains(branch[0].Shape))
                    removable.Add(path);
            }

            foreach (var item in removable)
                filteredTree.RemovePath(item);

            if (removable.Any())
                filteredTree = RenumberBucklingTree(filteredTree);

            return filteredTree;
        }

        private static DataTree<FemDesign.Results.CriticalParameter> FilterCriticalTree(DataTree<FemDesign.Results.CriticalParameter> tree, List<string> loadCombinations, List<int> shapeIds)
        {
            var removable = new List<GH_Path>();
            var filteredTree = tree;

            for (int i = 0; i < filteredTree.BranchCount; i++)
            {
                var path = filteredTree.Paths[i];
                var branch = filteredTree.Branches[i].ToList();

                if (loadCombinations.Any() && !loadCombinations.Contains(branch[0].CaseIdentifier, StringComparer.OrdinalIgnoreCase))
                {
                    removable.Add(path);
                    continue;
                }

                if (shapeIds.Any())
                {
                    for (int j = branch.Count - 1; j >= 0; j--)
                    {
                        if (!shapeIds.Contains(branch[j].Shape))
                            filteredTree.Branches[i].RemoveAt(j);
                    }
                }
            }

            foreach (var item in removable)
                filteredTree.RemovePath(item);

            if (removable.Any())
                filteredTree.RenumberPaths();

            return filteredTree;
        }

        private static DataTree<FemDesign.Results.NodalBucklingShape> RenumberBucklingTree(DataTree<FemDesign.Results.NodalBucklingShape> tree)
        {
            var orderedTree = new DataTree<FemDesign.Results.NodalBucklingShape>();
            if (tree.BranchCount == 0)
                return orderedTree;

            int i = 0;
            int j = 0;

            orderedTree.AddRange(tree.Branches[0], new GH_Path(0, 0));

            for (int b = 1; b < tree.Branches.Count; b++)
            {
                var currentBranch = tree.Branches[b];
                var previousBranch = tree.Branches[b - 1];

                if (currentBranch[0].CaseIdentifier != previousBranch[0].CaseIdentifier)
                {
                    i++;
                    j = 0;
                }
                else if (currentBranch[0].Shape != previousBranch[0].Shape)
                {
                    j++;
                }

                var path = new GH_Path(i, j);
                orderedTree.AddRange(currentBranch, path);
            }

            return orderedTree;
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{8A0E7239-F4F1-4FC7-AE79-FB4D7F2EC9DD}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}


