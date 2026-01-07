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
using FemDesign.Results;
using FemDesign.Results.Utils;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read eigenfrequency results using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignGetEigenfrequencyResults : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private List<int> _shapeIds;
        private Options _options;
        private Results.UnitResults _units;
        private bool _runNode;

        // Output data
        private DataTree<FemDesign.Results.NodalVibration> _vibrationTree;
        private DataTree<FemDesign.Results.EigenFrequencies> _frequencyTree;
        private List<string> _log;
        private bool _success;

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

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _shapeIds = new List<int>();
            DA.GetDataList("ShapeId", _shapeIds);

            _options = null;
            DA.GetData("Options", ref _options);

            _units = null;
            DA.GetData("Units", ref _units);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _vibrationTree = new DataTree<FemDesign.Results.NodalVibration>();
            _frequencyTree = new DataTree<FemDesign.Results.EigenFrequencies>();
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

                    // Helper to invoke private generic _getResults
                    List<IResult> InvokeGetResults(Type resultType)
                    {
                        string methodName = nameof(FemDesign.FemDesignConnection._getResults);
                        MethodInfo genericMethod = connection.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(resultType);
                        var res = (IEnumerable<IResult>)genericMethod.Invoke(connection, new object[] { _units, _options, null, false });
                        return res.ToList();
                    }

                    var vibrationRes = InvokeGetResults(typeof(FemDesign.Results.NodalVibration)).Cast<FemDesign.Results.NodalVibration>().ToList();
                    var frequencyRes = InvokeGetResults(typeof(FemDesign.Results.EigenFrequencies)).Cast<FemDesign.Results.EigenFrequencies>().ToList();

                    if (vibrationRes.Count == 0 && frequencyRes.Count == 0)
                        throw new Exception("Eigenfrequencies results have not been found. Have you run the eigenfrequencies analysis?");

                    string vibPropName = nameof(FemDesign.Results.NodalVibration.ShapeId);
                    string freqPropName = nameof(FemDesign.Results.EigenFrequencies.ShapeId);

                    if (_shapeIds.Any())
                    {
                        vibrationRes = vibrationRes.FilterResultsByShapeId(vibPropName, _shapeIds);
                        frequencyRes = frequencyRes.FilterResultsByShapeId(freqPropName, _shapeIds);
                    }

                    _vibrationTree = vibrationRes.CreateResultTree(vibPropName);
                    _frequencyTree = frequencyRes.CreateResultTree(freqPropName);
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
            DA.SetDataTree(1, _vibrationTree);
            DA.SetDataTree(2, _frequencyTree);
            DA.SetData("Success", _success);
            DA.SetDataList("Log", _log);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetDataTree(1, new DataTree<FemDesign.Results.NodalVibration>());
            DA.SetDataTree(2, new DataTree<FemDesign.Results.EigenFrequencies>());
            DA.SetData("Success", false);
            DA.SetDataList("Log", _log ?? new List<string>());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{23905992-55CC-473E-9825-02D565522219}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}
