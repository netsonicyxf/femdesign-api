using FemDesign.Grasshopper.Components.UIWidgets;
using FemDesign.Loads;
using GH_IO.Types;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using System;
using System.Linq;

namespace FemDesign.Grasshopper
{
    public class StudRail : SubComponent
    {
        public override string name() => "StudRail";
        public override string display_name() => "StudRail";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "");
            mngr.RegisterUnit(evaluationUnit);
            //evaluationUnit.Icon = FemDesign.Properties.Resources.StudRail;

            evaluationUnit.RegisterInputParam(new Param_Plane(), "Point|Plane", "Point|Plane", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Brep(), "Region", "Region", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_String(), "Pattern", "Pattern", "Stud rail pattern.", GH_ParamAccess.item, new GH_String("Orthogonal"));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(FemDesign.Reinforcement.Pattern)).ToList();

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "ReinforcingMaterial", "ReinforcingMaterial", "Reinforcement material.", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Diameter", "Diameter of studs [mm].", GH_ParamAccess.item, new GH_Number(16.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "NumberRails", "NumberRails", "Number of rails.", GH_ParamAccess.item, new GH_Integer(2));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "NumberStudsPerMeter", "NumberStudsPerMeter", "Number of studs per meter.", GH_ParamAccess.item, new GH_Integer(4));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "So", "So", "Spacing So [mm].", GH_ParamAccess.item, new GH_Number(150.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "S1", "S1", "Spacing S1 [mm].", GH_ParamAccess.item, new GH_Number(200.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "S2", "S2", "Spacing S2 [mm].", GH_ParamAccess.item, new GH_Number(300.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "NOT YET IMPLEMENTED. Contact us if interested!", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "UseOnly2_3", "UseOnly2_3", "Use only 2/3 of the studs.", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Stud";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[4]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[5]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[6]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[7]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[8]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[9]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[10]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[11]);
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

            string pattern = "";
            DA.GetData(2, ref pattern);

            var _pattern = FemDesign.GenericClasses.EnumParser.Parse<FemDesign.Reinforcement.Pattern>(pattern);

            var reinforcement = new FemDesign.Materials.Material();
            DA.GetData(3, ref reinforcement);

            var diameter = 16.0;
            DA.GetData(4, ref diameter);
            diameter /= 1000; // mm to m

            var numberRails = 2;
            DA.GetData(5, ref numberRails);

            var numberStudsPerMeter = 4;
            DA.GetData(6, ref numberStudsPerMeter);

            var so = 150.0;
            DA.GetData(7, ref so);
            so = so/1000; // mm to m

            var s1 = 200.0;
            DA.GetData(8, ref s1);
            s1 = s1/1000; // mm to m

            var s2 = 300.0;
            DA.GetData(9, ref s2);
            s2 = s2/1000; // mm to m

            double? height = 0.00;
            DA.GetData(10, ref height);
            height = height == 0.00 ? null : height/1000;

            var useOnly2_3 = false;
            DA.GetData(11, ref useOnly2_3);

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


            var studRail = new FemDesign.Reinforcement.StudRails();
            {
                studRail.Pattern = _pattern;
                studRail.S0 = so;
                studRail.S1 = s1;
                studRail.S2 = s2;
                studRail.RailsOnCircle = numberRails;
                studRail.StudsOnRail = numberStudsPerMeter;
                //studRail.Height = height == 0.00 ? null : height/1000;
                studRail.UseMinimalElements = useOnly2_3;

                var generalProduct = new FemDesign.Reinforcement.GeneralProduct();
                generalProduct.Wire = new FemDesign.Reinforcement.Wire(diameter, reinforcement, Reinforcement.WireProfileType.Ribbed);

                studRail.GeneralProduct = generalProduct;
            }

            punchingReinforcement.StudRails = studRail;

            DA.SetData(0, punchingReinforcement);
        }
    }
}