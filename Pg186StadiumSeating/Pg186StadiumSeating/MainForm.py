import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self._panel2 = System.Windows.Forms.Panel()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label4 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._panel1.SuspendLayout()
		self._panel2.SuspendLayout()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.BackColor = System.Drawing.Color.Gray
		self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel1.Controls.Add(self._textBox3)
		self._panel1.Controls.Add(self._textBox2)
		self._panel1.Controls.Add(self._textBox1)
		self._panel1.Controls.Add(self._label7)
		self._panel1.Controls.Add(self._label6)
		self._panel1.Controls.Add(self._label5)
		self._panel1.Controls.Add(self._label2)
		self._panel1.Controls.Add(self._label1)
		self._panel1.ForeColor = System.Drawing.Color.White
		self._panel1.Location = System.Drawing.Point(12, 23)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(200, 167)
		self._panel1.TabIndex = 0
		# 
		# panel2
		# 
		self._panel2.BackColor = System.Drawing.Color.Gray
		self._panel2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel2.Controls.Add(self._label14)
		self._panel2.Controls.Add(self._label13)
		self._panel2.Controls.Add(self._label12)
		self._panel2.Controls.Add(self._label11)
		self._panel2.Controls.Add(self._label4)
		self._panel2.Controls.Add(self._label8)
		self._panel2.Controls.Add(self._label9)
		self._panel2.Controls.Add(self._label10)
		self._panel2.Controls.Add(self._label3)
		self._panel2.ForeColor = System.Drawing.Color.White
		self._panel2.Location = System.Drawing.Point(238, 23)
		self._panel2.Name = "panel2"
		self._panel2.Size = System.Drawing.Size(200, 167)
		self._panel2.TabIndex = 1
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Gray
		self._button1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(91, 231)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 37)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Gray
		self._button2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(183, 231)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 37)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Gray
		self._button3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(275, 231)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 37)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(21, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(178, 43)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the number of tickets sold for each class of seats"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(3, 0)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(82, 16)
		self._label2.TabIndex = 1
		self._label2.Text = "Tickets Sold"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25)
		self._label3.Location = System.Drawing.Point(3, -1)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(109, 17)
		self._label3.TabIndex = 2
		self._label3.Text = "Revenue Generated"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(21, 59)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(63, 17)
		self._label5.TabIndex = 2
		self._label5.Text = "Class  A:"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(21, 88)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(63, 17)
		self._label6.TabIndex = 3
		self._label6.Text = "Class  B:"
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(21, 117)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(63, 17)
		self._label7.TabIndex = 4
		self._label7.Text = "Class  C:"
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(39, 87)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(73, 17)
		self._label8.TabIndex = 7
		self._label8.Text = "Class  C:"
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(39, 58)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(73, 17)
		self._label9.TabIndex = 6
		self._label9.Text = "Class  B:"
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(39, 29)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(73, 17)
		self._label10.TabIndex = 5
		self._label10.Text = "Class  A:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Gray
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(78, 58)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 5
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Gray
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(78, 87)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 6
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Gray
		self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox3.ForeColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(78, 116)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 7
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(-1, 116)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 18)
		self._label4.TabIndex = 8
		self._label4.Text = "Total Revenue:"
		# 
		# label11
		# 
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(95, 29)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(85, 18)
		self._label11.TabIndex = 9
		# 
		# label12
		# 
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(95, 58)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(85, 18)
		self._label12.TabIndex = 10
		# 
		# label13
		# 
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label13.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(95, 88)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(85, 18)
		self._label13.TabIndex = 11
		# 
		# label14
		# 
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label14.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(95, 116)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(85, 18)
		self._label14.TabIndex = 12
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DimGray
		self.ClientSize = System.Drawing.Size(450, 280)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._panel2)
		self.Controls.Add(self._panel1)
		self.Name = "MainForm"
		self.Text = "Pg186StadiumSeating"
		self._panel1.ResumeLayout(False)
		self._panel1.PerformLayout()
		self._panel2.ResumeLayout(False)
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		CA = (self._textBox1.Text)
		CB = (self._textBox2.Text)
		CC = (self._textBox3.Text)
		TR = (CA * 15) + (CA * 12) + (CA * 9)
		self._label11.Text = str(CA)
		self._label12.Text = str(CB)
		self._label13.Text = str(CC)
		self._label14.Text = str(TR)