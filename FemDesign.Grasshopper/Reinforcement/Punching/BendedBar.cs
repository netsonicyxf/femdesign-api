using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;
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


            evaluationUnit.RegisterInputParam(new Param_Point(), "LocalCenter", "LocalCenter", "Local center point of the bended bar.", GH_ParamAccess.item);
            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "ReinforcingMaterial", "ReinforcingMaterial", "Reinforcing material.", GH_ParamAccess.item);
            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Dia", "Diameter of the bended bar. [mm]", GH_ParamAccess.item, new GH_Number(10.0));
            evaluationUnit.RegisterInputParam(new Param_Number(), "TipSectionsLength", "TipLen", "Length of the tip sections. [mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.RegisterInputParam(new Param_Number(), "MiddleSectionsLength", "MidLen", "Length of the middle sections. [mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "Height of the bended bar. [mm]", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.RegisterInputParam(new Param_Number(), "Angle", "Angle", "Bend angle. [degrees]", GH_ParamAccess.item, new GH_Number(90.0));
            evaluationUnit.RegisterInputParam(new Param_String(), "Direction", "Dir", "Direction of the bended bar local x-axis. Options: X, Y.", GH_ParamAccess.item, new GH_String("X"));


        }

        public override void SolveInstance(IGH_DataAccess DA, out string msg, out GH_RuntimeMessageLevel level)
        {
            msg = "";
            level = GH_RuntimeMessageLevel.Warning;

            Rhino.Geometry.Point3d LocalCenter = new Rhino.Geometry.Point3d(0, 0, 0);
            DA.GetData(0, ref LocalCenter);

            var reinforcingMaterial = new FemDesign.Materials.Material();
            DA.GetData(1, ref reinforcingMaterial);

            var diameter = 10.0;
            DA.GetData(2, ref diameter);

            var tipSectionsLength = 0.0;
            DA.GetData(3, ref tipSectionsLength);

            var middleSectionsLength = 0.0;
            DA.GetData(4, ref middleSectionsLength);

            var height = 0.0;
            DA.GetData(5, ref height);

            var angle = 90.0;
            DA.GetData(6, ref angle);

            angle = angle * Math.PI / 180.0;

            if (angle < 0 || angle > Math.PI / 2)
            {
                msg = "Angle must be between 0 and 90 degrees.";
                level = GH_RuntimeMessageLevel.Error;
                return;
            }


            var direction = "X";
            DA.GetData(7, ref direction);

            var bendedBar = new FemDesign.Reinforcement.BendedBar();

            bendedBar.LocalCenter = LocalCenter.FromRhino();
            bendedBar.Wire = new FemDesign.Reinforcement.Wire(diameter, reinforcingMaterial, Reinforcement.WireProfileType.Ribbed);
            bendedBar.Angle = angle;
            bendedBar.Height = height;
            bendedBar.MiddleSectionsLength = middleSectionsLength;
            bendedBar.TipSectionsLength = tipSectionsLength;
            bendedBar.Direction = direction;




            DA.SetData(0, bendedBar);
        }
    }
}