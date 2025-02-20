﻿using Grasshopper.GUI.Canvas;

namespace FemDesign.Grasshopper.Components.UIWidgets
{
    public class WidgetRenderArgs
    {
        public GH_Canvas Canvas
        {
            get;
            private set;
        }
        public WidgetChannel Channel
        {
            get;
            private set;
        }
        public WidgetRenderArgs(GH_Canvas canvas, WidgetChannel channel)
        {
            Canvas = canvas;
            Channel = channel;
        }
    }
}
