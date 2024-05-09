import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.BackColor = System.Drawing.Color.LightSalmon
		self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel1.Controls.Add(self._textBox3)
		self._panel1.Controls.Add(self._textBox2)
		self._panel1.Controls.Add(self._textBox1)
		self._panel1.Controls.Add(self._label5)
		self._panel1.Controls.Add(self._label4)
		self._panel1.Controls.Add(self._label3)
		self._panel1.Controls.Add(self._label2)
		self._panel1.Controls.Add(self._label1)
		self._panel1.ForeColor = System.Drawing.Color.White
		self._panel1.Location = System.Drawing.Point(12, 12)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(260, 145)
		self._panel1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSalmon
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 196)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(129, 53)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSalmon
		self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(147, 196)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(129, 53)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(30, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(113, 22)
		self._label1.TabIndex = 0
		self._label1.Text = "Test Score 1:"
		# 
		# label2
		# 
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(30, 39)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(113, 22)
		self._label2.TabIndex = 1
		self._label2.Text = "Test Score 2:"
		# 
		# label3
		# 
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(30, 62)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(113, 22)
		self._label3.TabIndex = 2
		self._label3.Text = "Test Score 3:"
		# 
		# label4
		# 
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(20, 94)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(51, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Average:"
		# 
		# label5
		# 
		self._label5.Location = System.Drawing.Point(67, 94)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 4
		# 
		# label6
		# 
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(94, 160)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 5
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(98, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(110, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(98, 36)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(110, 20)
		self._textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(98, 59)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(110, 20)
		self._textBox3.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Firebrick
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._panel1)
		self.Name = "MainForm"
		self.Text = "Pg198ScoreAvg"
		self._panel1.ResumeLayout(False)
		self._panel1.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		ScoreAvg = (num1 + num2 + num3)/3
		self._label5.Text = str(ScoreAvg)
		if ScoreAvg > 95:
			self._label6.Text = "Great Job!"
		else:
			self._label6.Text = ""


	def Label5Click(self, sender, e):
		pass