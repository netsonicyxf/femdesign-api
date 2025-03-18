// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;
using Grasshopper.Kernel.Special;
using Rhino.Geometry;
using FemDesign.Loads;

using FemDesign.Grasshopper.Extension.ComponentExtension;
using System.Linq;
using System.Drawing;
using System.Reflection;
using FemDesign.Properties;

namespace FemDesign.Grasshopper
{
    public class DrawingLayer : FEM_Design_API_Component
    {
        public DrawingLayer() : base("Layer", "Layer", "", CategoryName.Name(), "ModellingTools")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            // create pmanager to accept name, colour, hidden and protected
            pManager.AddTextParameter("Name", "Name", "Name of Layer", GH_ParamAccess.item, "0");
            pManager.AddColourParameter("Colour", "Colour", "Colour of Layer", GH_ParamAccess.item, System.Drawing.Color.Black);
            pManager.AddBooleanParameter("Hidden", "Hidden", "Hidden Layer", GH_ParamAccess.item, false);
            pManager.AddBooleanParameter("Protected", "Protected", "Protected Layer", GH_ParamAccess.item, false);
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Layer", "Layer", "", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // create variables
            string name = "";
            DA.GetData(0, ref name);

            System.Drawing.Color colour = System.Drawing.Color.FromArgb(0, 0, 0);
            DA.GetData(1, ref colour);

            bool hidden = false;
            DA.GetData(2, ref hidden);

            bool @protected = false;
            DA.GetData(3, ref @protected);


            var layer = new StruSoft.Interop.StruXml.Data.Layer_type
            {
                Name = name,
                Colour = ColorTranslator.ToHtml((Color)colour).Substring(1),
                Hidden = hidden,
                Protected = @protected
            };

            // output
            DA.SetData(0, layer);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {

                return Resources.LayerDrawing;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{24FAD0A2-5CD9-4598-A9E9-0A3D5C5B5AF0}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.last;

    }
}