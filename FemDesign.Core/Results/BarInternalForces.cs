using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Globalization;
using System.Text.RegularExpressions;
using FemDesign.GenericClasses;


namespace FemDesign.Results
{
    /// <summary>
    /// FemDesign "Bars, Internal Forces" result
    /// </summary>
    public class BarInternalForces : IResult
    {
        /// <summary>
        /// Support name identifier
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Internal position, X
        /// </summary>
        public readonly double X;
        /// <summary>
        /// N
        /// </summary>
        public readonly double N;
        /// <summary>
        /// Local Ty'
        /// </summary>
        public readonly double Ty;
        /// <summary>
        /// Local Tz'
        /// </summary>
        public readonly double Tz;
        /// <summary>
        /// Mt
        /// </summary>
        public readonly double Mt;
        /// <summary>
        /// Local My'
        /// </summary>
        public readonly double My;
        /// <summary>
        /// Local Mz'
        /// </summary>
        public readonly double Mz;
        /// <summary>
        /// Force resultant
        /// </summary>

        public readonly string CaseIdentifier;

        internal BarInternalForces(string id,double x, double n, double ty, double tz, double mt, double my, double mz, string resultCase)
        {
            Id = id;
            X = x;
            N = n;
            Ty = ty;
            Tz = tz;
            Mt = mt;
            My = my;
            Mz = mz;
            CaseIdentifier = resultCase;
        }

        public override string ToString()
        {
            return $"{base.ToString()}, {Id}, {CaseIdentifier}";
        }

        internal static Regex IdentificationExpression
        {
            get
            {
                return new Regex(@"(?'type'Bars), (?'result'Internal forces), (?'loadcasetype'[\w\ ]+) - Load (?'casecomb'[\w\ ]+): (?'casename'[\w\ ]+)");
            }
        }

        internal static Regex HeaderExpression
        {
            get
            {
                return new Regex(@"(?'type'Bars), (?'result'Internal forces), (?'loadcasetype'[\w\ ]+) - Load (?'casecomb'[\w\ ]+): (?'casename'[\w\ ]+)|ID|\[.*\]");
            }
        }

        internal static BarInternalForces Parse(string[] row, CsvParser reader, Dictionary<string, string> HeaderData)
        {
            string barname = row[0];
            double x = Double.Parse(row[1], CultureInfo.InvariantCulture);
            double n = Double.Parse(row[2], CultureInfo.InvariantCulture);
            double ty = Double.Parse(row[3], CultureInfo.InvariantCulture);
            double tz = Double.Parse(row[4], CultureInfo.InvariantCulture);
            double mt = Double.Parse(row[5], CultureInfo.InvariantCulture);
            double my = Double.Parse(row[6], CultureInfo.InvariantCulture);
            double mz = Double.Parse(row[7], CultureInfo.InvariantCulture);
            string lc = HeaderData["casename"];
            return new BarInternalForces(barname, x, n, ty, tz, mt, my, mz, lc);
        }
    }
}
