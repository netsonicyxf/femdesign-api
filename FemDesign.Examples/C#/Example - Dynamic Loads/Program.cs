﻿using System;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using FemDesign;
using FemDesign.Calculate;
using FemDesign.GenericClasses;
using FemDesign.Geometry;
using FemDesign.Loads;
using FemDesign.Materials;
using FemDesign.ModellingTools;
using FemDesign.Shells;
using FemDesign.Utils;

namespace FemDesign.Examples
{
    internal class Program
    {
        static void Main()
        {

            var diagram1 = new Diagram("diagram1", new List<double> { 0.0, 1, 2}, new List<double> { 1, 0.1, 0.3});
            var diagram2 = new Diagram("diagram2", new List<double> { 0.0, 0.1, 0.2}, new List<double> { 1, 0.1, 0.3});

            var loadCase1 = new LoadCase("name", LoadCaseType.DeadLoad, LoadCaseDuration.Permanent);
            var loadCase2 = new LoadCase("name2", LoadCaseType.Static, LoadCaseDuration.Permanent);

            var exLdCase1 = new ExcitationForceLoadCase(loadCase1, 1, diagram1);
            var exLdCase2 = new ExcitationForceLoadCase(loadCase2, 2, diagram2);

            var combination1 = new ExcitationForceCombination()
            {
                Name = "combo1",
                dT = 0.01,
                records = new List<ExcitationForceLoadCase> { exLdCase1 }
            };

            var combination2 = new ExcitationForceCombination()
            {
                Name = "combo2",
                dT = 0.02,
                records = new List<ExcitationForceLoadCase> { exLdCase1, exLdCase2 }
            };

            var excitationForce = new Loads.ExcitationForce()
            {
                Diagram = new List<Diagram> { diagram1, diagram2 },
                Combination = new List<ExcitationForceCombination> {  combination1, combination2},
            };

            var model = new Model(Country.COMMON);

            model.Entities.Loads.ExcitationForce = excitationForce;

            // TODO
            // model.AddExcitationForce(combination1, combination2)

            model.Entities.Loads.LoadCases.Add(loadCase1);
            model.Entities.Loads.LoadCases.Add(loadCase2);
            model.Entities.Loads.LoadCases.Add(loadCase2);

            using(var femdesign = new FemDesignConnection(keepOpen: true))
            {
                femdesign.Open(model);
            }
        }
    }
}