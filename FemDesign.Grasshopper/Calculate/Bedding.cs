// https://strusoft.com/
using System;
using Grasshopper.Kernel;
using FemDesign;
using FemDesign.Calculate;
using FemDesign.Grasshopper.Extension.ComponentExtension;
using Grasshopper.Kernel.Special;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using FemDesign.Loads;

namespace FemDesign.Grasshopper
{
    public class CalculationParametersBeddingDefine : FEM_Design_API_Component
    {
        public CalculationParametersBeddingDefine() : base("Bedding.Define", "Bedding", "Define calculation parameters for a bedding calculation.", CategoryName.Name(), SubCategoryName.Cat7a())
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddTextParameter("LdCombChar", "LdCombChar", "Characteristic Load Combination name", GH_ParamAccess.item);
            pManager.AddTextParameter("MeshPrep", "MeshPrep", "Connect 'ValueList' to get the options.\nMeshPrep type:\nFactoryDefault\nActualMesh.", GH_ParamAccess.item, "FactoryDefault");
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddNumberParameter("StiffX", "StiffX", "", GH_ParamAccess.item, 0);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddNumberParameter("StiffY", "StiffY", "", GH_ParamAccess.item, 0);
            pManager[pManager.ParamCount - 1].Optional = true;
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Bedding", "Bedding", "Bedding.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            string ldCombChar = "";
            DA.GetData(0, ref ldCombChar);

            string meshPrep = "";
            DA.GetData(1, ref meshPrep);

            double stiffX = 0.5;
            DA.GetData(2, ref stiffX);

            double stiffY = 0.5;
            DA.GetData(3, ref stiffY);


            MeshPrep _meshPrep = FemDesign.GenericClasses.EnumParser.Parse<MeshPrep>(meshPrep);

            Bedding obj = new Calculate.Bedding(ldCombChar, _meshPrep, stiffX, stiffY); 

            // return
            DA.SetData(0, obj);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return Properties.Resources.Bedding;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{9BEAD3CF-BCC8-42C9-80D9-AC9BE45F7C11}"); }
        }

        protected override void BeforeSolveInstance()
        {
            ValueListUtils.UpdateValueLists(this, 1, Enum.GetNames(typeof(MeshPrep)).ToList(), null, GH_ValueListMode.DropDown);
        }


        public override GH_Exposure Exposure => GH_Exposure.tertiary;

    }
}