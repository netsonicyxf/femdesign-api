// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Reflection;
using System.Threading;
using Grasshopper.Kernel;

using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Get quantities using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignGetQuantities : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private string _resultTypeName;
        private Results.UnitResults _units;
        private bool _runNode;

        // Output data
        private List<Results.IResult> _results;
        private List<string> _log;
        private bool _success;

        public FemDesignGetQuantities() : base("FEM-Design.GetQuantities", "GetQuantities", "Get quantities from current model using shared connection. Result files (.csv) are saved into the output directory.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("QuantityType", "QuantityType", "Quantity type:\n\n" +
                nameof(ListProc.QuantityEstimationConcrete) + "\n" +
                nameof(ListProc.QuantityEstimationReinforcement) + "\n" +
                nameof(ListProc.QuantityEstimationSteel) + "\n" +
                nameof(ListProc.QuantityEstimationTimber) + "\n" +
                nameof(ListProc.QuantityEstimationTimberPanel) + "\n" +
                nameof(ListProc.QuantityEstimationMasonry) + "\n" +
                nameof(ListProc.QuantityEstimationGeneral) + "\n" +
                nameof(ListProc.QuantityEstimationProfiledPanel), GH_ParamAccess.item);
            pManager.AddGenericParameter("Units", "Units", "Optional result units.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Quantities", "Quantities", "Quantities.", GH_ParamAccess.list);
            pManager.AddBooleanParameter("Success", "Success", "True if succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _resultTypeName = null;
            DA.GetData("QuantityType", ref _resultTypeName);

            _units = null;
            DA.GetData("Units", ref _units);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _results = new List<Results.IResult>();
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

            // Check inputs
            if (string.IsNullOrWhiteSpace(_resultTypeName))
                throw new Exception("'QuantityType' is null or empty.");

            // Try getting the quantity result type
            string typeName = $"FemDesign.Results.{_resultTypeName}, FemDesign.Core";
            Type resultType = Type.GetType(typeName);
            if (resultType == null)
                throw new ArgumentException($"QuantityType '{typeName}' does not exist!");

            FemDesignConnectionHub.InvokeAsync(_handle.Id, connection =>
            {
                void onOutput(string s) { _log.Add(s); }
                connection.OnOutput += onOutput;
                try
                {
                    cancellationToken.ThrowIfCancellationRequested();
                    var methodName = nameof(FemDesign.FemDesignConnection._getQuantities);
                    var method = connection.GetType().GetMethod(methodName, BindingFlags.Instance | BindingFlags.NonPublic).MakeGenericMethod(resultType);
                    var res = (IEnumerable<Results.IResult>)method.Invoke(connection, new object[] { _units, false });
                    _results.AddRange(res);
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
            DA.SetDataList("Quantities", _results);
            DA.SetData("Success", _success);
            DA.SetDataList("Log", _log);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetDataList("Quantities", new List<Results.IResult>());
            DA.SetData("Success", false);
            DA.SetDataList("Log", _log ?? new List<string>());
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_readresult;
        public override Guid ComponentGuid => new Guid("{4498FBC1-1EA9-4885-8658-FF79652C51CB}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}
