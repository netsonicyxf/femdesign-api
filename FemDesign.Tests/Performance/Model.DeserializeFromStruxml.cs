using Microsoft.VisualStudio.TestTools.UnitTesting;
using FemDesign;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Runtime.Serialization;
using System.Runtime.Serialization.Formatters.Binary;
using System.Reflection;

namespace FemDesign.Tests.Performance
{
    [TestClass()]
    public class ModelDeserializeFromStruxml
    {
        [TestInitialize]
        public void Warmup()
        {
            for (int i = 0; i < 100000; i++)
            {
                Math.Sqrt(5.0);
            }
        }

        [TestCategory("Performance"), TestMethod("very large model")]
        public void VeryLarge()
        {
            var path = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "OneDrive - StruSoft AB", "FEM-Design API", "Performance test files", "very_large_model.struxml");

            var time = Utils.Time(() => Model.DeserializeFromFilePath(path));

            Assert.IsTrue(time <= TimeSpan.FromSeconds(1.0), $"Time: {time.TotalSeconds:0.###}s");
        }

        [TestCategory("Performance"), TestMethod("large model")]
        public void Large()
        {
            var path = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "OneDrive - StruSoft AB", "FEM-Design API", "Performance test files", "large_model.struxml");

            var time = Utils.Time(() => Model.DeserializeFromFilePath(path));

            Assert.IsTrue(time <= TimeSpan.FromSeconds(0.5), $"Time: {time.TotalSeconds:0.###}s");
        }

        [TestCategory("Performance"), TestMethod("small model")]
        public void Small()
        {
            var path = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.UserProfile), "OneDrive - StruSoft AB", "FEM-Design API", "Performance test files", "small_model.struxml");
            var time = Utils.Time(() => Model.DeserializeFromFilePath(path));

            Assert.IsTrue(time <= TimeSpan.FromSeconds(0.1), $"Time: {time.TotalSeconds:0.###}s");
        }
    }
}
