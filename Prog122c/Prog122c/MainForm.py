import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.HotTrack
		self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.White
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 21
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(575, 256)
		self._listBox1.TabIndex = 2
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.HotTrack
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(203, 282)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(189, 108)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.HotTrack
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 282)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(185, 108)
		self._button1.TabIndex = 4
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.HotTrack
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(398, 282)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(189, 108)
		self._button3.TabIndex = 5
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SteelBlue
		self.ClientSize = System.Drawing.Size(603, 402)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "collum1\t\tcollum2\t\tcollum3\t\tcollum4"
		self._listBox1.Items.Add(heading)
		for num in range (1, 5+1):
			col1 = num * 2
			col2 = col1 + 1
			col3 = col1 * 2
			col4 = col1 ** 2
			col = str(col1) + "\t\t" + str(col2) + "\t\t" + str(col3) + "\t\t" + str(col4)
			
			self._listBox1.Items.Add(col)
			
	
	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()