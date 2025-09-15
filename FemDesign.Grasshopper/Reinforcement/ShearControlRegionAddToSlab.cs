// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using Eto.Forms;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.Grasshopper
{
    public class ShearControlRegionAddToSlab : FEM_Design_API_Component
    {
        public ShearControlRegionAddToSlab() : base("ShearControlRegion.AddToSlab", "AddToSlab", "", "FEM-Design", "Reinforcement")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Slab", "Slab", "Slab.", GH_ParamAccess.item);
            pManager.AddGenericParameter("ShearControlRegion", "ShearControlRegion", "ShearControlRegion to add to slab. Item or list.", GH_ParamAccess.list);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Slab", "Slab", "Passed slab.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get data
            FemDesign.Shells.Slab slab = null;
            if (!DA.GetData(0, ref slab))
            {
                return;
            }

            List<FemDesign.Reinforcement.ShearControlRegionType> shearControlRegion = new List<FemDesign.Reinforcement.ShearControlRegionType>();
            if (!DA.GetDataList(1, shearControlRegion))
            {
                return;
            }



            FemDesign.Shells.Slab obj = FemDesign.Reinforcement.SurfaceReinforcement.AddShearControlRegionToSlab(slab, shearControlRegion);

            // return
            DA.SetData(0, obj);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.RebarAddToElement;
                ;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{B8CCC7F2-0EA5-4912-AA99-2C9E7AC0B9CD}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}