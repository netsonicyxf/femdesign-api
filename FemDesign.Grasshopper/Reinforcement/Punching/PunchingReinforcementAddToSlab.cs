// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using Eto.Forms;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.Grasshopper
{
    public class PunchingReinforcementAddToSlab : FEM_Design_API_Component
    {
        public PunchingReinforcementAddToSlab() : base("PunchingReinforcement.AddToSlab", "AddToSlab", "", "FEM-Design", "Reinforcement")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Slab", "Slab", "Slab.", GH_ParamAccess.item);
            pManager.AddGenericParameter("PunchingReinforcement", "PunchingReinforcement", "PunchingReinforcement to add to slab. Item or list.", GH_ParamAccess.list);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Slab", "Slab", "Passed slab.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            
            // return
            DA.SetData(0, null);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.RebarAddToElement;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{24F1454C-423E-4549-8317-0216D51AF236}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.tertiary;
    }
}