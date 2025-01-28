using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;
using System;
using System.Collections.Generic;
using System.Linq;
using Grasshopper.GUI.Script;

namespace FemDesign.Grasshopper
{
    public class TemporaryLoadGroup : SubComponent
    {
        public override string name() => "TemporaryLoadGroup";
        public override string display_name() => "TemporaryLoadGroup";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "TemporaryLoadGroup");
            evaluationUnit.Icon = FemDesign.Properties.Resources.LoadGroup;
            mngr.RegisterUnit(evaluationUnit);

            evaluationUnit.RegisterInputParam(new Param_Number(), "SafetyFactor", "SafetyFactor", "", GH_ParamAccess.item, new GH_Number(1.50));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Psi0", "Psi0", "", GH_ParamAccess.item, new GH_Number(0.70));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Psi1", "Psi1", "", GH_ParamAccess.item, new GH_Number(0.50));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Psi2", "Psi2", "", GH_ParamAccess.item, new GH_Number(0.30));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;


            evaluationUnit.RegisterInputParam(new Param_Boolean(), "LeadingLoadCases", "LeadingLoadCases", "", GH_ParamAccess.item, new GH_Boolean(true));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "IgnoreSLS", "IgnoreSLS", "", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;


            evaluationUnit.RegisterInputParam(new Param_String(), "TemporaryEffect", "TemporaryEffect", "\nGeneral\nWind\nSnow", GH_ParamAccess.item, new GH_String("General"));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(Loads.TemporaryEffect)).ToList();



            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Factors";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
            evaluationUnit.AddMenu(gH_ExtendableMenu0);


            GH_ExtendableMenu gH_ExtendableMenu1 = new GH_ExtendableMenu(1, "");
            gH_ExtendableMenu1.Name = "Options";
            gH_ExtendableMenu1.Expand();
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[4]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[5]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[6]);
            evaluationUnit.AddMenu(gH_ExtendableMenu1);
        }

        public override void SolveInstance(IGH_DataAccess DA, out string msg, out GH_RuntimeMessageLevel level)
        {
            msg = "";
            level = GH_RuntimeMessageLevel.Warning;

            string name = "";
            DA.GetData(0, ref name);

            string _relationship = "alternative";
            DA.GetData(1, ref _relationship);

            var relationship = FemDesign.GenericClasses.EnumParser.Parse<Loads.ELoadGroupRelationship>(_relationship);

            var loadCases = new List<Loads.LoadCase>();
            DA.GetDataList(2, loadCases);

            bool considerMaxLoadGroup = true;
            DA.GetData(3, ref considerMaxLoadGroup);

            double safetyFactor = 1.0;
            DA.GetData(4, ref safetyFactor);

            double psi0 = 0.7;
            DA.GetData(5, ref psi0);

            double psi1 = 0.5;
            DA.GetData(6, ref psi1);

            double psi2 = 0.3;
            DA.GetData(7, ref psi2);

            bool leading = true;
            DA.GetData(8, ref leading);

            bool ignore = true;
            DA.GetData(9, ref ignore);

            string _temporaryEffect = "General";
            DA.GetData(10, ref _temporaryEffect);

            var temporaryEffect = FemDesign.GenericClasses.EnumParser.Parse<Loads.TemporaryEffect>(_temporaryEffect);

            var tempLoadGroup = new Loads.LoadGroupTemporary(safetyFactor, psi0, psi1, psi2, leading, loadCases, relationship, name);

            tempLoadGroup.IgnoreSls = ignore;
            tempLoadGroup.TemporaryEffect = temporaryEffect;

            var ldGroup = new Loads.ModelGeneralLoadGroup();

            ldGroup.ModelLoadGroupTemporary = tempLoadGroup;
            ldGroup.ConsiderInGmax = considerMaxLoadGroup;
            ldGroup.Name = name;


            DA.SetData(0, ldGroup);
        }

    }
}