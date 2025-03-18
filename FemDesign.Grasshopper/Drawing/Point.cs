// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Special;
using Rhino.Geometry;
using FemDesign.Loads;

using FemDesign.Grasshopper.Extension.ComponentExtension;
using System.Linq;
using FemDesign.Grasshopper.Components.UIWidgets;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Properties;
using System.Drawing;

namespace FemDesign.Grasshopper
{
    public class Point : GH_SwitcherComponent
    {
        public Point() : base("Point", "Point", "", CategoryName.Name(), "ModellingTools")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddPointParameter("Point", "Point", "", GH_ParamAccess.item);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Point", "Point", "Point.", GH_ParamAccess.item);
        }

        protected override void RegisterEvaluationUnits(EvaluationUnitManager mngr)
        {

            EvaluationUnit evaluationUnit = new EvaluationUnit("ExtendableComponent", "ExtComp", "A Test Component");
            mngr.RegisterUnit(evaluationUnit);


            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "Layer", "Layer", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Colour(), "Colour", "Colour", "", GH_ParamAccess.item, new GH_Colour(System.Drawing.Color.FromArgb(0, 0, 0)));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_String(), "PointStyle", "PointStyle", "", GH_ParamAccess.item, new GH_String("cross"));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(StruSoft.Interop.StruXml.Data.Pointstyle_type)).ToList();



            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "Style");
            gH_ExtendableMenu0.Name = "Style";
            gH_ExtendableMenu0.Expand();
            evaluationUnit.AddMenu(gH_ExtendableMenu0);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
        }

        protected override void SolveInstance(IGH_DataAccess DA, EvaluationUnit unit)
        {
            Point3d start = new Point3d();
            DA.GetData(0, ref start);

            StruSoft.Interop.StruXml.Data.Layer_type layer = new StruSoft.Interop.StruXml.Data.Layer_type();
            DA.GetData(1, ref layer);

            System.Drawing.Color colour = System.Drawing.Color.FromArgb(0, 0, 0);
            DA.GetData(2, ref colour);

            string _pointStyle = "cross";
            DA.GetData(3, ref _pointStyle);

            var pointStyle = (StruSoft.Interop.StruXml.Data.Pointstyle_type)Enum.Parse(typeof(StruSoft.Interop.StruXml.Data.Pointstyle_type), _pointStyle, true);

            var style = new StruSoft.Interop.StruXml.Data.Style_type();
            style.Colour = ColorTranslator.ToHtml((System.Drawing.Color)colour).Substring(1);
            style.Layer = layer.Name;
            style.Point_style = pointStyle;

            // Create curve
            var point = new FemDesign.Drawing.Point3d(start.X, start.Y, start.Z, layer, style);

            DA.SetData(0, point);

        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {

                return Resources.PointDrawing;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{7E7272C4-83C2-4A7B-8597-9B0846A39DC1}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.last;

    }
}