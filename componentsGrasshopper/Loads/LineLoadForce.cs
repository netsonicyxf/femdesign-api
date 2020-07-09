// https://strusoft.com/
using System;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.GH
{
    public class LineLoadForce: GH_Component
    {
        public LineLoadForce(): base("LineLoad.Force", "Force", "Creates a force line load.", "FemDesign", "Loads")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddCurveParameter("Curve", "Curve", "Curve defining the line load.", GH_ParamAccess.item);
            pManager.AddVectorParameter("StartForce", "StartForce", "StartForce.", GH_ParamAccess.item);
            pManager.AddVectorParameter("EndForce", "EndForce", "EndForce. Optional. If undefined LineLoad will be uniform with a force of StartForce.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("LoadCase", "LoadCase", "LoadCase.", GH_ParamAccess.item);
            pManager.AddBooleanParameter("ConstLoadDir", "ConstLoadDir", "Constant load direction? If true direction of load will be constant along action line. If false direction of load will vary along action line - characteristic direction is in the middle point of line. Optional.", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddTextParameter("Comment", "Comment", "Comment.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("LineLoad", "LineLoad", "LineLoad.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get data
            Curve curve = null;
            if (!DA.GetData(0, ref curve)) { return; }

            Vector3d startForce = Vector3d.Zero;
            if (!DA.GetData(1, ref startForce)) { return; }

            Vector3d endForce = Vector3d.Zero;
            if (!DA.GetData(2, ref endForce))
            {
                // if no data set endForce to startForce to create a uniform line load.
                endForce = startForce;
            }

            FemDesign.Loads.LoadCase loadCase = null;
            if (!DA.GetData(3, ref loadCase)) { return; }

            bool constLoadDir = true;
            if (!DA.GetData(4, ref constLoadDir)) 
            {
                // pass
            }
            
            string comment = null;
            if (!DA.GetData(5, ref comment))
            {
                // pass
            }

            if (curve == null || startForce == null || endForce == null || loadCase == null) { return; }

            //
            FemDesign.Geometry.Edge edge = FemDesign.Geometry.Edge.FromRhinoLineOrArc1(curve);
            FemDesign.Geometry.FdVector3d _startForce = FemDesign.Geometry.FdVector3d.FromRhino(startForce);
            FemDesign.Geometry.FdVector3d _endForce = FemDesign.Geometry.FdVector3d.FromRhino(endForce);
            FemDesign.Loads.GenericLoadObject obj = new FemDesign.Loads.GenericLoadObject();
            obj.lineLoad = new FemDesign.Loads.LineLoad(edge, _startForce, _endForce, loadCase, comment, constLoadDir, false, "force");

            // return
            DA.SetData(0, obj);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.LineLoadForce;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("5ef58ff2-2480-4df9-923a-ecad75abf2b2"); }
        }
    }
}