using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Fibonacci_Series
{
    public partial class form1 : Form
    {
        public form1()
        {
            InitializeComponent();
                    
        }


        int count = 0; 

        private void btn_generate_Click(object sender, EventArgs e)
        {
            if (txt_num.Text != "")
            {
                int num = int.Parse(txt_num.Text);
                int[] arr = new int[num];
                int a = 0;
                int b = 1;
                string s_list = "0";

                for (int i = 1; i < num; i++)
                {
                    int c = a + b;

                    arr[i] = c;
                    s_list = s_list+ c.ToString();
                    a = b;
                    b = c;
                }
                try
                {
                    arr[0] = 1;
                    txt_show.Text = arr[count].ToString();
                    count++;

                }

                catch
                {
                    MessageBox.Show("All Numbers Displayed:");
                    txt_show.Clear();
                }
            }

            else
            {
                MessageBox.Show("Enter the number of Fibonacci Number");
            }
        }
    }
}
