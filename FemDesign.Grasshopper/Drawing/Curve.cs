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
    public class DrawingCurve : GH_SwitcherComponent
    {

        private enum CurveStyleType
        {
            CENTER2,
            CONTINOUS,
            DASH12,
            DASH2,
            DASH4,
            DASH8,
        }

        public DrawingCurve() : base("Curve", "Curve", "", CategoryName.Name(), "ModellingTools")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddPointParameter("StartPoint", "StartPoint", "Start point of curve.", GH_ParamAccess.item);
            pManager.AddPointParameter("EndPoint", "EndPoint", "End point of curve.", GH_ParamAccess.item);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Curve", "Curve", "Curve.", GH_ParamAccess.item);
        }

        protected override void RegisterEvaluationUnits(EvaluationUnitManager mngr)
        {

            EvaluationUnit evaluationUnit = new EvaluationUnit("ExtendableComponent", "ExtComp", "A Test Component");
            mngr.RegisterUnit(evaluationUnit);


            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "Layer", "Layer", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Colour(), "Colour", "Colour", "", GH_ParamAccess.item, new GH_Colour(System.Drawing.Color.Black));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_String(), "LineStyle", "LineStyle", "", GH_ParamAccess.item, new GH_String("CONTINUOUS"));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(CurveStyleType)).ToList();


            evaluationUnit.RegisterInputParam(new Param_Number(), "Penwidth", "Penwidth", "[mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;



            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "Style");
            gH_ExtendableMenu0.Name = "Style";
            gH_ExtendableMenu0.Expand();
            evaluationUnit.AddMenu(gH_ExtendableMenu0);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
        }

        protected override void SolveInstance(IGH_DataAccess DA, EvaluationUnit unit)
        {
            Point3d start = new Point3d();
            DA.GetData(0, ref start);

            Point3d end = new Point3d();
            DA.GetData(1, ref end);

            StruSoft.Interop.StruXml.Data.Layer_type layer = new StruSoft.Interop.StruXml.Data.Layer_type();
            DA.GetData(2, ref layer);

            System.Drawing.Color colour = System.Drawing.Color.FromArgb(200, 232, 0);
            DA.GetData(3, ref colour);

            string lineStyle = "CONTINUOUS";
            DA.GetData(4, ref lineStyle);

            double penWidth = 0.0;
            DA.GetData(5, ref penWidth);

            // Create curve
            var style = new StruSoft.Interop.StruXml.Data.Style_type();
            style.Penwidth = penWidth/1000;
            style.Colour = ColorTranslator.ToHtml((System.Drawing.Color)colour).Substring(1);
            style.Layer = layer.Name;
            style.Line_style = lineStyle;

            var curve = new FemDesign.Drawing.Curve(start.FromRhino(), end.FromRhino(), layer, style);

            DA.SetData(0, curve);

        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {

                return Resources.CurveDrawing;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{5C2ACE20-C0C0-47A7-886F-BF7B404BBC20}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.last;

    }
}