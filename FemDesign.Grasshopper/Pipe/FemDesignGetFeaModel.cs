// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;

using FemDesign.Results;

namespace FemDesign.Grasshopper
{
    /// <summary>
    /// Read the finite element model using the shared hub connection (standard GH_Component, UI-blocking).
    /// Mirrors PipeGetFeaModel behavior without the async workaround.
    /// </summary>
    public class FemDesignGetFeaModel : FEM_Design_API_Component
    {
        public FemDesignGetFeaModel() : base("FEM-Design.GetFeModel", "GetFeModel", "Read the finite element data using the shared FEM-Design connection.", CategoryName.Name(), SubCategoryName.Cat8())
        {
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("Units", "Units", "Specify the Result Units for some specific type.\nDefault Units are: Length.m, Angle.deg, SectionalData.m, Force.kN, Mass.kg, Displacement.m, Stress.Pa", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Connection", "Connection", "Shared FEM-Design connection handle.", GH_ParamAccess.item);
            pManager.AddGenericParameter("FiniteElement", "FiniteElement", "FEM-Design finite element model.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("Success", "Success", "True if operation succeeded.", GH_ParamAccess.item);
        }

        protected override void SolveInstance(IGH_DataAccess DA)
        {
            FemDesignHubHandle handle = null;
            DA.GetData("Connection", ref handle);

            Results.UnitResults units = null;
            DA.GetData("Units", ref units);

            bool success = false;
            FiniteElement feModel = null;

            try
            {
                if (handle == null)
                    throw new Exception("Connection handle is null.");

                if (units == null)
                    units = Results.UnitResults.Default();

                FemDesignConnectionHub.InvokeAsync(handle.Id, connection =>
                {
                    connection.GenerateFeaModel();
                    feModel = connection.GetFeaModel(units.Length);
                }).GetAwaiter().GetResult();

                success = true;
            }
            catch (Exception ex)
            {
                this.AddRuntimeMessage(GH_RuntimeMessageLevel.Error, ex.Message);
                success = false;
            }

            DA.SetData("Connection", handle);
            DA.SetData("FiniteElement", feModel);
            DA.SetData("Success", success);
        }

        protected override System.Drawing.Bitmap Icon => FemDesign.Properties.Resources.FEM_GetMesh;
        public override Guid ComponentGuid => new Guid("{49306D49-2DB5-449D-B6BA-CDE870DD204D}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}


