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
using static FemDesign.Calculate.ConcreteDesignConfig;
using FemDesign.GenericClasses;
using FemDesign.Calculate;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.ToolTip;
using System.Threading;

namespace FemDesign.Grasshopper
{
    public class AccidentalLoadGroup : SubComponent
    {
        public override string name() => "AccidentalLoadGroup";
        public override string display_name() => "AccidentalLoadGroup";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "AccidentalLoadGroup");
            evaluationUnit.Icon = FemDesign.Properties.Resources.LoadGroup;
            mngr.RegisterUnit(evaluationUnit);

            evaluationUnit.RegisterInputParam(new Param_Number(), "SafetyFactor", "SafetyFactor", "", GH_ParamAccess.item, new GH_Number(1.30));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "UsingPsi1", "UsingPsi1", "", GH_ParamAccess.item, new GH_Boolean(true));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "SnowEffect", "SnowEffect", "", GH_ParamAccess.item, new GH_Boolean(true));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;


            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Options";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            evaluationUnit.AddMenu(gH_ExtendableMenu0);
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

            bool usingPsi = true;
            DA.GetData(5, ref usingPsi);

            bool snowEffect = true;
            DA.GetData(6, ref snowEffect);



            var accidentalLoadGroup = new StruSoft.Interop.StruXml.Data.Accidental_load_group
            {
                Safety_factor = safetyFactor,
                Using_Psi_1 = usingPsi,
                Load_case = loadCases.Select(x => new StruSoft.Interop.StruXml.Data.Reference_type { Guid = x.Guid.ToString() }).ToList(),
            };

            var ldGroup = new Loads.ModelGeneralLoadGroup();

            ldGroup.AccidentalLoadGroup= accidentalLoadGroup;
            ldGroup.ConsiderInGmax = considerMaxLoadGroup;
            ldGroup.Name = name;

            DA.SetData(0, ldGroup);
        }
    }
}