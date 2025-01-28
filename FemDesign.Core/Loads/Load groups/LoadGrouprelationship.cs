using FemDesign.GenericClasses;
using System.Xml.Serialization;

namespace FemDesign.Loads
{
    /// <summary>
    /// Used for keeping track of the relationsship of the load cases in a group
    /// </summary>
    [System.Serializable]
    public enum ELoadGroupRelationship
    {
        /// <summary> If all cases are to be applied mutually exclusive </summary>
        [Parseable("alternative", "Alternative", "ALTERNATIVE", "0")]
        [XmlEnum("alternative")]
        Alternative,

        /// <summary> If all cases are to be applied simultaneously</summary>
        [Parseable("simultaneous", "Simultaneous", "SIMULTANEOUS","1")]
        [XmlEnum("simultaneous")]
        Simultaneous,

        /// <summary> If all cases are to be applied together </summary>
        [Parseable("entire", "Entire", "ENTIRE", "2")]
        [XmlEnum("entire")]
        Entire,

        /// <summary> Custom combination pattern</summary>
        [Parseable("custom", "Custom", "CUSTOM", "3")]
        [XmlEnum("custom")]
        Custom,
    }
}