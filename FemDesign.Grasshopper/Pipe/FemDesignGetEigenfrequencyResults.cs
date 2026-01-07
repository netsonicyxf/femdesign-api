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
    /// Read eigenfrequency results using the shared hub connection (standard GH_Component, UI-blocking).
    /// Mirrors PipeEigenFrequencyResults behavior without the async workaround.
    /// </summary>
    public class FemDesignGetEigenfrequencyResults : FEM_Design_API_Component
    {
        public FemDesignGetEigenfrequencyResults() : base("FEM-Design.GetEigenfrequencyResults", "EigenfrequencyResults", "Read eigenfrequency results from current model using shared connection. Result files (.csv) are saved into the output directory.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddIntegerParameter("ShapeId", "ShapeId", "Vibration shape identifier must be greater or equal to 1. Optional parameter. If not defined, all shapes will be listed.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Options", "Options", "Settings for output location. Default is 'ByStep' and 'Vertices'.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Units", "Units", "Specify the Result Units for some specific type.\nDefault Units are: Length.m, Angle.deg, SectionalData.m, Force.kN, Mass.kg, Displacement.m, Stress.Pa", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("VibrationShapes", "Shapes", "Vibration shape results.", GH_ParamAccess.tree);
            pManager.AddGenericParameter("Eigenfrequencies", "Eigenfrequencies", "Eigenfrequency results.", GH_ParamAccess.tree);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

            var shapeIds = new List<int>();
            DA.GetDataList("ShapeId", shapeIds);

            Options options = null;
            DA.GetData("Options", ref options);

            Results.UnitResults units = null;
            DA.GetData("Units", ref units);

            bool runNode = true;
            DA.GetData("RunNode", ref runNode);

            var log = new List<string>();
            bool success = false;

            var vibrationTree = new DataTree<FemDesign.Results.NodalVibration>();
            var frequencyTree = new DataTree<FemDesign.Results.EigenFrequencies>();

            if (!runNode)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Warning, "Run node set to false.");
                DA.SetData("Connection", null);
                DA.SetDataTree(1, vibrationTree);
                DA.SetDataTree(2, frequencyTree);
                DA.SetData("Success", false);
                DA.SetDataList("Log", log);
                return;
            }

            // check inputs
            if (handle == null)
                throw new Exception("Connection handle is null.");

            try
            {
                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
                {
                    void onOutput(string s) { log.Add(s); }
                    connection.OnOutput += onOutput;
                    try
                    {
                        // helper to invoke private generic _getResults
                        List<IResult> InvokeGetResults(Type resultType)
                        {
                            string methodName = nameof(FemDesign.FemDesignConnection._getResults);
                            MethodInfo genericMethod = connection.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(resultType);
                            var res = (IEnumerable<IResult>)genericMethod.Invoke(connection, new object[] { units, options, null, false });
                            return res.ToList();
                        }

                        var vibrationRes = InvokeGetResults(typeof(FemDesign.Results.NodalVibration)).Cast<FemDesign.Results.NodalVibration>().ToList();
                        var frequencyRes = InvokeGetResults(typeof(FemDesign.Results.EigenFrequencies)).Cast<FemDesign.Results.EigenFrequencies>().ToList();

                        if (vibrationRes.Count == 0 && frequencyRes.Count == 0)
                            throw new Exception("Eigenfrequencies results have not been found. Have you run the eigenfrequencies analysis?");

                        string vibPropName = nameof(FemDesign.Results.NodalVibration.ShapeId);
                        string freqPropName = nameof(FemDesign.Results.EigenFrequencies.ShapeId);

                        if (shapeIds.Any())
                        {
                            vibrationRes = vibrationRes.FilterResultsByShapeId(vibPropName, shapeIds);
                            frequencyRes = frequencyRes.FilterResultsByShapeId(freqPropName, shapeIds);
                        }

                        vibrationTree = vibrationRes.CreateResultTree(vibPropName);
                        frequencyTree = frequencyRes.CreateResultTree(freqPropName);
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
            DA.SetDataTree(1, vibrationTree);
            DA.SetDataTree(2, frequencyTree);
            DA.SetData("Success", success);
            DA.SetDataList("Log", log);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{23905992-55CC-473E-9825-02D565522219}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}


