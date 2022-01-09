namespace RaspPiProjectUI
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
            System.Windows.Forms.DataVisualization.Charting.ChartArea chartArea1 = new System.Windows.Forms.DataVisualization.Charting.ChartArea();
            System.Windows.Forms.DataVisualization.Charting.Legend legend1 = new System.Windows.Forms.DataVisualization.Charting.Legend();
            System.Windows.Forms.DataVisualization.Charting.Series series1 = new System.Windows.Forms.DataVisualization.Charting.Series();
            this.label1 = new System.Windows.Forms.Label();
            this.wykres = new System.Windows.Forms.DataVisualization.Charting.Chart();
            this.panel1 = new System.Windows.Forms.Panel();
            this.panel2 = new System.Windows.Forms.Panel();
            this.period = new System.Windows.Forms.GroupBox();
            this.day = new System.Windows.Forms.Button();
            this.month = new System.Windows.Forms.Button();
            this.week = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.wykres)).BeginInit();
            this.panel1.SuspendLayout();
            this.panel2.SuspendLayout();
            this.period.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(238)));
            this.label1.Location = new System.Drawing.Point(3, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(171, 36);
            this.label1.TabIndex = 0;
            this.label1.Text = "Hello World";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // wykres
            // 
            chartArea1.Name = "ChartArea1";
            this.wykres.ChartAreas.Add(chartArea1);
            this.wykres.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            legend1.Name = "Legend1";
            this.wykres.Legends.Add(legend1);
            this.wykres.Location = new System.Drawing.Point(12, 68);
            this.wykres.Name = "wykres";
            series1.ChartArea = "ChartArea1";
            series1.ChartType = System.Windows.Forms.DataVisualization.Charting.SeriesChartType.Line;
            series1.Legend = "Legend1";
            series1.Name = "Series1";
            this.wykres.Series.Add(series1);
            this.wykres.Size = new System.Drawing.Size(1238, 509);
            this.wykres.TabIndex = 1;
            this.wykres.Text = "chart1";
            // 
            // panel1
            // 
            this.panel1.Controls.Add(this.label1);
            this.panel1.Location = new System.Drawing.Point(12, 12);
            this.panel1.Name = "panel1";
            this.panel1.Size = new System.Drawing.Size(1238, 50);
            this.panel1.TabIndex = 2;
            // 
            // panel2
            // 
            this.panel2.Controls.Add(this.period);
            this.panel2.Location = new System.Drawing.Point(12, 583);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(1238, 78);
            this.panel2.TabIndex = 3;
            // 
            // period
            // 
            this.period.Controls.Add(this.day);
            this.period.Controls.Add(this.month);
            this.period.Controls.Add(this.week);
            this.period.Location = new System.Drawing.Point(9, 3);
            this.period.Name = "period";
            this.period.Size = new System.Drawing.Size(241, 72);
            this.period.TabIndex = 3;
            this.period.TabStop = false;
            this.period.Text = "Okres";
            // 
            // day
            // 
            this.day.Location = new System.Drawing.Point(6, 21);
            this.day.Name = "day";
            this.day.Size = new System.Drawing.Size(72, 32);
            this.day.TabIndex = 0;
            this.day.Text = "Dziś";
            this.day.UseVisualStyleBackColor = true;
            this.day.Click += new System.EventHandler(this.day_Click);
            // 
            // month
            // 
            this.month.Location = new System.Drawing.Point(162, 21);
            this.month.Name = "month";
            this.month.Size = new System.Drawing.Size(72, 32);
            this.month.TabIndex = 2;
            this.month.Text = "Miesiąc";
            this.month.UseVisualStyleBackColor = true;
            this.month.Click += new System.EventHandler(this.month_Click);
            // 
            // week
            // 
            this.week.Location = new System.Drawing.Point(84, 21);
            this.week.Name = "week";
            this.week.Size = new System.Drawing.Size(72, 32);
            this.week.TabIndex = 1;
            this.week.Text = "Tydzień";
            this.week.UseVisualStyleBackColor = true;
            this.week.Click += new System.EventHandler(this.week_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1262, 673);
            this.Controls.Add(this.panel2);
            this.Controls.Add(this.panel1);
            this.Controls.Add(this.wykres);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.Name = "MainWindow";
            this.Text = "RaspPiProject";
            ((System.ComponentModel.ISupportInitialize)(this.wykres)).EndInit();
            this.panel1.ResumeLayout(false);
            this.panel1.PerformLayout();
            this.panel2.ResumeLayout(false);
            this.period.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.DataVisualization.Charting.Chart wykres;
        private System.Windows.Forms.Panel panel1;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.GroupBox period;
        private System.Windows.Forms.Button day;
        private System.Windows.Forms.Button month;
        private System.Windows.Forms.Button week;
    }
}

