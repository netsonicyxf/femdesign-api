using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;

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
            evaluationUnit.Icon = FemDesign.Properties.Resources.StudRail;

            evaluationUnit.RegisterInputParam(new Param_String(), "Pattern", "Pattern", "Stud rail pattern.", GH_ParamAccess.item, new GH_String("Orthogonal"));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "Reinforcement", "Reinforcement", "Reinforcement material.", GH_ParamAccess.item);
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

            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "Determine height automatically.", GH_ParamAccess.item, new GH_Number(0.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "UseOnly2_3", "UseOnly2_3", "Use only 2/3 of the studs.", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

        }

        public override void SolveInstance(IGH_DataAccess DA, out string msg, out GH_RuntimeMessageLevel level)
        {
            msg = "";
            level = GH_RuntimeMessageLevel.Warning;

            string pattern = "";
            DA.GetData(0, ref pattern);

            var reinforcement = new FemDesign.Materials.Material();
            DA.GetData(1, ref reinforcement);

            var diameter = 16.0;
            DA.GetData(2, ref diameter);

            var numberRails = 2;
            DA.GetData(3, ref numberRails);

            var numberStudsPerMeter = 4;
            DA.GetData(4, ref numberStudsPerMeter);

            var so = 150.0;
            DA.GetData(5, ref so);

            var s1 = 200.0;
            DA.GetData(6, ref s1);

            var s2 = 300.0;
            DA.GetData(7, ref s2);

            double? height = 0.00;
            DA.GetData(8, ref height);

            var useOnly2_3 = false;
            DA.GetData(9, ref useOnly2_3);

            var studRail = new FemDesign.Reinforcement.StudRails();
            studRail.Patter = pattern;
            studRail.S0 = so;
            studRail.S1 = s1;
            studRail.S2 = s2;
            studRail.RailsOnCircle = numberRails;
            studRail.StudsOnRail = numberStudsPerMeter;
            studRail.Height = height == 0.00 ? null : height;
            studRail.UseMinimalElements = useOnly2_3;

            var generalProduct = new FemDesign.Reinforcement.GeneralProduct();
            generalProduct.Wire = new FemDesign.Reinforcement.Wire(diameter, reinforcement, Reinforcement.WireProfileType.Ribbed);

            studRail.GeneralProduct = generalProduct;


            DA.SetData(0, studRail);
        }
    }
}