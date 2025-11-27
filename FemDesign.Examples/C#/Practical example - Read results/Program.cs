using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using FemDesign;
using FemDesign.Calculate;

namespace FemDesign.Examples
{
    internal class Program
    {
        static void Main(string[] args)
        {

            var connection = new FemDesignConnection();
            connection.Open("model_mix.struxml");

            var analysis = Analysis.StaticAnalysis();
            connection.RunAnalysis(analysis);


            var ndLoadCase = connection.GetLoadCaseResults<Results.NodalDisplacement>();
            var ndLoadComb = connection.GetLoadCombinationResults<Results.NodalDisplacement>();

            Console.WriteLine("Done!");



        }
    }
}
