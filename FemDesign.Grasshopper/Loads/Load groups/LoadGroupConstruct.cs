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

namespace FemDesign.Grasshopper
{
    public class LoadGroupConstruct : GH_SwitcherComponent
    {
        private List<SubComponent> _subcomponents = new List<SubComponent>();
        public override string UnitMenuName => "LoadGroup";
        protected override string DefaultEvaluationUnit => _subcomponents[0].name();
        public override Guid ComponentGuid => new Guid("{02C157DD-BC06-4B1B-9167-9950CDF0F050}");
        public override GH_Exposure Exposure => GH_Exposure.quarternary;

        protected override Bitmap Icon => FemDesign.Properties.Resources.Config;

        public LoadGroupConstruct()
            : base("LoadGroup.Construct", "LoadGroup.Construct",
              "",
              CategoryName.Name(), SubCategoryName.Cat3())
        {
            ((GH_Component)this).Hidden = true;
        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddTextParameter("Name", "Name", "", GH_ParamAccess.item);
            pManager.AddTextParameter("Relationship", "Relationship", "Connect 'ValueList' to get the options.\nAlternative\nSimultaneous\nEntire\nCustom - NOT IMPLEMENTED", GH_ParamAccess.item, "Alternative");
            pManager.AddGenericParameter("LoadCases", "LoadCases", "", GH_ParamAccess.list);
            pManager.AddBooleanParameter("ConsiderInMaxLoadGroup", "ConsiderInMaxLoadGroup", "", GH_ParamAccess.item, true);
            pManager[pManager.ParamCount - 1].Optional = true;
        }

        protected override void BeforeSolveInstance()
        {
            ValueListUtils.UpdateValueLists(this, 1, Enum.GetNames(typeof(FemDesign.Loads.ELoadGroupRelationship)).ToList());
        }

        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.RegisterParam(new Param_GenericObject(), "LoadGroup", "LoadGroup", "");
        }

        protected override void RegisterEvaluationUnits(EvaluationUnitManager mngr)
        {
            _subcomponents.Add(new PermanentLoadGroup());
            _subcomponents.Add(new StressLoadGroup());
            _subcomponents.Add(new TemporaryLoadGroup());
            _subcomponents.Add(new AccidentalLoadGroup());


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
                ToolStripMenuItem toolStripMenuItem = Menu_AppendItem(menu, "LoadGroup");
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