// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.Grasshopper
{
    public class BarsDeconstructOBSOLETE_FEM_Design_21_0_0 : GH_Component
    {
        public BarsDeconstructOBSOLETE_FEM_Design_21_0_0() : base("Bars.Deconstruct", "Deconstruct", "Deconstruct a bar element.", "FEM - Design", "Deconstruct")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Bar", "Bar", "Bar.", GH_ParamAccess.item);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddTextParameter("Guid", "Guid", "Guid.", GH_ParamAccess.item);
            pManager.AddCurveParameter("Curve", "Curve", "LineCurve or ArcCurve", GH_ParamAccess.item);
            pManager.AddGenericParameter("Type", "Type", "Bar type", GH_ParamAccess.item);
            pManager.AddGenericParameter("Material", "Material", "Material", GH_ParamAccess.item);
            pManager.AddGenericParameter("Section", "Section", "Section", GH_ParamAccess.list);
            pManager.AddGenericParameter("Connectivity", "Connectivity", "Connectivity", GH_ParamAccess.list);
            pManager.AddGenericParameter("Eccentricity", "Eccentricity", "Eccentricity", GH_ParamAccess.list);
            pManager.AddGenericParameter("LocalY", "LocalY", "LocalY", GH_ParamAccess.item);
            pManager.AddGenericParameter("Stirrups", "Stirrups", "Stirrups.", GH_ParamAccess.list);
            pManager.AddGenericParameter("LongitudinalBars", "LongBars", "Longitudinal bars.", GH_ParamAccess.list);
            pManager.AddGenericParameter("PTC", "PTC", "Post-tensioning cables.", GH_ParamAccess.list);
            pManager.AddTextParameter("Identifier", "Identifier", "Structural element ID.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get input
            FemDesign.Bars.Bar bar = null;
            if (!DA.GetData(0, ref bar))
            {
                return;
            }
            if (bar == null)
            {
                return;
            }

            // return
            DA.SetData(0, bar.Guid);
            DA.SetData(1, bar.ToRhino());
            DA.SetData(2, bar.BarPart.ComplexMaterialObj);
            DA.SetDataList(3, bar.BarPart.ComplexSectionObj.Sections);
            DA.SetDataList(4, bar.BarPart.Connectivity);
            DA.SetDataList(5, bar.BarPart.ComplexSectionObj.Eccentricities);
            DA.SetData(6, bar.BarPart.LocalY.ToRhino());
            DA.SetData(7, bar.Identifier);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.BarDeconstruct;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("87525a2e-598f-44ac-ad96-f2058bc37623"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.hidden;
    }
}