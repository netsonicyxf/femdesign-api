
namespace FemDesign.Installer
{
    partial class MainWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.RefreshButton = new System.Windows.Forms.Button();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.VersionSelector = new System.Windows.Forms.ComboBox();
            this.DownloadButton = new System.Windows.Forms.Button();
            this.GrasshopperCheckBox = new System.Windows.Forms.CheckBox();
            this.DynamoCheckBox = new System.Windows.Forms.CheckBox();
            this.IncludePreReleaseCheckBox = new System.Windows.Forms.CheckBox();
            this.SuspendLayout();
            // 
            // RefreshButton
            // 
            this.RefreshButton.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
            this.RefreshButton.Location = new System.Drawing.Point(392, 56);
            this.RefreshButton.Name = "RefreshButton";
            this.RefreshButton.Size = new System.Drawing.Size(21, 23);
            this.RefreshButton.TabIndex = 0;
            this.RefreshButton.Text = "⟳";
            this.RefreshButton.UseVisualStyleBackColor = true;
            this.RefreshButton.Click += new System.EventHandler(this.button1_Click);
            // 
            // textBox1
            // 
            this.textBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) 
            | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.textBox1.Location = new System.Drawing.Point(35, 156);
            this.textBox1.Multiline = true;
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(378, 224);
            this.textBox1.TabIndex = 1;
            // 
            // VersionSelector
            // 
            this.VersionSelector.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.VersionSelector.FormattingEnabled = true;
            this.VersionSelector.Items.AddRange(new object[] {
            "Item1",
            "Item2",
            "Item3"});
            this.VersionSelector.Location = new System.Drawing.Point(35, 56);
            this.VersionSelector.Name = "VersionSelector";
            this.VersionSelector.Size = new System.Drawing.Size(351, 21);
            this.VersionSelector.TabIndex = 2;
            this.VersionSelector.SelectedIndexChanged += new System.EventHandler(this.VersionSelector_SelectedIndexChanged);
            // 
            // DownloadButton
            // 
            this.DownloadButton.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) 
            | System.Windows.Forms.AnchorStyles.Right)));
            this.DownloadButton.Location = new System.Drawing.Point(35, 111);
            this.DownloadButton.Name = "DownloadButton";
            this.DownloadButton.Size = new System.Drawing.Size(378, 39);
            this.DownloadButton.TabIndex = 3;
            this.DownloadButton.Text = "Install";
            this.DownloadButton.UseVisualStyleBackColor = true;
            this.DownloadButton.Click += new System.EventHandler(this.DownloadButton_Click);
            // 
            // GrasshopperCheckBox
            // 
            this.GrasshopperCheckBox.AutoSize = true;
            this.GrasshopperCheckBox.Checked = true;
            this.GrasshopperCheckBox.CheckState = System.Windows.Forms.CheckState.Checked;
            this.GrasshopperCheckBox.Location = new System.Drawing.Point(35, 83);
            this.GrasshopperCheckBox.Name = "GrasshopperCheckBox";
            this.GrasshopperCheckBox.Size = new System.Drawing.Size(86, 17);
            this.GrasshopperCheckBox.TabIndex = 4;
            this.GrasshopperCheckBox.Text = "Grasshopper";
            this.GrasshopperCheckBox.UseVisualStyleBackColor = true;
            // 
            // DynamoCheckBox
            // 
            this.DynamoCheckBox.AutoSize = true;
            this.DynamoCheckBox.Enabled = false;
            this.DynamoCheckBox.Location = new System.Drawing.Point(127, 83);
            this.DynamoCheckBox.Name = "DynamoCheckBox";
            this.DynamoCheckBox.Size = new System.Drawing.Size(65, 17);
            this.DynamoCheckBox.TabIndex = 5;
            this.DynamoCheckBox.Text = "Dynamo";
            this.DynamoCheckBox.UseVisualStyleBackColor = true;
            // 
            // IncludePreReleaseCheckBox
            // 
            this.IncludePreReleaseCheckBox.AutoSize = true;
            this.IncludePreReleaseCheckBox.Location = new System.Drawing.Point(35, 33);
            this.IncludePreReleaseCheckBox.Name = "IncludePreReleaseCheckBox";
            this.IncludePreReleaseCheckBox.Size = new System.Drawing.Size(122, 17);
            this.IncludePreReleaseCheckBox.TabIndex = 6;
            this.IncludePreReleaseCheckBox.Text = "Include Pre-releases";
            this.IncludePreReleaseCheckBox.UseVisualStyleBackColor = true;
            this.IncludePreReleaseCheckBox.CheckedChanged += new System.EventHandler(this.IncludePreReleaseCheckBox_CheckedChanged);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(444, 411);
            this.Controls.Add(this.IncludePreReleaseCheckBox);
            this.Controls.Add(this.DynamoCheckBox);
            this.Controls.Add(this.GrasshopperCheckBox);
            this.Controls.Add(this.DownloadButton);
            this.Controls.Add(this.VersionSelector);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.RefreshButton);
            this.Name = "MainWindow";
            this.Text = "FEM-Design API installer";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button RefreshButton;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.ComboBox VersionSelector;
        private System.Windows.Forms.Button DownloadButton;
        private System.Windows.Forms.CheckBox GrasshopperCheckBox;
        private System.Windows.Forms.CheckBox DynamoCheckBox;
        private System.Windows.Forms.CheckBox IncludePreReleaseCheckBox;
    }
}

