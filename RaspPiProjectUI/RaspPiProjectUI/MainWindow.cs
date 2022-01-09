using System;
using System.Windows.Forms;

namespace RaspPiProjectUI
{
    public partial class MainWindow : Form
    {
        Control dayButton;
        Control weekButton;
        Control monthButton;
        Period selectedPeriod = Period.day;

        public MainWindow()
        {
            InitializeComponent();

            dayButton = Controls.Find("day", true)[0];
            weekButton = Controls.Find("week", true)[0];
            monthButton = Controls.Find("month", true)[0];

            dayButton.Enabled = false;
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void day_Click(object sender, EventArgs e)
        {
            selectedPeriod = Period.day;

            dayButton.Enabled = false;
            weekButton.Enabled = true;
            monthButton.Enabled = true;
        }

        private void week_Click(object sender, EventArgs e)
        {
            selectedPeriod = Period.week;

            dayButton.Enabled = true;
            weekButton.Enabled = false;
            monthButton.Enabled = true;
        }

        private void month_Click(object sender, EventArgs e)
        {
            selectedPeriod = Period.month;

            dayButton.Enabled = true;
            weekButton.Enabled = true;
            monthButton.Enabled = false;
        }
    }
}
