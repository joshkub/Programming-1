﻿import System.Drawing
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
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(136, 203)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(112, 26)
		self._button1.TabIndex = 0
		self._button1.Text = "Clear"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(254, 203)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(112, 26)
		self._button2.TabIndex = 1
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(18, 203)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(112, 26)
		self._button3.TabIndex = 2
		self._button3.Text = "Calculate"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(18, 22)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(138, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "Enter you first name:"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(17, 56)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(145, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Enter your last name:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(18, 127)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(145, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "This is your full name:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(159, 127)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(149, 23)
		self._label4.TabIndex = 6
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(153, 57)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 22)
		self._textBox1.TabIndex = 7
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(153, 22)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 22)
		self._textBox2.TabIndex = 8
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(384, 261)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Pg119FullName"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		last = str(self._textBox1.Text)
		first = str(self._textBox2.Text)
		self._label4.Text = first + " " + last

	def Button1Click(self, sender, e):
		self._textBox2.Text = ""
		self._textBox1.Text = ""
		self._label4.Text = ""		

	def Button2Click(self, sender, e):
		Application.Exit()