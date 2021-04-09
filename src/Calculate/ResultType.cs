﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

#region dynamo
using Autodesk.DesignScript.Runtime;
#endregion

namespace FemDesign.Calculate
{
    [System.Serializable]
    [IsVisibleInDynamoLibrary(true)]
    public enum ResultType 
    {
        /* LOADCASES*/

        /// <summary>
        /// Bars, internal forces
        /// </summary>
        frCaseIntfBar_ListProc,

        /* LOADCOMBINATIONS*/

        /// <summary>
        /// Labelled sections, internal forces
        /// </summary>
        frCombIntfBarEnd_ListProc,
        frCombIntfResSection_ListProc,
    }
}