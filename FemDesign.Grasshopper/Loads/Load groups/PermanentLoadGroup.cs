using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Rhino.Geometry;
using FemDesign.Loads;
using FemDesign.Grasshopper.Extension.ComponentExtension;
using Grasshopper.Kernel.Special;
using FemDesign.GenericClasses;
using FemDesign.Calculate;

namespace FemDesign.Grasshopper
{
    public class PermanentLoadGroup : SubComponent
    {
        public override string name() => "PermanentLoadGroup";
        public override string display_name() => "PermanentLoadGroup";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "PermanentLoadGroup");
            evaluationUnit.Icon = FemDesign.Properties.Resources.LoadGroup;
            mngr.RegisterUnit(evaluationUnit);

            evaluationUnit.RegisterInputParam(new Param_Number(), "Favourable", "Favourable", "", GH_ParamAccess.item, new GH_Number(1));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Unfavourable", "Unfavourable", "", GH_ParamAccess.item, new GH_Number(1.35));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Epsilon", "Epsilon", "", GH_ParamAccess.item, new GH_Number(0.93));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Favourable", "Favourable", "", GH_ParamAccess.item, new GH_Number(1.00));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Unfavourable", "Unfavourable", "", GH_ParamAccess.item, new GH_Number(1.00));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Standard combinations";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            evaluationUnit.AddMenu(gH_ExtendableMenu0);

            GH_ExtendableMenu gH_ExtendableMenu1 = new GH_ExtendableMenu(1, "");
            gH_ExtendableMenu1.Name = "Accidental combinations";
            gH_ExtendableMenu1.Expand();
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[3]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[4]);
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

            double standardFavourable = 1.0;
            DA.GetData(4, ref standardFavourable);

            double standardUnfavourable = 1.35;
            DA.GetData(5, ref standardUnfavourable);

            double epsilon = 0.93;
            DA.GetData(6, ref epsilon);

            double accidentalFavourable = 1.0;
            DA.GetData(7, ref accidentalFavourable);

            double accidentalUnfavourable = 1.0;
            DA.GetData(8, ref accidentalUnfavourable);



            var loadGroupPermanent = new FemDesign.Loads.LoadGroupPermanent(standardFavourable, standardUnfavourable, accidentalFavourable, accidentalUnfavourable, loadCases, relationship, epsilon, name);


            var ldGroup = new FemDesign.Loads.ModelGeneralLoadGroup();

            ldGroup.ModelLoadGroupPermanent = loadGroupPermanent;
            ldGroup.ConsiderInGmax = considerMaxLoadGroup;
            ldGroup.Name = name;

            DA.SetData(0, ldGroup);
        }
    }
}