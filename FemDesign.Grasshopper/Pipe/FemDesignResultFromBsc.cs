// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Data;
using Grasshopper;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Extract results from a model using a .bsc file with the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignResultFromBsc : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private List<string> _bscPaths;
        private List<string> _csvPaths;
        private List<FemDesign.GenericClasses.IStructureElement> _elements;
        private bool _runNode;

        // Output data
        private DataTree<object> _resultsTree;
        private List<string> _log;
        private bool _success;

        public FemDesignResultFromBsc() : base("FEM-Design.GetResultFromBsc", "ResultFromBsc", "Extract results using a .bsc file with shared connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("BscFilePath", "BscFilePath", "File path(s) to .bsc batch-file(s).", GH_ParamAccess.list);
            pManager.AddTextParameter("CsvFilePath", "CsvFilePath", "Optional output .csv path(s). If not set, results are saved next to the .bsc file(s).", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Elements", "Elements", "Optional elements filter.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddTextParameter("Results", "Results", "Results as data tree (CSV paths).", GH_ParamAccess.tree);
            pManager.AddBooleanParameter("Success", "Success", "True if succeeded.", GH_ParamAccess.item);
            pManager.AddTextParameter("Log", "Log", "Operation log.", GH_ParamAccess.list);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _bscPaths = new List<string>();
            DA.GetDataList("BscFilePath", _bscPaths);

            _csvPaths = new List<string>();
            DA.GetDataList("CsvFilePath", _csvPaths);

            _elements = new List<FemDesign.GenericClasses.IStructureElement>();
            DA.GetDataList("Elements", _elements);

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

                    if (_csvPaths == null || _csvPaths.Count == 0)
                    {
                        _csvPaths = _bscPaths.Select(b => System.IO.Path.ChangeExtension(b, "csv")).ToList();
                    }

                    var results = _bscPaths.Zip(_csvPaths, (bsc, csv) => connection.GetResultsFromBsc(bsc, csv, _elements));
                    int i = 0;
                    foreach (var r in results)
                    {
                        _resultsTree.AddRange(r, new GH_Path(i));
                        i++;
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
        public override Guid ComponentGuid => new Guid("{59667BED-D84B-47E7-BC56-B6D99DC5C274}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}
