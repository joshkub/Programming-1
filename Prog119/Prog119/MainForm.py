import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button3 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(-2, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(185, 34)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter Your First Name:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.FlatStyle = System.Windows.Forms.FlatStyle.System
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(180, 134)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(160, 19)
		self._label4.TabIndex = 3
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.None
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(180, 79)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(160, 19)
		self._textBox1.TabIndex = 4
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.None
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(180, 23)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(160, 19)
		self._textBox2.TabIndex = 5
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(12, 192)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(102, 34)
		self._button3.TabIndex = 8
		self._button3.Text = "Show Name"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(238, 192)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(102, 34)
		self._button1.TabIndex = 9
		self._button1.Text = "Exit"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(125, 192)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(102, 34)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(-2, 67)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(185, 34)
		self._label5.TabIndex = 1
		self._label5.Text = "Enter Your Last Name:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(72, 126)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(111, 34)
		self._label6.TabIndex = 2
		self._label6.Text = "Full Name:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(352, 238)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog119"
		self.ResumeLayout(False)
		self.PerformLayout()
			
		

	def Button3Click(self, sender, e):
		FN = str(self._textBox2.Text)
		LN = str(self._textBox1.Text)
		FULLN = str(FN + " " + LN)
		self._label4.Text = str(FULLN)
		

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox2.Text = ""
		self._textBox1.Text = ""

	def Button1Click(self, sender, e):
		Application.Exit()