using FemDesign.Bars.Buckling;
using FemDesign.GenericClasses;
using FemDesign.Geometry;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Serialization;
using static FemDesign.AuxiliaryResults.ResultPoint;

namespace FemDesign.AuxiliaryResults
{
    [System.Serializable]
    public class VirtualBarContainer
    {
        [System.Xml.Serialization.XmlElement("result_line", Order = 1)]
        public List<VirtualBar> VirtualBars = new List<VirtualBar>();

    }
    [System.Serializable]
    public class VirtualBar : NamedEntityBase, IStructureElement
    {
        [XmlIgnore]
        private static int _resultPointinstances = 0;
        public static void ResetInstanceCount() => _resultPointinstances = 0;
        protected override int GetUniqueInstanceCount() => ++_resultPointinstances;

        [XmlElement("start")]
        public FemDesign.Geometry.Point3d Start { get; set; }

        [XmlElement("end")]
        public FemDesign.Geometry.Point3d End { get; set; }

        [XmlElement("y_axis")]
        public FemDesign.Geometry.Vector3d YAxis { get; set; }

        [XmlElement("base_entity")]
        public List<Guid> BaseEntities { get; set; }

        public VirtualBar() { }




        public VirtualBar(Point3d start, Point3d end, Vector3d yAxis, List<IStructureElement> elements, string identifier = "VB")
        {
            this.EntityCreated();

            Start = start;
            End = end;
            YAxis = yAxis;
            Identifier = identifier;
            SetBaseEntities(elements);
        }

        private void SetBaseEntities(List<IStructureElement> elements)
        {
            this.BaseEntities = new List<Guid>();

            foreach (IStructureElement element in elements)
            {
                if (element is Shells.Slab slab)
                {
                    BaseEntities.Add(slab.SlabPart.Guid);
                }
                else if (element is Bars.Bar bar)
                {
                    BaseEntities.Add(bar.BarPart.Guid);
                }
                else
                {
                    throw new NotImplementedException($"result point at {element.GetType()} has not been implemented");
                }
            }
        }
    }
}