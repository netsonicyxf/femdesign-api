// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Threading;
using Grasshopper.Kernel;

using FemDesign.Results;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read the finite element model using the shared hub connection.
    /// Supports both sync (UI-blocking) and async (non-blocking) modes via FemDesignSettings.
    /// </summary>
    public class FemDesignGetFeaModel : FemDesignHybridComponent
    {
        // Input data
        private FemDesignHubHandle _handle;
        private Results.UnitResults _units;
        private bool _runNode;

        // Output data
        private FiniteElement _feModel;
        private bool _success;

        public FemDesignGetFeaModel() : base("FEM-Design.GetFeModel", "GetFeModel", "Read the finite element data using the shared FEM-Design connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Units", "Units", "Specify the Result Units for some specific type.\nDefault Units are: Length.m, Angle.deg, SectionalData.m, Force.kN, Mass.kg, Displacement.m, Stress.Pa", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddBooleanParameter("RunNode", "RunNode", "If true node will execute. If false node will not execute.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("FiniteElement", "FiniteElement", "FEM-Design finite element model.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
        }

        protected override void CollectInputData(IGH_DataAccess DA)
        {
            _handle = null;
            DA.GetData("Connection", ref _handle);

            _units = null;
            DA.GetData("Units", ref _units);

            _runNode = true;
            DA.GetData("RunNode", ref _runNode);

            // Reset output data
            _feModel = null;
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

            if (_units == null)
                _units = Results.UnitResults.Default();

            FemDesignConnectionHub.InvokeAsync(_handle.Id, connection =>
            {
                cancellationToken.ThrowIfCancellationRequested();
                connection.GenerateFeaModel();
                _feModel = connection.GetFeaModel(_units.Length);
            }).GetAwaiter().GetResult();

            _success = true;
        }

        protected override void SetOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", _handle);
            DA.SetData("FiniteElement", _feModel);
            DA.SetData("Success", _success);
        }

        protected override void SetDefaultOutputData(IGH_DataAccess DA)
        {
            DA.SetData("Connection", null);
            DA.SetData("FiniteElement", null);
            DA.SetData("Success", false);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_GetMesh;
        public override Guid ComponentGuid => new Guid("{49306D49-2DB5-449D-B6BA-CDE870DD204D}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}
