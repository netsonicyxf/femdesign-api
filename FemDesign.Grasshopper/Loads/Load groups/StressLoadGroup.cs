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
    public class StressLoadGroup : SubComponent
    {
        public override string name() => "StressLoadGroup";
        public override string display_name() => "StressLoadGroup";

        public override void registerEvaluationUnits(EvaluationUnitManager mngr)
        {
            EvaluationUnit evaluationUnit = new EvaluationUnit(name(), display_name(), "StressLoadGroup");
            evaluationUnit.Icon = FemDesign.Properties.Resources.LoadGroup;
            mngr.RegisterUnit(evaluationUnit);

            evaluationUnit.RegisterInputParam(new Param_Number(), "Standard", "Standard", "", GH_ParamAccess.item, new GH_Number(1.00));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Accidental", "Accidental", "", GH_ParamAccess.item, new GH_Number(1.30));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Factors";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
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

            var relationship = (StruSoft.Interop.StruXml.Data.Ldgroup_relation)Enum.Parse(typeof(StruSoft.Interop.StruXml.Data.Ldgroup_relation), _relationship, true);

            var loadCases = new List<Loads.LoadCase>();
            DA.GetDataList(2, loadCases);

            bool considerMaxLoadGroup = true;
            DA.GetData(3, ref considerMaxLoadGroup);


            double standard = 1.0;
            DA.GetData(4, ref standard);

            double accidental = 1.0;
            DA.GetData(5, ref accidental);


            var stressLoadGroup = new StruSoft.Interop.StruXml.Data.Stress_load_group
            {
                Standard = standard,
                Accidental = accidental,
                Relationship = relationship,
                Load_case = loadCases.Select(x => new StruSoft.Interop.StruXml.Data.Reference_type { Guid = x.Guid.ToString() }).ToList(),
            };

            var ldGroup = new Loads.ModelGeneralLoadGroup();

            ldGroup.StressLoadGroup = stressLoadGroup;
            ldGroup.ConsiderInGmax = considerMaxLoadGroup;
            ldGroup.Name = name;

            DA.SetData(0, ldGroup);
        }
    }
}