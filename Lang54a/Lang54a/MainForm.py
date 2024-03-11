import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSeaGreen
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(4, 8)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(119, 27)
		self._label1.TabIndex = 0
		self._label1.Text = "1970 VW Bug:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSeaGreen
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(4, 38)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(119, 27)
		self._label2.TabIndex = 1
		self._label2.Text = "1979 Firebird:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSeaGreen
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(4, 67)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(119, 28)
		self._label3.TabIndex = 2
		self._label3.Text = "1980 Subaru:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.LightSeaGreen
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(4, 98)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(119, 27)
		self._label4.TabIndex = 3
		self._label4.Text = "1975 Cutlass:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightSeaGreen
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(127, 8)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(87, 27)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightSeaGreen
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(127, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(87, 27)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.LightSeaGreen
		self._textBox3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(127, 68)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(87, 27)
		self._textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.LightSeaGreen
		self._textBox4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox4.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.ForeColor = System.Drawing.Color.White
		self._textBox4.Location = System.Drawing.Point(127, 98)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(87, 27)
		self._textBox4.TabIndex = 7
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSeaGreen
		self._button1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(218, 4)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 57)
		self._button1.TabIndex = 8
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSeaGreen
		self._button2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.None
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(218, 67)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 57)
		self._button2.TabIndex = 9
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSeaGreen
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(115, 132)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(119, 20)
		self._label5.TabIndex = 10
		self._label5.Text = "1970 VW Bug:"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSeaGreen
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(115, 162)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(119, 20)
		self._label6.TabIndex = 11
		self._label6.Text = "1979 Firebird:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSeaGreen
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(115, 192)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(119, 20)
		self._label7.TabIndex = 12
		self._label7.Text = "1980 Subaru:"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.LightSeaGreen
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label8.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(115, 222)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(119, 20)
		self._label8.TabIndex = 13
		self._label8.Text = "1975 Cutlass:"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Teal
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(236, 132)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(53, 20)
		self._label10.TabIndex = 15
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Teal
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(236, 162)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(53, 20)
		self._label11.TabIndex = 16
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Teal
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(236, 192)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(53, 20)
		self._label12.TabIndex = 17
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Teal
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.Location = System.Drawing.Point(236, 222)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(53, 20)
		self._label13.TabIndex = 18
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumAquamarine
		self.ClientSize = System.Drawing.Size(297, 249)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang54a"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Bug = float(self._textBox1.Text)
		Fire = float(self._textBox2.Text)
		Subaru = float(self._textBox3.Text)
		Cutlass = float(self._textBox4.Text)
		BugM = Bug // 31.8
		FireM = Fire // 10.3
		SubaruM = Subaru // 20.1
		CutlassM = Cutlass // 14.6
		self._label10.Text = str(BugM)
		self._label11.Text = str(FireM)
		self._label12.Text = str(SubaruM)
		self._label13.Text = str(CutlassM)


	def Button2Click(self, sender, e):
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""
		self._label13.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""