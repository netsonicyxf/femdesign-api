// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.Grasshopper
{
    public class VirtualBar : FEM_Design_API_Component
    {
        public VirtualBar() : base("VirtualBar", "VirtualBar", "Define a virtual bar", CategoryName.Name(), SubCategoryName.Cat7b())
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddPointParameter("Start", "Start", "", GH_ParamAccess.item);
            pManager.AddPointParameter("End", "End", "", GH_ParamAccess.item);
            pManager.AddVectorParameter("LocalY", "LocalY", "", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("StructuralElements", "StructuralElements", "", GH_ParamAccess.list);
            pManager.AddTextParameter("Identifier", "Identifier", "Identifier. Optional, default value if undefined.", GH_ParamAccess.item, "VB");
            pManager[pManager.ParamCount - 1].Optional = true;
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("VirtualBar", "VirtualBar", "", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get input
            Rhino.Geometry.Point3d start = Rhino.Geometry.Point3d.Origin;
            DA.GetData(0, ref start);

            Rhino.Geometry.Point3d end = Rhino.Geometry.Point3d.Origin;
            DA.GetData(1, ref end);

            Rhino.Geometry.Vector3d localY = Rhino.Geometry.Vector3d.Zero;
            if ( !DA.GetData(2, ref localY))
            {
                Rhino.Geometry.Vector3d localX = end - start;
                localX.Unitize();
                localY = Rhino.Geometry.Vector3d.CrossProduct(localX, Rhino.Geometry.Vector3d.ZAxis);
            }

            List<FemDesign.GenericClasses.IStructureElement> structuralElement = new List<GenericClasses.IStructureElement>();
            DA.GetDataList(3, structuralElement);

            string identifier = "VB";
            DA.GetData(4, ref identifier);

            var virtualBar = new FemDesign.AuxiliaryResults.VirtualBar(start.FromRhino(), end.FromRhino(), localY.FromRhino(), structuralElement, identifier);

            // output
            DA.SetData(0, virtualBar);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.VirtualBar;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{C345C770-2D93-4117-A156-58094D0AE185}"); }
        }
        public override GH_Exposure Exposure => GH_Exposure.primary;

    }
}