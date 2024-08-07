﻿// https://strusoft.com/
using System;
using System.Collections.Generic;
using FemDesign.Loads;
using System.Runtime.InteropServices;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.Grasshopper
{
    public class SurfaceLoadUniform : FEM_Design_API_Component
    {
        public SurfaceLoadUniform() : base("SurfaceLoad.Uniform", "Uniform", "Create a uniform surface load.", CategoryName.Name(), SubCategoryName.Cat3())
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddSurfaceParameter("Surface", "Surface", "Surface.", GH_ParamAccess.item);
            pManager.AddVectorParameter("Force", "Force", "Force. [kN/m²]", GH_ParamAccess.item);
            pManager.AddBooleanParameter("LoadProjection", "LoadProjection", "LoadProjection. \nFalse: Intensity meant along action line (eg. dead load). \nTrue: Intensity meant perpendicular to direction of load (eg. snow load).", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("LoadCase", "LoadCase", "LoadCase.", GH_ParamAccess.item);
            pManager.AddTextParameter("Comment", "Comment", "Comment.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("SurfaceLoad", "SurfaceLoad", "SurfaceLoad.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            Brep surface = null;
            if (!DA.GetData("Surface", ref surface)) { return; }

            Vector3d force = Vector3d.Zero;
            if (!DA.GetData("Force", ref force)) { return; }

            dynamic loadCase = null;
            if (!DA.GetData("LoadCase", ref loadCase)) { return; }

            bool loadProjection = false;
            DA.GetData("LoadProjection", ref loadProjection);
            
            string comment = "";
            DA.GetData("Comment", ref comment);

            if (surface == null || force == null || loadCase == null) { return; }

            // Convert geometry
            FemDesign.Geometry.Region region = surface.FromRhino();
            FemDesign.Geometry.Vector3d _force = force.FromRhino();


            FemDesign.Loads.SurfaceLoad obj = null;

            if (loadCase.Value is string str)
            {
                if (str != "caseless")
                    throw new Exception("Load case must be a Load case object or \"caseless\" string");

                obj = FemDesign.Loads.SurfaceLoad.CaselessUniform(region, _force);
            }
            else if (loadCase.Value is FemDesign.Loads.LoadCase ldCase)
            {
                obj = FemDesign.Loads.SurfaceLoad.Uniform(region, _force, ldCase, loadProjection, comment);
            }

            DA.SetData("SurfaceLoad", obj);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.SurfaceLoadUniform;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{24F37183-4590-475B-9D7E-4EE5872014BB}"); }
        }

        public override GH_Exposure Exposure => GH_Exposure.tertiary;

    }
}