using System;
using System.IO;
using System.IO.Compression;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Net;
using System.Net.Http;
using Octokit;

namespace FemDesign.Installer
{
    public partial class MainWindow : Form
    {
        private GitHubClient GithubClient;
        private Dictionary<int, Release> Releases = new Dictionary<int, Release>();

        public MainWindow()
        {
            InitializeComponent();

            this.GithubClient = new GitHubClient(new ProductHeaderValue("StruSoft-femdesign-api-FemDesign.Installer"));

            UpdateReleaseList();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            UpdateReleaseList();
        }

        private async void UpdateReleaseList()
        {
            VersionSelector.Items.Clear();
            Releases.Clear();

            var releases = await GithubClient.Repository.Release.GetAll("StruSoft", "femdesign-api");

            VersionSelector.Items.AddRange(releases
                .Where(r => !r.Prerelease || IncludePreReleaseCheckBox.Checked)
                .Select(r => (object)$"{r.TagName} - {r.Name}")
                .ToArray()
                );
            Releases = releases.ToDictionary(r => r.Id);

            if (VersionSelector.SelectedIndex < 0)
                VersionSelector.SelectedIndex = 0;

        }

        private async void DownloadButton_Click(object sender, EventArgs e)
        {
            var selected = (string)VersionSelector.SelectedItem;

            Release selectedRelease = Releases.Values.First(r => $"{r.TagName} - {r.Name}" == selected);

            // Download FemDesign.Grasshopper
            ReleaseAsset femdesignGrasshopper = selectedRelease.Assets.FirstOrDefault(a => a.Name == "FemDesign.Grasshopper.zip");
            if (GrasshopperCheckBox.Checked && femdesignGrasshopper != null)
            {
                string GrasshopperInstallDirectory = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Grasshopper", "Libraries", "FemDesign");
                string path = await Download(femdesignGrasshopper.BrowserDownloadUrl, GrasshopperInstallDirectory);
                UnzipInDirectory(path);
                textBox1.AppendText($"Installed {femdesignGrasshopper.Name.Replace(".zip", "")} - {selectedRelease.TagName}" + Environment.NewLine);
            }

            // Download FemDesign.Dynamo
            ReleaseAsset femdesignDynamo = selectedRelease.Assets.FirstOrDefault(a => a.Name == "FemDesign.Dynamo.zip");
            if (DynamoCheckBox.Checked && femdesignDynamo != null)
            {
                //string DynamoInstallDirectory = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Dynamo", , "FemDesign");
                //string path = await Download(femdesignDynamo.BrowserDownloadUrl, DynamoInstallDirectory);
                //Unzip(path);
            }
        }

        private void VersionSelector_SelectedIndexChanged(object sender, EventArgs e)
        {
            ComboBox comboBox = (ComboBox)sender;
        }

        public static async Task<string> Download(string url, string directory)
        {
            var client = new HttpClient();
            var response = await client.GetAsync(url);
            var bytes = await response.Content.ReadAsByteArrayAsync();
            var fileName = response.Content.Headers.ContentDisposition.FileName;
            var path = Path.Combine(directory, fileName);
            if (File.Exists(path))
                File.Delete(path);

            using (var stream = new FileStream(path, System.IO.FileMode.CreateNew, FileAccess.Write))
            {
                await stream.WriteAsync(bytes, 0, bytes.Length);
            }
            return path;
        }

        public void UnzipInDirectory(string zipPath)
        {
            string directory = Path.GetDirectoryName(zipPath);

            // Delete files before extracting
            using (var zip = ZipFile.OpenRead(zipPath))
            foreach (var entry in zip.Entries)
            {
                var path = Path.Combine(directory, entry.FullName);
                if (File.Exists(path))
                    File.Delete(path);
            }
            ZipFile.ExtractToDirectory(zipPath, directory, Encoding.UTF8);
            File.Delete(zipPath);
        }

        private void IncludePreReleaseCheckBox_CheckedChanged(object sender, EventArgs e)
        {
            UpdateReleaseList();
        }
    }
}
