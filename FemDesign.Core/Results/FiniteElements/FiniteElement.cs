using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

#if ISDYNAMO
using Autodesk.DesignScript.Runtime;
#endif

namespace FemDesign.Results
{
    public partial class FiniteElement
    {
        /// <summary>
        /// Fea Nodes Object
        /// </summary>
        public List<FemNode> FemNode { get; set; }

        /// <summary>
        /// Fea Bar Object
        /// </summary>
        public List<FemBar> FemBar { get; set; }

        /// <summary>
        /// Fea Shell Object
        /// </summary>
        public List<FemShell> FemShell { get; set; }

        /// <summary>
        /// Point connection elements
        /// </summary>
        public List<PointConnectionElement> FemPointConnection { get; set; }

        /// <summary>
        /// Line connection elements
        /// </summary>
        public List<LineConnectionElement> FemLineConnection { get; set; }

        /// <summary>
        /// Point connection elements
        /// </summary>
        public List<PointSupportElement> FemPointSupport { get; set; }

        /// <summary>
        /// Line connection elements
        /// </summary>
        public List<LineSupportElement> FemLineSupport { get; set; }

        internal FiniteElement() { }

        public FiniteElement(List<FemNode> femNode, List<FemBar> femBar, List<FemShell> femShell)
        {
            this.FemNode = femNode;
            this.FemBar = femBar;
            this.FemShell = femShell;
        }
    }
}