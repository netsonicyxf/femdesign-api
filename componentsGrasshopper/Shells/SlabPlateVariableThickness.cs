// https://strusoft.com/
using System;
using System.Collections.Generic;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.GH
{
    public class SlabPlateVariableThickness: GH_Component
    {
        public SlabPlateVariableThickness(): base("Slab.PlateVariableThickness", "PlateVariable", "Create a plate element with variable thickness.", "FemDesign", "Shells")
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddSurfaceParameter("Surface", "Surface", "Surface must be flat", GH_ParamAccess.item);
            pManager.AddGenericParameter("Thickness", "Thickness", "Thickness. List of 3 items [t1, t2, t3].", GH_ParamAccess.list);
            pManager.AddGenericParameter("Material", "Material", "Material.", GH_ParamAccess.item);
            pManager.AddGenericParameter("ShellEccentricity", "Eccentricity", "ShellEccentricity. Optional.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("ShellOrthotropy", "Orthotropy", "ShellOrthotropy. Optional.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("ShellEdgeConnection", "EdgeConnection", "ShellEdgeConnection. Optional.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddTextParameter("Identifier", "Identifier", "Identifier.", GH_ParamAccess.item, "P");
            pManager[pManager.ParamCount - 1].Optional = true;
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Slab", "Slab", "Slab.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get input
            Brep surface = null;
            List<FemDesign.Shells.Thickness> thickness = new List<FemDesign.Shells.Thickness>();
            FemDesign.Materials.Material material = null;
            FemDesign.Shells.ShellEccentricity eccentricity = FemDesign.Shells.ShellEccentricity.Default();
            FemDesign.Shells.ShellOrthotropy orthotropy = FemDesign.Shells.ShellOrthotropy.Default();
            FemDesign.Shells.ShellEdgeConnection edgeConnection = FemDesign.Shells.ShellEdgeConnection.Rigid();
            string identifier = "P";
            if(!DA.GetData(0, ref surface)) { return; }
            if(!DA.GetDataList(1, thickness)) { return; }
            if(!DA.GetData(2, ref material)) { return; }
            if(!DA.GetData(3, ref eccentricity))
            {
                // pass
            }
            if(!DA.GetData(4, ref orthotropy))
            {
                // pass
            }
            if(!DA.GetData(5, ref edgeConnection))
            {
                // pass
            }
            if(!DA.GetData(6, ref identifier))
            {
                // pass
            }
            if (surface == null || thickness == null || material == null || eccentricity == null || orthotropy == null || edgeConnection == null) { return; }
            if (thickness.Count != 3)
            {
                throw new System.ArgumentException("Thickness must contain exactly 3 items.");
            }

            //
            FemDesign.Geometry.Region region = FemDesign.Geometry.Region.FromRhino(surface);

            //
            FemDesign.Shells.Slab obj = FemDesign.Shells.Slab.Plate(identifier, material, region, edgeConnection, eccentricity, orthotropy, thickness);

            // return
            DA.SetData(0, obj);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.PlateVariableThickness;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("1a00487a-beed-49ba-b9e9-d4b45c201c4b"); }
        }
    }
}