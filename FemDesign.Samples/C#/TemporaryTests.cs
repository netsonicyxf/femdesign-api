using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace FemDesign.Samples
{
    public partial class SampleProgram
    {
        private static void TemporaryTests()
        {
            string struxmlPath = @"C:\Users\JohannaRiad\OneDrive - StruSoft AB\Desktop\example_walls.struxml";
            string struxmlPathOut = @"C:\Users\JohannaRiad\OneDrive - StruSoft AB\Desktop\example_walls_CB.struxml";
            Model model = Model.DeserializeFromFilePath(struxmlPath);
            FemDesign.Shells.Slab baseShell = model.Entities.Slabs.FirstOrDefault();
            Geometry.RectangleType rectangle = new Geometry.RectangleType() { 
                BaseCorner = new Geometry.FdPoint3d(1, 0, 7),
                DimX = 1,
                DimY = 0.5,
                LocalX = baseShell.SlabPart.LocalX,
                LocalY = baseShell.SlabPart.LocalY
            };

            Reinforcement.HiddenBar hiddenBar = new Reinforcement.HiddenBar(baseShell, rectangle);

            model.Entities.HiddenBars.Add(hiddenBar);
            model.SerializeModel(struxmlPathOut);

        }
    }
}