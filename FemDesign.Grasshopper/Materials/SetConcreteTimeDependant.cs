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
using StruSoft.Interop;
using FemDesign.Materials;

namespace FemDesign.Grasshopper
{
    public class MaterialSetTDA : GH_SwitcherComponent
    {
        /// </summary>
        public MaterialSetTDA() : base("SetTDA", "SetTDA", "", CategoryName.Name(), SubCategoryName.Cat4a())
        {

        }

        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddGenericParameter("Material", "Material", "Material.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = false;


        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Material", "Material", "Material.", GH_ParamAccess.item);
        }

        protected override void RegisterEvaluationUnits(EvaluationUnitManager mngr)
        {

            EvaluationUnit evaluationUnit = new EvaluationUnit("ExtendableComponent", "ExtComp", "A Test Component");
            mngr.RegisterUnit(evaluationUnit);

            evaluationUnit.RegisterInputParam(new Param_Integer(), "t0", "t0", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "Humidity", "Humidity", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "CalculateAc", "CalculateAc", "", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Ac", "Ac", "", GH_ParamAccess.item, new GH_Number(1.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "u", "u", "", GH_ParamAccess.item, new GH_Number(1.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "NonLinearCreep", "NonLinearCreep", "", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "CementType", "CementType", "Cement Type as integer according to FemDesign API.", GH_ParamAccess.item, new GH_Integer(0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(StruSoft.Interop_24.Cement_type)).ToList();

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "IncreaseFinalValue", "IncreaseFinalValue", "", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            GH_ExtendableMenu gH_ExtendableMenu0 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu0.Name = "Creep";
            gH_ExtendableMenu0.Expand();
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[0]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[1]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[2]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[3]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[4]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[5]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[6]);
            gH_ExtendableMenu0.RegisterInputPlug(evaluationUnit.Inputs[7]);

            evaluationUnit.AddMenu(gH_ExtendableMenu0);


            evaluationUnit.RegisterInputParam(new Param_Integer(), "t0", "t0", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "Humidity", "Humidity", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Boolean(), "CalculateAc", "CalculateAc", "", GH_ParamAccess.item, new GH_Boolean(false));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "Ac", "Ac", "", GH_ParamAccess.item, new GH_Number(1.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Number(), "u", "u", "", GH_ParamAccess.item, new GH_Number(1.0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "CementType", "CementType", "Cement Type as integer according to FemDesign API.", GH_ParamAccess.item, new GH_Integer(0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(StruSoft.Interop_24.Cement_type)).ToList();


            GH_ExtendableMenu gH_ExtendableMenu1 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu1.Name = "Shrinkage";
            gH_ExtendableMenu1.Expand();
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[8]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[9]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[10]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[11]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[12]);
            gH_ExtendableMenu1.RegisterInputPlug(evaluationUnit.Inputs[13]);
            evaluationUnit.AddMenu(gH_ExtendableMenu1);



            evaluationUnit.RegisterInputParam(new Param_Integer(), "t0", "t0", "", GH_ParamAccess.item);
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;

            evaluationUnit.RegisterInputParam(new Param_Integer(), "CementType", "CementType", "Cement Type as integer according to FemDesign API.", GH_ParamAccess.item, new GH_Integer(0));
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].Parameter.Optional = true;
            evaluationUnit.Inputs[evaluationUnit.Inputs.Count - 1].EnumInput = Enum.GetNames(typeof(StruSoft.Interop_24.Cement_type)).ToList();

            GH_ExtendableMenu gH_ExtendableMenu2 = new GH_ExtendableMenu(0, "");
            gH_ExtendableMenu2.Name = "Elasticity";
            gH_ExtendableMenu2.Expand();
            gH_ExtendableMenu2.RegisterInputPlug(evaluationUnit.Inputs[14]);
            gH_ExtendableMenu2.RegisterInputPlug(evaluationUnit.Inputs[15]);
            evaluationUnit.AddMenu(gH_ExtendableMenu2);
        }



        /// <summary>
        /// This is the method that actually does the work.
        /// </summary>
        /// <param name="DA">The DA object can be used to retrieve data from input parameters and 
        /// to store data in output parameters.</param>
        protected override void SolveInstance(IGH_DataAccess DA, EvaluationUnit unit)
        {
            FemDesign.Materials.Material material = null;
            DA.GetData(0, ref material);

            // creep
            int t0_creep = 0;
            DA.GetData(1, ref t0_creep);

            int humidity = 0;
            DA.GetData(2, ref humidity);

            bool calculateAc = false;
            DA.GetData(3, ref calculateAc);

            double Ac = 1.0;
            DA.GetData(4, ref Ac);

            double u = 1.0;
            DA.GetData(5, ref u);

            bool nonLinearCreep = false;
            DA.GetData(6, ref nonLinearCreep);

            int cementType_creep = 0;
            DA.GetData(7, ref cementType_creep);

            bool increaseFinalValue = false;
            DA.GetData(8, ref increaseFinalValue);


            // shrinkage
            int t0_shrinkage = 0;
            DA.GetData(9, ref t0_shrinkage);

            int humidity_shrinkage = 0;
            DA.GetData(10, ref humidity_shrinkage);

            bool calculateAc_shrinkage = false;
            DA.GetData(11, ref calculateAc_shrinkage);

            double Ac_shrinkage = 1.0;
            DA.GetData(12, ref Ac_shrinkage);

            double u_shrinkage = 1.0;
            DA.GetData(13, ref u_shrinkage);

            int cementType_shrinkage = 0;
            DA.GetData(14, ref cementType_shrinkage);

            // elasticity
            int t0_elasticity = 0;
            DA.GetData(15, ref t0_elasticity);

            int cementType_elasticity = 0;
            DA.GetData(16, ref cementType_elasticity);


            var newMaterial = material.SetCreep(t0_creep, humidity, calculateAc, Ac, u, nonLinearCreep, (StruSoft.Interop_24.Cement_type)cementType_creep, increaseFinalValue);
            newMaterial = newMaterial.SetShrinkage(t0_shrinkage, humidity_shrinkage, calculateAc_shrinkage, Ac_shrinkage, u_shrinkage, (StruSoft.Interop_24.Cement_type)cementType_shrinkage);

            material = newMaterial.setElasticity(t0_elasticity, (StruSoft.Interop_24.Cement_type)cementType_elasticity);



            DA.SetData(0, material);



        }

        /// <summary>
        /// Provides an Icon for every component that will be visible in the User Interface.
        /// Icons need to be 24x24 pixels.
        /// </summary>
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                // You can add image files to your project resources and access them like this:
                return FemDesign.Properties.Resources.MaterialSetConcreteMaterialProperties;
            }
        }

        //To recompute component/solve instance method.
        protected void setModelProps()
        {
            ((GH_DocumentObject)this).ExpireSolution(true);
        }


        /// <summary>
        /// Each component must have a unique Guid to identify it. 
        /// It is vital this Guid doesn't change otherwise old ghx files 
        /// that use the old ID will partially fail during loading.
        /// </summary>
        public override Guid ComponentGuid
        {
            get { return new Guid("{A80FC5B7-F548-4DBF-97C4-AE73FA07CCC6}"); }
        }
    }
}