using FemDesign.Grasshopper.Components.UIWidgets;
using FemDesign.Reinforcement;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using System;

namespace FemDesign.Grasshopper
{
    public class BendedBar : SubComponent
    {
        public override string name() => "BendedBar";
        public override string display_name() => "BendedBar";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "");
            mngr.RegisterUnit(evaluationUnit);
            evaluationUnit.Icon = FemDesign.Properties.Resources.BendedBar;


            evaluationUnit.RegisterInputParam(new Param_Plane(), "Point|Plane", "Point|Plane", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Brep(), "Region", "Region", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Point(), "LocalCenter", "LocalCenter", "Local center point of the bended bar.", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "ReinforcingMaterial", "ReinforcingMaterial", "Reinforcing material.", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Dia", "Diameter of the bended bar. [mm]", GH_ParamAccess.item, new GH_Number(10.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "TipSectionsLength", "TipLen", "Length of the tip sections. [mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "MiddleSectionsLength", "MidLen", "Length of the middle sections. [mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "Height of the bended bar. [mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Angle", "Angle", "Bend angle. [degrees]", GH_ParamAccess.item, new GH_Number(90.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_String(), "Direction", "Dir", "Direction of the bended bar local x-axis. Options: X, Y.", GH_ParamAccess.item, new GH_String("X"));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Bended";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[4]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[5]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[6]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[7]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[8]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[9]);
            evaluationUnit.AddMenu(gH_ExtendableMenu0);

        }

        public override void SolveInstance(IGH_DataAccess DA, out string msg, out GH_RuntimeMessageLevel level)
        {
            msg = "";
            level = GH_RuntimeMessageLevel.Warning;

            var plane = Rhino.Geometry.Plane.WorldXY;
            DA.GetData(0, ref plane);

            Rhino.Geometry.Brep region = null;
            DA.GetData(1, ref region);

            Rhino.Geometry.Point3d LocalCenter = new Rhino.Geometry.Point3d(0, 0, 0);
            DA.GetData(2, ref LocalCenter);

            var reinforcingMaterial = new FemDesign.Materials.Material();
            DA.GetData(3, ref reinforcingMaterial);

            var diameter = 10.0;
            DA.GetData(4, ref diameter);
            diameter = diameter / 1000.0; // mm to m

            var tipSectionsLength = 0.0;
            DA.GetData(5, ref tipSectionsLength);
            tipSectionsLength = tipSectionsLength / 1000.0; // mm to m

            var middleSectionsLength = 0.0;
            DA.GetData(6, ref middleSectionsLength);
            middleSectionsLength = middleSectionsLength / 1000.0; // mm to m

            var height = 0.0;
            DA.GetData(7, ref height);
            height = height / 1000.0; // mm to m

            var angle = 90.0;
            DA.GetData(8, ref angle);

            angle = angle * Math.PI / 180.0;

            if (angle < 0 || angle > Math.PI / 2)
            {
                msg = "Angle must be between 0 and 90 degrees.";
                level = GH_RuntimeMessageLevel.Error;
                return;
            }

            var direction = "X";
            DA.GetData(9, ref direction);

            var _direction = FemDesign.GenericClasses.EnumParser.Parse<FemDesign.Reinforcement.Direction>(direction);


            var punchingReinforcement = new FemDesign.Reinforcement.PunchingReinforcement();
            {
                // punching area
                var punchingArea = new FemDesign.Reinforcement.PunchingArea();
                punchingArea.LocalPos = plane.Origin.FromRhino();
                punchingArea.LocalX = plane.XAxis.FromRhino();
                punchingArea.LocalY = plane.YAxis.FromRhino();
                punchingArea.Region = region.FromRhino();

                punchingReinforcement.PunchingArea = punchingArea;
            }

            var bendedBar = new FemDesign.Reinforcement.BendedBar();
            {
                bendedBar.LocalCenter = LocalCenter.FromRhino();
                bendedBar.Wire = new FemDesign.Reinforcement.Wire(diameter, reinforcingMaterial, Reinforcement.WireProfileType.Ribbed);
                bendedBar.Angle = angle;
                bendedBar.Height = height;
                bendedBar.MiddleSectionsLength = middleSectionsLength;
                bendedBar.TipSectionsLength = tipSectionsLength;
                bendedBar.Direction = direction;
            }

            punchingReinforcement.BendedBar = bendedBar;





            DA.SetData(0, punchingReinforcement);
        }
    }
}