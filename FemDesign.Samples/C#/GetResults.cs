using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace FemDesign.Samples
{
    public partial class SampleProgram
    {
        private static void GetResults()
        {
            string csvPath1 = @"C:\Users\JohannaRiad\OneDrive - StruSoft AB\Documents\2. Eget presentationsmaterial\9. Stalbyggnadsdagen 2021\Hattbalk\pointsupportreactions.csv";
            var results1 = FemDesign.Results.ResultsReader.Parse(csvPath1);


            string csvPath2 = @"C:\Users\JohannaRiad\OneDrive - StruSoft AB\Documents\2. Eget presentationsmaterial\9. Stalbyggnadsdagen 2021\Hattbalk\barinternalforces.csv";
            var results2 = FemDesign.Results.ResultsReader.Parse(csvPath2);

            double a = 10;

        }
    }
}
