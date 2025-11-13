using Grasshopper.Kernel;
using Grasshopper.Kernel.Parameters;
using Grasshopper.Kernel.Types;
using FemDesign.Grasshopper.Components.UIWidgets;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Rhino.Geometry;
using FemDesign.Grasshopper;
using System.Windows.Forms;
using FemDesign.Grasshopper.Extension.ComponentExtension;
using FemDesign.Loads;
using Grasshopper.Kernel.Special;
using FemDesign.Reinforcement;

namespace FemDesign.Grasshopper
{
    public class PunchingBase : GH_SwitcherComponent
    {
        private List<SubComponent> _subcomponents = new List<SubComponent>();
        public override string UnitMenuName => "PunchingReinforcement";
        protected override string DefaultEvaluationUnit => _subcomponents[0].name();
        public override Guid ComponentGuid => new Guid("{68F38838-9C23-46CC-A656-386925AAE3B9}");
        public override GH_Exposure Exposure => GH_Exposure.tertiary;

        protected override Bitmap Icon => FemDesign.Properties.Resources.Punching;

        public PunchingBase()
            : base("Punching", "Punching",
              "Punching reinforcement settings for a FEM-Design model.",
              CategoryName.Name(), SubCategoryName.CatReinforcement())
        {
            ((GH_Component)this).Hidden = true;
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.RegisterParam(new Param_GenericObject(), "PunchingReinforcement", "PunchingReinforcement", "Punching reinforcement settings.");
        }

        protected override void RegisterEvaluationUnits(EvaluationUnitManager mngr)
        {
            _subcomponents.Add(new StudRail());
            _subcomponents.Add(new StirrupCircular());

            foreach (SubComponent item in _subcomponents)
            {
                item.registerEvaluationUnits(mngr);
            }
        }

        protected override void OnComponentLoaded()
        {
            base.OnComponentLoaded();
            foreach (SubComponent item in _subcomponents)
            {
                item.OnComponentLoaded();
            }
        }

        protected override void SolveInstance(IGH_DataAccess DA, EvaluationUnit unit)
        {
            if (unit == null)
            {
                return;
            }
            foreach (SubComponent item in _subcomponents)
            {
                if (unit.Name.Equals(item.name()))
                {
                    item.SolveInstance(DA, out var msg, out var level);
                    if (msg != "")
                    {
                        ((GH_ActiveObject)this).AddRuntimeMessage(level, msg);
                    }
                    return;
                }
            }
            throw new Exception("Invalid sub-component");
        }
        // Part of the code that allows to extend the menu with additional items
        // Right click on the component to see the options
        public override void AppendAdditionalMenuItems(ToolStripDropDown menu)
        {
            base.AppendAdditionalMenuItems(menu);
            if (evalUnits.Units.Count > 0)
            {
                Menu_AppendSeparator(menu);
                ToolStripMenuItem toolStripMenuItem = Menu_AppendItem(menu, "PunchingReinforcement");
                foreach (EvaluationUnit unit in evalUnits.Units)
                {
                    Menu_AppendItem(toolStripMenuItem.DropDown, unit.Name, Menu_ActivateUnit, null, true, unit.Active).Tag = unit;
                }
                Menu_AppendSeparator(menu);
            }
        }
        private void Menu_ActivateUnit(object sender, EventArgs e)
        {
            try
            {
                EvaluationUnit evaluationUnit = (EvaluationUnit)((ToolStripMenuItem)sender).Tag;
                if (evaluationUnit != null)
                {
                    SwitchUnit(evaluationUnit);
                }
            }
            catch (Exception ex)
            {
                throw ex;
            }
        }
    }
}