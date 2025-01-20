// https://strusoft.com/

using System.Xml.Serialization;
using System.Collections.Generic;
using FemDesign.GenericClasses;
using StruSoft.Interop.StruXml.Data;

namespace FemDesign.Loads
{
    /// <summary>
    /// permanent_load_group (child of general_load_group)
    /// </summary>
    [System.Serializable]
    public partial class LoadGroupPermanent: LoadGroupBase
    {
        [XmlAttribute("standard_favourable")]
        public double StandardFavourable { get; set; }
        [XmlAttribute("standard_unfavourable")]
        public double StandardUnfavourable { get; set; }
        [XmlAttribute("xi")]
        public double _xi;
        [XmlIgnore]
        public double Xi
        {
            get
            {
                return this._xi;
            }
            set
            {
                this._xi = RestrictedDouble.NonNegMax_10(value);
            }
        }
        [XmlAttribute("accidental_favourable")]
        public double AccidentalFavourable { get; set; }
        [XmlAttribute("accidental_unfavourable")]
        public double AccidentalUnfavourable { get; set; }

        [XmlElement(ElementName = "custom_table", Order = 1)]
        public PermanentGroupRecord CustomTable { get; set; }
        /// <summary>
        /// ONLY FOR DESERIALIZATION
        /// NEEDS TO BE FIXED
        /// </summary>
        [XmlElement("load_case", Order = 2)]
        public List<Reference_type> Load_case { get; set; }

        [XmlElement("load_case", Order = 3)]
        public new List<ModelLoadCaseInGroup> ModelLoadCase { get; set; }


        /// <summary>
        /// parameterless constructor for serialization
        /// </summary>
        private LoadGroupPermanent() { }

        /// <summary>
        /// Public constructor.
        /// </summary>
        /// <param name="standardFavourable">Safety factor for favourable load.</param>
        /// <param name="standardUnfavourable">Safety factor for unfavourable load.</param>
        /// <param name="accidentalFavourable">Safety factor for favourable load for accidental load combinations.</param>
        /// <param name="accidentalUnfavourable">Safety factor for unfavourable load for accidental load combinations.</param>
        /// <param name="loadCases">List of load cases in the load group</param>
        /// <param name="relationsship">Specifies how to condider the load cases in combinations</param>
        /// <param name="xi">Xi-factor used in the combinations, see EN 1990.</param>
        /// <param name="name"></param>
        public LoadGroupPermanent(double standardFavourable, 
                                       double standardUnfavourable, double accidentalFavourable,
                                       double accidentalUnfavourable, List<LoadCase> loadCases, 
                                       ELoadGroupRelationship relationsship, double xi, string name)
        {
            this.Name = name;
            this.StandardFavourable = standardFavourable;
            this.StandardUnfavourable = standardUnfavourable;
            this.AccidentalFavourable = accidentalFavourable;
            this.AccidentalUnfavourable = accidentalUnfavourable;
            this.Relationship = relationsship;
            this.Xi = xi;

            //this.ModelLoadCase = new List<ModelLoadCaseInGroup>();
            for (int i = 0; i < loadCases.Count; i++)
            {
                AddLoadCase(loadCases[i]);
            }
        }
    }

    [System.Serializable]
    public class PermanentGroupRecord
    {
        [XmlElement("record")]
        public List<StruSoft.Interop.StruXml.Data.Permanent_load_groupRecord> Record { get; set; }

        public PermanentGroupRecord()
        {
        }
    }

}