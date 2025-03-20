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
        public MeshPrep meshPrep { get; set; } = MeshPrep.FactoryDefault;

        [XmlAttribute("Stiff_x")]
        public double StiffX { get; set; } = 0.5;

        [XmlAttribute("Stiff_y")]
        public double StiffY { get; set; } = 0.5;

        private Bedding()
        {
        }

        public Bedding(string ldCombChar, MeshPrep meshPrep, double stiffX, double stiffY)
        {
            this.LdCombChar = ldCombChar;
            this.meshPrep = meshPrep;
            this.StiffX = stiffX;
            this.StiffY = stiffY;
        }

        public static Bedding Default()
        {
            return new Bedding
            {
                StiffX = 0.5,
                StiffY = 0.5,
                meshPrep = MeshPrep.FactoryDefault,
            };
        }
    }

    public enum MeshPrep
    {
        [Parseable("FactoryDefault")]
        FactoryDefault = 0,
        [Parseable("ActualMesh")]
        ActualMesh = 1,
    }
}
