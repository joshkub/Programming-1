﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.HotTrack
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(13, 12)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(103, 27)
		self._label1.TabIndex = 0
		self._label1.Text = "Num1:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(119, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(103, 27)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(119, 45)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(103, 27)
		self._textBox2.TabIndex = 3
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.HotTrack
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(13, 45)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(103, 27)
		self._label2.TabIndex = 2
		self._label2.Text = "Num2:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.HotTrack
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(13, 78)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(103, 27)
		self._label3.TabIndex = 4
		self._label3.Text = "Sum:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.HotTrack
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(13, 111)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(103, 27)
		self._label4.TabIndex = 6
		self._label4.Text = "Difference"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.SystemColors.HotTrack
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(13, 144)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(103, 27)
		self._label5.TabIndex = 8
		self._label5.Text = "Product:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.HotTrack
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(13, 177)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(103, 27)
		self._label6.TabIndex = 10
		self._label6.Text = "Average:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.SystemColors.HotTrack
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(13, 210)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(103, 27)
		self._label7.TabIndex = 12
		self._label7.Text = "Distance:"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.SystemColors.HotTrack
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(13, 243)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(103, 27)
		self._label8.TabIndex = 14
		self._label8.Text = "Max:"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.SystemColors.HotTrack
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(13, 276)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(103, 27)
		self._label9.TabIndex = 16
		self._label9.Text = "Min:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.RoyalBlue
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(228, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(107, 93)
		self._button1.TabIndex = 18
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.RoyalBlue
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(228, 111)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(107, 93)
		self._button2.TabIndex = 19
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.RoyalBlue
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(228, 210)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(107, 93)
		self._button3.TabIndex = 20
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.WhiteSmoke
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.Black
		self._label10.Location = System.Drawing.Point(119, 78)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(103, 27)
		self._label10.TabIndex = 21
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.WhiteSmoke
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.Black
		self._label11.Location = System.Drawing.Point(119, 111)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(103, 27)
		self._label11.TabIndex = 22
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.WhiteSmoke
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.Black
		self._label12.Location = System.Drawing.Point(119, 177)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(103, 27)
		self._label12.TabIndex = 24
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.WhiteSmoke
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.Black
		self._label13.Location = System.Drawing.Point(119, 144)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(103, 27)
		self._label13.TabIndex = 23
		self._label13.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.WhiteSmoke
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.ForeColor = System.Drawing.Color.Black
		self._label14.Location = System.Drawing.Point(119, 243)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(103, 27)
		self._label14.TabIndex = 26
		self._label14.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.WhiteSmoke
		self._label15.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label15.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label15.ForeColor = System.Drawing.Color.Black
		self._label15.Location = System.Drawing.Point(119, 210)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(103, 27)
		self._label15.TabIndex = 25
		self._label15.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.WhiteSmoke
		self._label16.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label16.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label16.ForeColor = System.Drawing.Color.Black
		self._label16.Location = System.Drawing.Point(119, 276)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(103, 27)
		self._label16.TabIndex = 28
		self._label16.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CornflowerBlue
		self.ClientSize = System.Drawing.Size(347, 320)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.ForeColor = System.Drawing.Color.Black
		self.Name = "MainForm"
		self.Text = "Prog88a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		sum = num1 + num2
		diff = num1 - num2
		product = num1 * num2
		avg = (num1 + num2) /2
		AbsDiff = abs(diff)
		max = 0
		min = 0
		if num1 >= num2:
			max = num1
		else: 
			max = num1
			
		if max == num1:
			min = num2
		else:
			min = num1
			
		self._label10.Text = str(sum)
		self._label11.Text = str(diff)
		self._label13.Text = str(product)
		self._label12.Text = str(avg)
		self._label14.Text = str(AbsDiff)
		self._label15.Text = str(max)
		self._label16.Text = str(min)