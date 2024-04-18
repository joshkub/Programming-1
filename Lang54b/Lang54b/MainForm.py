import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.PaleGreen
		self._textBox1.ForeColor = System.Drawing.Color.Black
		self._textBox1.Location = System.Drawing.Point(28, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.PaleGreen
		self._textBox2.ForeColor = System.Drawing.Color.Black
		self._textBox2.Location = System.Drawing.Point(186, 12)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.PaleGreen
		self._textBox3.ForeColor = System.Drawing.Color.Black
		self._textBox3.Location = System.Drawing.Point(28, 60)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.PaleGreen
		self._textBox4.ForeColor = System.Drawing.Color.Black
		self._textBox4.Location = System.Drawing.Point(186, 60)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 3
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(18, 103)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(81, 26)
		self._label2.TabIndex = 5
		self._label2.Text = "Average:"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(42, 150)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(57, 23)
		self._label1.TabIndex = 6
		self._label1.Text = "Total:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(105, 150)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(82, 23)
		self._label3.TabIndex = 7
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(105, 103)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(82, 23)
		self._label4.TabIndex = 8
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.PaleGreen
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(3, 207)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(158, 69)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.PaleGreen
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(162, 207)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(149, 69)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.PaleGreen
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(255, 176)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(56, 31)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.SeaGreen
		self.ClientSize = System.Drawing.Size(314, 279)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang54b"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		one = int(self._textBox1.Text)
		two = int(self._textBox2.Text)
		three = int(self._textBox3.Text)
		four = int(self._textBox4.Text)
		total = one + two + three + four
		average = (one + two + three + four) / 4
		self._label3.Text = str(total)
		self._label4.Text = str(average)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._label3.Text = ""
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()

