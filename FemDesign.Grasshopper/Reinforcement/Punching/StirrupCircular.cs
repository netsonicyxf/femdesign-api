using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;


namespace FemDesign.Grasshopper
{
    public class StirrupCircular : SubComponent
    {
        public override string name() => "StirrupCircular";
        public override string display_name() => "StirrupCircular";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "");
            mngr.RegisterUnit(evaluationUnit);
            evaluationUnit.Icon = FemDesign.Properties.Resources.StirrupCircular;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "Quality", "Quality", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;


            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Diameter", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Width", "Width", ".", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "MaxDistance", "MaxDistance", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "Quality", "Quality", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Diameter", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Overlap", "Overlap", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;


            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Stirrup";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[4]);
            evaluationUnit.AddMenu(gH_ExtendableMenu0);


            GH_ExtendableMenu gH_ExtendableMenu1 = new GH_ExtendableMenu(1, "");
            gH_ExtendableMenu1.Name = "Auxiliary";
            gH_ExtendableMenu1.Expand();
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[5]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[6]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[7]);
            //gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[8]);
            evaluationUnit.AddMenu(gH_ExtendableMenu1);
        }

        public override void SolveInstance(IGH_DataAccess DA, out string msg, out GH_RuntimeMessageLevel level)
        {
            msg = "";
            level = GH_RuntimeMessageLevel.Warning;

            FemDesign.Materials.Material stirrupQuality = null;
            DA.GetData(0, ref stirrupQuality);

            double stirrupDiameter = 0.01;
            DA.GetData(1, ref stirrupDiameter);

            double stirrupWidth = 0.2;
            DA.GetData(2, ref stirrupWidth);

            double stirrupHeight = 0.2;
            DA.GetData(3, ref stirrupHeight);

            double stirrupMaxDistance = 0.2;
            DA.GetData(4, ref stirrupMaxDistance);

            FemDesign.Materials.Material auxiliaryQuality = null;
            DA.GetData(5, ref auxiliaryQuality);

            double auxiliaryDiameter = 0.01;
            DA.GetData(6, ref auxiliaryDiameter);

            double auxiliaryOverlap = 0.2;
            DA.GetData(7, ref auxiliaryOverlap);


            var stirrup = new FemDesign.Reinforcement.ReinforcingRing();

            var stirrups = new FemDesign.Reinforcement.ReinforcingRingStirrups();
            stirrups.Width = stirrupWidth;
            stirrups.Height = stirrupHeight;
            stirrups.MaxDistance = stirrupMaxDistance;
            stirrups.Wire = new Reinforcement.Wire(stirrupDiameter, stirrupQuality, Reinforcement.WireProfileType.Ribbed);

            stirrup.Stirrups = stirrups;

            var auxiliary = new FemDesign.Reinforcement.AuxiliaryReinforcement();
            auxiliary.InnerRadius = 0.50;
            auxiliary.Overlap = auxiliaryOverlap;
            auxiliary.Wire = new Reinforcement.Wire(auxiliaryDiameter, auxiliaryQuality, Reinforcement.WireProfileType.Ribbed);

            stirrup.AuxiliaryReinforcement = auxiliary;

            DA.SetData(0, stirrup);
        }

        protected void setModelProps()
        {
            this.Parent_Component.ExpireSolution(true);
        }
    }
}