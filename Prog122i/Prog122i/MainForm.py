import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button2 = System.Windows.Forms.Button()
		self._listBox2 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.White
		self._button1.ForeColor = System.Drawing.Color.Black
		self._button1.Location = System.Drawing.Point(12, 334)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(193, 94)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.White
		self._listBox1.ForeColor = System.Drawing.Color.Black
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(391, 134)
		self._listBox1.TabIndex = 1
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.White
		self._button2.ForeColor = System.Drawing.Color.Black
		self._button2.Location = System.Drawing.Point(210, 334)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(193, 94)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.Color.White
		self._listBox2.ForeColor = System.Drawing.Color.Black
		self._listBox2.FormattingEnabled = True
		self._listBox2.Location = System.Drawing.Point(12, 145)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(391, 134)
		self._listBox2.TabIndex = 3
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Red
		self.ClientSize = System.Drawing.Size(415, 440)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog122i"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "collum1\t\tcollum2\t\tcollum3"
		self._listBox1.Items.Add(heading)
		for num in range (-25, 0):
			col1 = abs(num)	
			col2 = (col1 ** 0.3333333333333333)
			col3 = (col1 ** 3)

			cols = "-" + str(col1) + "\t\t -" + str(col2) + "\t\t -" + str(col3)
			
			self._listBox1.Items.Add(col)
		for num in range (1, 26):
			col1 = abs(num)	
			col2 = (col1 ** 0.3333333333333333)
			col3 = (col1 ** 3)

			cols = str(col1) + "\t\t" + str(col2) + "\t\t" + str(col3)
			
			self._listBox2.Items.Add(cols2)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()
		self._listBox2.Items.Clear() 		