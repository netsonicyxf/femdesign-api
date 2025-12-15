using GH_IO.Serialization;
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
        private static ToolStripMenuItem simplexMenu;

        internal static void OnStartup(GH_Canvas canvas)
        {
            simplexMenu = new ToolStripMenuItem("Simplex")
            {
                Name = "Simplex",
            };

            PopulateSub(simplexMenu);

            GH_DocumentEditor editor = null;

            while (editor == null)
            {
                editor = Grasshopper.Instances.DocumentEditor;
                Thread.Sleep(321);
            }

            if (!editor.MainMenuStrip.Items.ContainsKey("Simplex"))
            {
                editor.MainMenuStrip.Items.Add(simplexMenu);
            }
            else
            {
                simplexMenu = (ToolStripMenuItem)editor.MainMenuStrip.Items["Simplex"];
                lock (simplexMenu)
                {
                    simplexMenu.DropDown.Items.Add(new ToolStripSeparator());
                    PopulateSub(simplexMenu);
                }
            }

            Grasshopper.Instances.CanvasCreated -= OnStartup;
        }

        private static void PopulateSub(ToolStripMenuItem menuItem)
        {
            // Add Login
            menuItem.DropDown.Items.Add(
                "Login",
                SimplexGh.Properties.Resources.SimplexIconBlue,
                OpenForm);

            menuItem.DropDown.Items.Add(new ToolStripSeparator());
            //----------------------------------------------------

            // Add Documentation
            menuItem.DropDown.Items.Add("Documentation", SimplexGh.Properties.Resources.SimplexIconBlue,
                (sender, e) => OpenBrowser(sender, e, "https://simplex-docs.onstrusoft.com/api/grasshopper/get-started"));

            // Add Examples (submenu)
            var exampleSubMenu = new ToolStripMenuItem("&Examples");

            var templateItem = new ToolStripMenuItem(
                "&Simplex Foundation template",
                SimplexGh.Properties.Resources.SimplexIconBlue,
                (sender, e) => OpenExample(sender, e, "SimplexFoundationTemplate", null)
                );
            templateItem.ShortcutKeys = Keys.Control | Keys.Shift | Keys.T;
            templateItem.ShowShortcutKeys = true;
            exampleSubMenu.DropDown.Items.Add(templateItem);

            exampleSubMenu.DropDown.Items.Add(
                "Excel & Simplex connection",
                SimplexGh.Properties.Resources.SimplexIconBlue,
                (sender, e) => OpenExample(sender, e, "ExcelSxConnectionExample", "ExcelSxConnectionExample")
                );

            exampleSubMenu.DropDown.Items.Add(
                "FEM-Design & Simplex connection",
                SimplexGh.Properties.Resources.SimplexIconBlue,
                (sender, e) => OpenExample(sender, e, "FDSxConnectionExample", "FDSxConnectionExample")
                );

            menuItem.DropDown.Items.Add(exampleSubMenu);

            menuItem.DropDown.Items.Add(new ToolStripSeparator());
            //----------------------------------------------------

            // Add Help
            menuItem.DropDown.Items.Add(
                "Help",
                SimplexGh.Properties.Resources.SimplexIconBlue,
                (sender, e) => OpenBrowser(sender, e, "https://strusoft.freshdesk.com/en/support/tickets/new")
                );
        }

        // event handler that opens up a sub-window
        private static void OpenForm(object sender, System.EventArgs e)
        {
            new Form1().ShowDialog();
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
            Grasshopper.Instances.Settings.SetValue("SIMPLEX_BASEDIR", examplesDir);
            Rhino.RhinoDoc.ActiveDoc?.Strings.SetString("SIMPLEX_BASEDIR", examplesDir);

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