using FemDesign.Geometry;
using System.Xml.Serialization;
using System;


namespace FemDesign.Reinforcement
{
    [System.Serializable]
    public partial class PunchingArea: EntityBase
    {
        [XmlElement("base_shell", Order = 1)]
        public GuidListType BaseShell { get; set; }

        [XmlElement("connected_bar", Order = 2)]
        public GuidListType ConnectedBar { get; set; }

        [XmlElement("local_pos", Order = 3)]
        public Geometry.Point3d LocalPos { get; set; }

        [XmlElement("local_x", Order = 4)]
        public Geometry.Vector3d LocalX { get; set; }

        [XmlElement("local_y", Order = 5)]
        public Geometry.Vector3d LocalY { get; set; }

        [XmlElement("reference_points_offset", Order = 6)]
        public Geometry.Point3d RefPointsOffset { get; set; }

        [XmlElement("region", Order = 7)]
        public Geometry.Region Region { get; set; }

        [XmlAttribute("downward")]
        public bool Downward { get; set; }

        [XmlAttribute("manual_design")]
        public bool ManualDesign { get; set; }

        [XmlAttribute("name")]
        public string Name { get; set; }
        public PunchingArea()
        {
            this.EntityCreated();
        }

        internal FemDesign.Bars.Bar FindClosestBar(Model model)
        {
            if (model == null)
                return null;

            var bars = model.Entities.Bars;
            if (bars == null)
                return null;

            FemDesign.Bars.Bar closestBar = null;
            double minDistance = 0.001;

            foreach (var bar in bars)
            {
                var curve = bar.BarPart.Edge;
                if (curve == null)
                    continue;

                // Calculate distance from LocalPos to the bar (line segment)
                double distance = DistancePointToSegment(this.LocalPos, curve);
                if (distance < minDistance)
                {
                    closestBar = bar;
                    break;
                }
            }

            // You may want to define a threshold for "attached" (e.g., < 1e-6)
            return closestBar;
        }

        // Helper method to calculate distance from point to segment
        private static double DistancePointToSegment(FemDesign.Geometry.Point3d p, FemDesign.Geometry.Edge edge)
        {
            var a = edge.Points[0];
            var b = edge.Points[1];

            // Vector from a to p
            double dx = b.X - a.X;
            double dy = b.Y - a.Y;
            double dz = b.Z - a.Z;

            double t = ((p.X - a.X) * dx + (p.Y - a.Y) * dy + (p.Z - a.Z) * dz) / (dx * dx + dy * dy + dz * dz);
            t = System.Math.Max(0, Math.Min(1, t));

            double closestX = a.X + t * dx;
            double closestY = a.Y + t * dy;
            double closestZ = a.Z + t * dz;

            double distX = p.X - closestX;
            double distY = p.Y - closestY;
            double distZ = p.Z - closestZ;

            return Math.Sqrt(distX * distX + distY * distY + distZ * distZ);
        }
    }
}
