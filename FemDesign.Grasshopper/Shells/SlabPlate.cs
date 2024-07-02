// https://strusoft.com/
using System;
using System.Collections.Generic;
using System.Linq;
using Grasshopper.Kernel;
using Rhino.Geometry;

namespace FemDesign.Grasshopper
{
    public class SlabPlate: FEM_Design_API_Component
    {
        public SlabPlate(): base("Plate", "Construct", "Construct a plate element.", CategoryName.Name(), SubCategoryName.Cat2b())
        {

        }
        protected override void RegisterInputParams(GH_InputParamManager pManager)
        {
            pManager.AddSurfaceParameter("Surface", "Surface", "Surface must be flat.", GH_ParamAccess.item);
            pManager.AddNumberParameter("Thickness", "Thickness", "Thickness. [m]", GH_ParamAccess.item, 0.15);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("Material", "Material", "Material.", GH_ParamAccess.item);
            pManager.AddGenericParameter("ShellEccentricity", "Eccentricity", "ShellEccentricity. Optional.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("ShellOrthotropy", "Orthotropy", "ShellOrthotropy. Optional.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddGenericParameter("EdgeConnection", "EdgeConnection", "EdgeConnection. Optional.", GH_ParamAccess.list);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddVectorParameter("LocalX", "LocalX", "Set local x-axis. Vector must be perpendicular to surface local z-axis. Local y-axis will be adjusted accordingly. Optional, local x-axis from surface coordinate system used if undefined.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddVectorParameter("LocalZ", "LocalZ", "Set local z-axis. Vector must be perpendicular to surface local x-axis. Local y-axis will be adjusted accordingly. Optional, local z-axis from surface coordinate system used if undefined.", GH_ParamAccess.item);
            pManager[pManager.ParamCount - 1].Optional = true;
            pManager.AddTextParameter("Identifier", "Identifier", "Identifier. Optional.", GH_ParamAccess.item, "P");
            pManager[pManager.ParamCount - 1].Optional = true;
        }
        protected override void RegisterOutputParams(GH_OutputParamManager pManager)
        {
            pManager.AddGenericParameter("Slab", "Slab", "Slab.", GH_ParamAccess.item);
        }
        protected override void SolveInstance(IGH_DataAccess DA)
        {
            // get inputs
            Brep surface = null;
            if(!DA.GetData(0, ref surface)) { return; }

            double thickness = 0.15;
            DA.GetData(1, ref thickness);

            FemDesign.Materials.Material material = null;
            if(!DA.GetData(2, ref material)) { return; }

            FemDesign.Shells.ShellEccentricity eccentricity = FemDesign.Shells.ShellEccentricity.Default;
            DA.GetData(3, ref eccentricity);
            
            FemDesign.Shells.ShellOrthotropy orthotropy = FemDesign.Shells.ShellOrthotropy.Default;
            DA.GetData(4, ref orthotropy);
            
            List<FemDesign.Shells.EdgeConnection> edgeConnections = new List<FemDesign.Shells.EdgeConnection>();
            DA.GetDataList(5, edgeConnections);

            Rhino.Geometry.Vector3d x = Vector3d.Zero;
            DA.GetData(6, ref x);

            Rhino.Geometry.Vector3d z = Vector3d.Zero;
            DA.GetData(7, ref z);
            
            string identifier = "P";
            DA.GetData(8, ref identifier);

            // check inputs
            if (surface == null || material == null || eccentricity == null || orthotropy == null || identifier == null) { return; }

            // convert geometry
            FemDesign.Geometry.Region region = surface.FromRhino();

            // get thickness
            List<FemDesign.Shells.Thickness> thicknessObj = new List<FemDesign.Shells.Thickness>();
            thicknessObj.Add(new FemDesign.Shells.Thickness(region.Plane.Origin, thickness));
            

            // create a slab plate
            FemDesign.Shells.Slab obj = FemDesign.Shells.Slab.Plate(identifier, material, region, FemDesign.Shells.EdgeConnection.Rigid, eccentricity, orthotropy, thicknessObj);


            // set edge connections on slab
            obj.SlabPart.Region.SetEdgeConnections(edgeConnections);

            // set local x-axis
            if (!x.Equals(Vector3d.Zero))
            {
                obj.SlabPart.LocalX = x.FromRhino();
            }

            // set local z-axis
            if (!z.Equals(Vector3d.Zero))
            {
                obj.SlabPart.LocalZ = z.FromRhino();
            }

            // return
            DA.SetData(0, obj);
        }
        protected override System.Drawing.Bitmap Icon
        {
            get
            {
                return FemDesign.Properties.Resources.Plate;
            }
        }
        public override Guid ComponentGuid
        {
            get { return new Guid("{9CC107E2-4647-4F9D-97DE-96348736C1E9}"); }
        }
        public override GH_Exposure Exposure => GH_Exposure.primary;

    }
}