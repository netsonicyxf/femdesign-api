using FemDesign.Geometry;
using StruSoft.Interop.StruXml.Data;
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Reflection.Emit;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;
using FemDesign.GenericClasses;

namespace FemDesign.Drawing
{
    public class Point3d : IDrawing
    {
        [XmlIgnore]
        public double X { get; set; }
        [XmlIgnore]
        public double Y { get; set; }
        [XmlIgnore]
        public double Z { get; set; }


        [XmlElement("style")]
        public Style_type Style { get; set; }

        private Point3d()
        {
        }

        public Point3d(double x, double y, double z, Layer_type layer, Style_type style)
        {
            this.X = x;
            this.Y = y;
            this.Z = z;


            this.Style = style;
            this.Style.LayerObj = layer;
        }


        public static implicit operator StruSoft.Interop.StruXml.Data.Point_type(Point3d point)
        {
            return new StruSoft.Interop.StruXml.Data.Point_type
            {
                Location = new StruSoft.Interop.StruXml.Data.Point_type_3d
                {
                    X = point.X,
                    Y = point.Y,
                    Z = point.Z,
                },
                Style = point.Style,
            };
        }

    }
}
