using GH_IO.Serialization;
using Grasshopper;
using Grasshopper.GUI;
using Grasshopper.GUI.Canvas;
using Grasshopper.Kernel;

using System;
using System.Diagnostics;
using System.Reflection;
using System.Threading;
using System.Windows.Forms;

namespace FemDesign.Grasshopper.UI
{
    public class MenuLoad
    {
        private static string documentationUrl = "https://femdesign-api-docs.onstrusoft.com";
        private static string supportUrl = "https://strusoft.freshdesk.com";
        private static string communityUrl = "https://femdesign.discourse.group/";
        private static string gitHubUrl = "https://github.com/strusoft/femdesign-api";

        private static ToolStripMenuItem fdMenu;

        internal static void OnStartup(GH_Canvas canvas)
        {
            fdMenu = new ToolStripMenuItem("FEM-Design")
            {
                Name = "FEM-Design",
            };

            PopulateSub(fdMenu);

            GH_DocumentEditor editor = null;

            while (editor == null)
            {
                editor = Grasshopper.Instances.DocumentEditor;
                Thread.Sleep(321);
            }

            if (!editor.MainMenuStrip.Items.ContainsKey("FEM-Design"))
            {
                editor.MainMenuStrip.Items.Add(fdMenu);
            }
            else
            {
                fdMenu = (ToolStripMenuItem)editor.MainMenuStrip.Items["FEM-Design"];
                lock (fdMenu)
                {
                    fdMenu.DropDown.Items.Add(new ToolStripSeparator());
                    PopulateSub(fdMenu);
                }
            }

            Grasshopper.Instances.CanvasCreated -= OnStartup;
        }

        private static void PopulateSub(ToolStripMenuItem menuItem)
        {
            menuItem.DropDown.Items.Add("Documentation", Properties.Resources.FEM_Connection,
                (sender, e) => OpenBrowser(sender, e, documentationUrl));

            menuItem.DropDown.Items.Add(
                "Community", Properties.Resources.FEM_Connection,
                (sender, e) => OpenBrowser(sender, e, communityUrl));

            menuItem.DropDown.Items.Add(
                "Support", Properties.Resources.FEM_Connection,
                (sender, e) => OpenBrowser(sender, e, supportUrl));

            menuItem.DropDown.Items.Add(
                "GitHub", Properties.Resources.FEM_Connection,
                (sender, e) => OpenBrowser(sender, e, gitHubUrl));
        }

        // event handler that opens up a sub-window
        private static void OpenForm(object sender, System.EventArgs e)
        {
            // write content here...
        }

        // event handler that opens up a browser window
        private static void OpenBrowser(object sender, System.EventArgs e, string url)
        {
            Process.Start(new ProcessStartInfo { FileName = url, UseShellExecute = true });
        }

        // event handler that opens up a Grasshopper example document 
        private static void OpenExample(object sender, EventArgs e, string fileName, string exampleFolder)
        {
            string assemblyPath = Assembly.GetExecutingAssembly().Location;
            string folderAssembly = System.IO.Path.GetDirectoryName(assemblyPath);
            string examplesDir = exampleFolder is null
                ? System.IO.Path.Combine(folderAssembly, "Files", "Examples")
                : System.IO.Path.Combine(folderAssembly, "Files", "Examples", exampleFolder);

            // Make this folder discoverable to GH
            Grasshopper.Instances.Settings.SetValue("FEMDESIGN_BASEDIR", examplesDir);
            Rhino.RhinoDoc.ActiveDoc?.Strings.SetString("FEMDESIGN_BASEDIR", examplesDir);

            fileName = fileName + ".gh";
            string exampleFile = System.IO.Path.Combine(examplesDir, fileName);

            PasteGrasshopperFile(exampleFile);
        }

        private static void PasteGrasshopperFile(string filePath)
        {
            GH_Document currentDoc = Grasshopper.Instances.ActiveCanvas.Document;
            if (currentDoc == null)
            {
                MessageBox.Show("No active Grasshopper document found.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                return;
            }

            GH_Archive archive = new GH_Archive();
            archive.ReadFromFile(filePath);

            GH_Document newDoc = new GH_Document();
            if (archive.ExtractObject(newDoc, "Definition"))
            {
                currentDoc.MergeDocument(newDoc);
                Grasshopper.Instances.ActiveCanvas.Refresh();
                Grasshopper.Instances.ActiveCanvas.Update();
            }
            else
            {
                MessageBox.Show("Failed to extract the Grasshopper document from the archive.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}