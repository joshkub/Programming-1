import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.Location = System.Drawing.Point(21, 22)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(200, 100)
		self._panel1.TabIndex = 0
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._panel1)
		self.Name = "MainForm"
		self.Text = "Pg198ScoreAvg"
		self.ResumeLayout(False)

