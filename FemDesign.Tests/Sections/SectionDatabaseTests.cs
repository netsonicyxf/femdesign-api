using Microsoft.VisualStudio.TestTools.UnitTesting;
using FemDesign.Sections;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;
using System.Text.RegularExpressions;
using FuzzySharp;


namespace FemDesign.Sections
{
    [TestClass()]
    public class SectionDatabaseTests
    {
        [TestMethod("SectionDatabase.GetDefault - Speed")]
        [TestCategory("Performance")]
        public void GetDefaultTest()
        {
            Stopwatch sw = new Stopwatch();

            sw.Start();
            SectionDatabase.GetDefault();
            sw.Stop();
            Assert.IsTrue(sw.ElapsedMilliseconds < 500, $"GetDefault once should be fast. {sw.ElapsedMilliseconds}");

            sw.Restart();
            for (int i = 0; i < 10; i++)
                SectionDatabase.GetDefault();
            sw.Stop();
            Assert.IsTrue(sw.ElapsedMilliseconds < 100, $"GetDefault many times after the first should be very fast. {sw.ElapsedMilliseconds}");
        }


        [TestCategory("FEM-Design required")]
        [TestMethod("Fuzzy Search")]
        public void TestFuzzySearch()
        {
            var db = SectionDatabase.GetDefault();

            var section1 = db.SectionByName("HEA100");
            var targetName = "Steel section, HE-A, 100";
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("HEA-100");
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("HEA_100");
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("HEA100");
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("Steel section, HE-A, 100");
            Assert.IsTrue(section1.Name == targetName);



            section1 = db.SectionByName("CHS 323.9-8.8");
            targetName = "Steel section, CHS, 323.9-8.8";
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("CHS 323.9/8.8");
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("CHS, 323.9-8.8");
            Assert.IsTrue(section1.Name == targetName);

            //Timber section, Rectangle, 66x225
            section1 = db.SectionByName("Timber section, Rectangle, 66x225");
            targetName = "Timber section, Rectangle, 66x225";
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("Rectangle 66x225");
            Assert.IsTrue(section1.Name == targetName);

            section1 = db.SectionByName("Timber 66x225");
            Assert.IsTrue(section1.Name == targetName);


        }
    }
}