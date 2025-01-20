using Microsoft.VisualStudio.TestTools.UnitTesting;
using FemDesign.Loads;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace FemDesign.Loads
{
    [TestClass()]
    public class LoadGroupTests
    {
        [TestMethod("Load group serialise/deserialise")]
        public void LoadGroupTest1()
        {
            var model = Model.DeserializeFromFilePath("Loads/Assets/load-group.struxml");

            var loadGroupTable = model.Entities.Loads.LoadGroupTable;

            var customTable = loadGroupTable.CustomTable;

            Assert.IsTrue(loadGroupTable.GeneralLoadGroups[0].ModelLoadGroupPermanent.Load_case.Count == 2);
            Assert.IsTrue(loadGroupTable.GeneralLoadGroups[1].ModelLoadGroupTemporary.Load_case.Count == 1);
            Assert.IsTrue(loadGroupTable.GeneralLoadGroups[2].AccidentalLoadGroup.Load_case.Count == 1);
            Assert.IsTrue(loadGroupTable.GeneralLoadGroups[3].StressLoadGroup.Load_case.Count == 1);

        }
    }
}