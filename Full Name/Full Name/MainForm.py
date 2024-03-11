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
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.White
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.PeachPuff
		self._button1.Location = System.Drawing.Point(12, 85)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(260, 33)
		self._button1.TabIndex = 0
		self._button1.Text = "What's my full name?"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.White
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.PeachPuff
		self._button2.Location = System.Drawing.Point(228, 10)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(44, 25)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.TextAlign = System.Drawing.ContentAlignment.TopCenter
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.PeachPuff
		self._label1.Location = System.Drawing.Point(12, 38)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(260, 44)
		self._label1.TabIndex = 2
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label1.Click += self.Label1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PeachPuff
		self.ClientSize = System.Drawing.Size(284, 120)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Full Name"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label1.Text = "Joshua Kubala"

	def TextBox1TextChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		Application.Exit()

	def Label1Click(self, sender, e):
		pass