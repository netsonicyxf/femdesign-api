// https://strusoft.com/
using FemDesign.GenericClasses;
using System;
using System.Xml.Serialization;

namespace FemDesign.Calculate
{
    /// <summary>
    /// fdscript.xsd
    /// </summary>
    public partial class Bedding
    {
        [XmlAttribute("Ldcomb")]
        public string LdCombChar { get; set; }

        [XmlAttribute("Meshprep")]
        public int _meshPrep = 0;
        [XmlIgnore]
        public MeshPrep MeshPrep
        {
            get
            {
                return (MeshPrep)_meshPrep;
            }
            set
            {
                this._meshPrep = (int)value;
            }
        }

        [XmlAttribute("Stiff_X")]
        public double StiffX { get; set; } = 0.5;

        [XmlAttribute("Stiff_Y")]
        public double StiffY { get; set; } = 0.5;

        private Bedding()
        {
        }

        public Bedding(string ldCombChar, MeshPrep meshPrep, double stiffX, double stiffY)
        {
            this.LdCombChar = ldCombChar;
            this.MeshPrep = meshPrep;
            this.StiffX = stiffX;
            this.StiffY = stiffY;
        }

        public static Bedding Default()
        {
            return new Bedding
            {
                StiffX = 0.5,
                StiffY = 0.5,
                MeshPrep = MeshPrep.ActualMesh,
            };
        }
    }

    public enum MeshPrep
    {
        [Parseable("ActualMesh")]
        ActualMesh = 0,
        [Parseable("FactoryDefault")]
        FactoryDefault = 1,
    }
}
