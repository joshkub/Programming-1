import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox2 = System.Windows.Forms.ListBox()
		self._button6 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox2
		# 
		self._listBox2.BackColor = System.Drawing.SystemColors.HotTrack
		self._listBox2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._listBox2.FormattingEnabled = True
		self._listBox2.Location = System.Drawing.Point(19, 24)
		self._listBox2.Name = "listBox2"
		self._listBox2.Size = System.Drawing.Size(481, 264)
		self._listBox2.TabIndex = 8
		# 
		# button6
		# 
		self._button6.BackColor = System.Drawing.SystemColors.HotTrack
		self._button6.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button6.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button6.Location = System.Drawing.Point(342, 303)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(158, 76)
		self._button6.TabIndex = 7
		self._button6.Text = "Exit"
		self._button6.UseVisualStyleBackColor = False
		self._button6.Click += self.Button6Click
		# 
		# button5
		# 
		self._button5.BackColor = System.Drawing.SystemColors.HotTrack
		self._button5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button5.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button5.Location = System.Drawing.Point(180, 303)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(158, 76)
		self._button5.TabIndex = 6
		self._button5.Text = "Clear"
		self._button5.UseVisualStyleBackColor = False
		self._button5.Click += self.Button5Click
		# 
		# button4
		# 
		self._button4.BackColor = System.Drawing.SystemColors.HotTrack
		self._button4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._button4.Location = System.Drawing.Point(19, 303)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(158, 76)
		self._button4.TabIndex = 5
		self._button4.Text = "Calculate"
		self._button4.UseVisualStyleBackColor = False
		self._button4.Click += self.Button4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DodgerBlue
		self.ClientSize = System.Drawing.Size(518, 402)
		self.Controls.Add(self._listBox2)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Name = "MainForm"
		self.Text = "Prog122b"
		self.ResumeLayout(False)

	def Button4Click(self, sender, e):
		heading = "Hour / Pay"
		self._listBox2.Items.Add(heading)
		Pay = 4
		for Hour in range(1, 41):
			PayH = 4 * Hour
			line = str(Hour) + " / " + str(PayH)
			self._listBox2.Items.Add(line)
			

	def Button5Click(self, sender, e):
		self._listBox2.Items.Clear()

	def Button6Click(self, sender, e):
		Application.Exit()