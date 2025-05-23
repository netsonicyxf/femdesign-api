namespace FemDesign
{
    /// <summary>
    /// Contains double restrictions used for property definitions.
    /// 
    /// Restrictions are defined by strusoft.xsd
    /// </summary>
    internal class RestrictedDouble
    {
        /// <summary>
        /// Check if val in range (min, max)
        /// </summary>
        internal static double ValueInClosedInterval(double val, double min, double max)
        {
            if (val >= min && val <= max)
            {
                return val;
            }
            else
            {
                throw new System.ArgumentOutOfRangeException($"Value should be between or equal to {min} and {max}");
            }
        }

        /// <summary>
        /// Check if val is larger than min and smaller than max
        /// </summary>
        internal static double ValueInOpenInterval(double val, double min, double max)
        {
            if (val > min && val < max)
            {
                return val;
            }
            else
            {
                throw new System.ArgumentOutOfRangeException($"Value should be between {min} and {max}");
            }
        }

        /// <summary>
        /// Check if val is larger or equal to min and smaller than max
        /// </summary>
        internal static double ValueInHalfOpenInterval(double val, double min, double max)
        {
            if (val >= min && val < max)
            {
                return val;
            }
            else
            {
                throw new System.ArgumentOutOfRangeException($"Value should be larger or equal to {min} and smaller than {max}");
            }
        }

        /// <summary>
        /// Check if val is larger than min and smaller or equal to max
        /// </summary>
        internal static double ValueInHalfClosedInterval(double val, double min, double max)
        {
            if (val > min && val <= max)
            {
                return val;
            }
            else
            {
                throw new System.ArgumentOutOfRangeException($"Value should be larger than {min} and smaller or equal to {max}");
            }
        }

        /// <summary>
        /// Check if val is positive
        /// </summary>
        internal static double Positive(double val)
        {
            if (val > 0)
            {
                return val;
            }
            else
            {
                throw new System.ArgumentOutOfRangeException("Value should be positive");
            }
        }

        /// <summary>
        /// abs_max_1000
        /// </summary>
        internal static double AbsMax_1000(double val)
        {
            double max = 1000;
            return RestrictedDouble.ValueInClosedInterval(val, -max, max);
        }

        /// <summary>
        /// abs_max_10000
        /// </summary>
        internal static double AbsMax_10000(double val)
        {
            double max = 10000;
            return RestrictedDouble.ValueInClosedInterval(val, -max, max);
        }

        /// <summary>
        /// abs_max_1e20
        /// </summary>
        internal static double AbsMax_1e20(double val)
        {
            // align_offset

            double max = 1E20;
            return RestrictedDouble.ValueInClosedInterval(val, -max, max);
        }

        /// <summary>
        /// non_neg_max_1, position_type, reduction_factor_type, orthotropy_type
        /// </summary>
        internal static double NonNegMax_1(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1);
        }

        /// <summary>
        /// non_neg_max_5
        /// </summary>
        internal static double NonNegMax_5(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 5);
        }

        /// <summary>
        /// non_neg_max_10
        /// </summary>
        internal static double NonNegMax_10(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 10);
        }
        
        /// <summary>
        /// non_zero_max_10_1
        /// </summary>
        internal static double NonZeroMax_10_1(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0.02, 10);
        }

        /// <summary>
        /// non_zero_max_10_1
        /// </summary>
        internal static double NonZeroMax_10_2(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0.03, 10);
        }

        /// <summary>
        /// non_zero_max_10_1
        /// </summary>
        internal static double PositiveMax_1000(double val)
        {
            return RestrictedDouble.ValueInHalfClosedInterval(val, 0, 1000);
        }

        /// <summary>
        /// non_neg_max_20
        /// </summary>
        internal static double NonNegMax_20(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 20);
        }

        /// <summary>
        /// non_neg_max_90
        /// </summary>
        internal static double NonNegMax_90(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 90);
        }

        /// <summary>
        /// non_neg_max_100
        /// </summary>
        internal static double NonNegMax_100(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 100);
        }

        /// <summary>
        /// non_neg_max_1000
        /// </summary>
        internal static double NonNegMax_1000(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1000);
        }

        /// <summary>
        /// non_neg_max_10000
        /// </summary>
        internal static double NonNegMax_10000(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 10000);
        }

        /// <summary>
        /// non_neg_max_1e15
        /// </summary>
        internal static double NonNegMax_1e5(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1E5);
        }

        /// <summary>
        /// non_neg_max_1e7
        /// </summary>
        internal static double NonNegMax_1e7(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1E7);
        }

        /// <summary>
        /// non_neg_max_1e10
        /// </summary>
        internal static double NonNegMax_1e10(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1E10);
        }

        /// <summary>
        /// non_neg_max_1e15
        /// </summary>
        internal static double NonNegMax_1e15(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1E15);
        }

        /// <summary>
        /// Checks if the value is a positive, non-zero number that is no greater than 1e15.
        /// </summary>
        internal static double NonZeroMax_1e15(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 1E-5, 1E15);
        }

        /// <summary>
        /// non_neg_max_1e20
        /// </summary>
        internal static double NonNegMax_1e20(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1E20);
        }

        /// <summary>
        /// Checks if the value is a positive, non-zero number that is no greater than 1e20.
        /// </summary>
        internal static double NonZeroMax_1e20(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 1E-5, 1E20);
        }

        /// <summary>
        /// non_neg_max_1e30
        /// </summary>
        internal static double NonNegMax_1e30(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1E30);
        }

        /// <summary>
        /// Checks if the value is a positive, non-zero number that is no greater than 1e30.
        /// </summary>
        internal static double NonZeroMax_1e30(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 1E-5, 1E30);
        }

        /// <summary>
        /// Check if val in range [90.0, 180.0]
        /// </summary>
        internal static double MeshMaxAngle(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 90, 180);
        }

        /// <summary>
        /// Check if val in range [2.0, 500.0]
        /// </summary>
        internal static double MeshMaxRatio(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 2, 500);
        }

        /// <summary>
        /// material_base_value
        /// </summary>
        internal static double MaterialBaseValue(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 3.403E38);
        }

        /// <summary>
        /// material_nu_value
        /// </summary>
        internal static double MaterialNuValue(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 0.499);
        }

        /// <summary>
        /// one_quadrant
        /// </summary>
        internal static double OneQuadrantRadians(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1.5707963267949);
        }

        /// <summary>
        /// one_quadrant, degree specific
        /// </summary>
        internal static double OneQuadrantDegrees(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 90);
        }

        /// <summary>
        /// two_quadrants
        /// </summary>
        internal static double TwoQuadrantsRadians(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 3.14159265358979);
        }

        /// <summary>
        /// two_quadrants, degree specific
        /// </summary>
        internal static double TwoQuadrantsDegrees(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 180);
        }

        /// <summary>
        /// abs_two_quadrants
        /// </summary>
        internal static double AbsTwoQuadrants(double val)
        {
            double max = 3.14159265358979;
            return RestrictedDouble.ValueInClosedInterval(val, -max, max);
        }

        /// <summary>
        /// position_type
        /// </summary>
        internal static double PositionType(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0, 1);
        }

        /// <summary>
        /// rc_diameter_value
        /// </summary>
        internal static double RcDiameterValue(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0.001, 0.1);
        }

        /// <summary>
        /// rc_k_value
        /// </summary>
        internal static double RcKValue(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 1.05, 1E10);
        }

        /// <summary>
        /// timber_panel_thickness
        /// </summary>
        internal static double TimberPanelThickness(double val)
        {
            return RestrictedDouble.ValueInClosedInterval(val, 0.001, 100.0);
        }
    }
}