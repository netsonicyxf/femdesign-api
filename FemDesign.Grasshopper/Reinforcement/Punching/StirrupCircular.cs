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


            evaluationUnit.RegisterInputParam(new Param_Plane(), "Point|Plane", "Point|Plane", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Brep(), "Region", "Region", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "InnerRadius", "InnerRadius", "[m]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "ReinforcingMaterial", "ReinforcingMaterial", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Diameter", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Width", "Width", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "MaxDistance", "MaxDistance", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "ReinforcingMaterial", "ReinforcingMaterial", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Diameter", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Overlap", "Overlap", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;


            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Stirrup";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[4]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[5]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[6]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[7]);
            evaluationUnit.AddMenu(gH_ExtendableMenu0);


            GH_ExtendableMenu gH_ExtendableMenu1 = new GH_ExtendableMenu(1, "");
            gH_ExtendableMenu1.Name = "Auxiliary";
            gH_ExtendableMenu1.Expand();
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[8]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[9]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[10]);
            evaluationUnit.AddMenu(gH_ExtendableMenu1);
        }

        public override void SolveInstance(IGH_DataAccess DA, out string msg, out GH_RuntimeMessageLevel level)
        {
            msg = "";
            level = GH_RuntimeMessageLevel.Warning;

            var plane = Rhino.Geometry.Plane.WorldXY;
            DA.GetData(0, ref plane);

            Rhino.Geometry.Brep region = null;
            DA.GetData(1, ref region);

            double innerRadius = 1.0;
            DA.GetData(2, ref innerRadius);

            FemDesign.Materials.Material stirrupQuality = null;
            DA.GetData(3, ref stirrupQuality);

            double stirrupDiameter = 10;
            DA.GetData(4, ref stirrupDiameter);
            stirrupDiameter /= 1000.0; // mm to m

            double stirrupWidth = 200;
            DA.GetData(5, ref stirrupWidth);
            stirrupWidth /= 1000.0; // mm to m

            double stirrupHeight = 200;
            DA.GetData(6, ref stirrupHeight);
            stirrupHeight /= 1000.0; // mm to m

            double stirrupMaxDistance = 200;
            DA.GetData(7, ref stirrupMaxDistance);
            stirrupMaxDistance /= 1000.0; // mm to m

            FemDesign.Materials.Material auxiliaryQuality = null;
            DA.GetData(8, ref auxiliaryQuality);

            double auxiliaryDiameter = 10;
            DA.GetData(9, ref auxiliaryDiameter);
            auxiliaryDiameter /= 1000.0; // mm to m

            double auxiliaryOverlap = 200;
            DA.GetData(10, ref auxiliaryOverlap);
            auxiliaryOverlap /= 1000.0; // mm to m

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

            var reinforcingRing = new FemDesign.Reinforcement.ReinforcingRing();
            {
                // stirrups
                var stirrups = new FemDesign.Reinforcement.ReinforcingRingStirrups();
                stirrups.Width = stirrupWidth;
                stirrups.Height = stirrupHeight;
                stirrups.MaxDistance = stirrupMaxDistance;
                stirrups.Wire = new Reinforcement.Wire(stirrupDiameter, stirrupQuality, Reinforcement.WireProfileType.Ribbed);

                // auxiliary reinforcement
                var auxiliary = new FemDesign.Reinforcement.AuxiliaryReinforcement();
                auxiliary.InnerRadius = 0.50;
                auxiliary.Overlap = auxiliaryOverlap;
                auxiliary.Wire = new Reinforcement.Wire(auxiliaryDiameter, auxiliaryQuality, Reinforcement.WireProfileType.Ribbed);

                // assign to reinforcing ring
                reinforcingRing.Stirrups = stirrups;
                reinforcingRing.AuxiliaryReinforcement = auxiliary;
            }


            punchingReinforcement.ReinforcingRing = reinforcingRing;

            DA.SetData(0, punchingReinforcement);
        }

        protected void setModelProps()
        {
            this.Parent_Component.ExpireSolution(true);
        }
    }
}