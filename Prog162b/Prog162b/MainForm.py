import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._listBox2 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.HotTrack
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(12, 290)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 76)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.HotTrack
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(173, 290)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(158, 76)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.HotTrack
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(335, 290)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(158, 76)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.HotTrack
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(12, 11)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(481, 264)
		self._listBox1.TabIndex = 4
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.SystemColors.HotTrack
		self._button4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button4.Location = System.Drawing.Point(12, 291)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(158, 76)
		self._button4.TabIndex = 1
		self._button4.Text = "Calculate"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button1Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.SystemColors.HotTrack
		self._button5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button5.Location = System.Drawing.Point(173, 291)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(158, 76)
		self._button5.TabIndex = 2
		self._button5.Text = "Clear"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button2Click
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.SystemColors.HotTrack
		self._button6.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button6.Location = System.Drawing.Point(335, 291)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(158, 76)
		self._button6.TabIndex = 3
		self._button6.Text = "Exit"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button3Click
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.SystemColors.HotTrack
		self._listBox2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._listBox2.FormattingEnabled = True
		self._listBox2.Location = System.Drawing.Point(12, 12)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(481, 264)
		self._listBox2.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.RoyalBlue
		self.ClientSize = System.Drawing.Size(505, 378)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Prog162b"
		self.ResumeLayout(False)


	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button1Click(self, sender, e):
		heading = "Year/t/tPopulation (in mil.)"
		self._listBox1.Items.Add(heading)
		pop = 243 # 1990
		for year in range(1991, 2016):
			line = str(year) + "/t/t" + str(int(pop))
			self._listBox1.Items.Add(line)
			pop *= 1.029 # pop = pop * 1.029

	def Button3Click(self, sender, e):
		Application.Exit()