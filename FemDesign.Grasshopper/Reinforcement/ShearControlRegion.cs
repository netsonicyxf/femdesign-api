// https://strusoft.com/
using FemDesign.GenericClasses;
using FemDesign.Grasshopper.Extension.ComponentExtension;
using FemDesign.Reinforcement;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Special;
using Rhino.Geometry;
using System;
using System.Linq;

namespace FemDesign.Grasshopper
{
    public class ShearControlRegion : FEM_Design_API_Component
    {
        public ShearControlRegion() : base("ShearControlRegion", "ShearControlRegion", "", "FEM-Design", "Reinforcement")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddSurfaceParameter("Surface", "Surface", "", GH_ParamAccess.item);
            pManager.AddBooleanParameter("IgnoreShearCheck", "IgnoreShearCheck", "", GH_ParamAccess.item);
            pManager.AddBooleanParameter("ReduceShearForces", "reduce_shear_forces", "", GH_ParamAccess.item);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("ShearControlRegion", "ShearControlRegion", "", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get data
            Rhino.Geometry.Brep brep = null;
            bool ignoreShearCheck = false;
            bool reduceShearForces = false;

            DA.GetData(0, ref brep);
            DA.GetData(1, ref ignoreShearCheck);
            DA.GetData(2, ref reduceShearForces);

            FemDesign.Reinforcement.ShearControlRegionType obj = new FemDesign.Reinforcement.ShearControlRegionType(brep.FromRhino(), ignoreShearCheck, reduceShearForces );

            // return
            DA.SetData(0, obj);
        }

        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.shearRegion;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{6FC91887-9C17-416E-A0C4-C1BEC2139FAE}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}