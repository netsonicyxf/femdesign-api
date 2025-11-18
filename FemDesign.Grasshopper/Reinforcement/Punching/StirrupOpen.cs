using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;


namespace FemDesign.Grasshopper
{

    public class StirrupOpen : SubComponent
    {
        public override string name() => "StirrupOpen";
        public override string display_name() => "StirrupOpen";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "");
            mngr.RegisterUnit(evaluationUnit);
            //evaluationUnit.Icon = FemDesign.Properties.Resources.StirrupCircular;

            evaluationUnit.RegisterInputParam(new Param_Plane(), "Point|Plane", "Point|Plane", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Brep(), "Region", "Region", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "ReinforcingMaterial", "ReinforcingMaterial", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Diameter", "Diameter", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Width", "Width", "[m]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_GenericObject(), "Length", "Length", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = false;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Height", "Height", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Distance_X", "Distance_X", "[mm]", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Distance_Y", "Distance_Y", "[mm]", GH_ParamAccess.item);
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
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[8]);
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

            FemDesign.Materials.Material stirrupQuality = null;
            DA.GetData(2, ref stirrupQuality);

            double stirrupDiameter = 10;
            DA.GetData(3, ref stirrupDiameter);
            stirrupDiameter /= 1000.0; // mm to m

            double stirrupWidth = 200;
            DA.GetData(4, ref stirrupWidth);
            stirrupWidth /= 1000.0; // mm to m

            double stirrupLength = 200;
            DA.GetData(5, ref stirrupLength);
            stirrupLength /= 1000.0; // mm to m

            double stirrupHeight = 200;
            DA.GetData(6, ref stirrupHeight);
            stirrupHeight /= 1000.0; // mm to m

            double distance_x = 200;
            DA.GetData(7, ref distance_x);
            distance_x /= 1000.0; // mm to m

            double distance_y = 200;
            DA.GetData(8, ref distance_y);
            distance_y /= 1000.0; // mm to m

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

            var openStirrups = new FemDesign.Reinforcement.OpenStirrups();
            {
                openStirrups.Wire = new FemDesign.Reinforcement.Wire(stirrupDiameter, stirrupQuality, Reinforcement.WireProfileType.Ribbed);
                openStirrups.Region = region.FromRhino();
                openStirrups.Width = stirrupWidth;
                openStirrups.Length = stirrupLength;
                openStirrups.Height = stirrupHeight;
                openStirrups.DistanceX = distance_x;
                openStirrups.DistanceY = distance_y;
            }


            punchingReinforcement.OpenStirrups = openStirrups;

            DA.SetData(0, punchingReinforcement);
        }

        protected void setModelProps()
        {
            this.Parent_Component.ExpireSolution(true);
        }
    }
}