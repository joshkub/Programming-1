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
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightSalmon
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 196)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(137, 56)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightSalmon
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(149, 196)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(123, 56)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Red
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(237, -2)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(48, 28)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Transparent
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 39)
		self._label1.TabIndex = 3
		self._label1.Text = "Radius:"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightSalmon
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(108, 17)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(77, 22)
		self._textBox1.TabIndex = 7
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Transparent
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(37, 47)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(84, 34)
		self._label2.TabIndex = 8
		self._label2.Text = "Area:"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Transparent
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(108, 54)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(77, 23)
		self._label3.TabIndex = 9
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Transparent
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(10, 84)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(111, 34)
		self._label4.TabIndex = 10
		self._label4.Text = "Circum:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Transparent
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(108, 92)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(77, 23)
		self._label5.TabIndex = 11
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Transparent
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(12, 123)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(109, 34)
		self._label6.TabIndex = 12
		self._label6.Text = "Radius:"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Transparent
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(108, 131)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(77, 23)
		self._label7.TabIndex = 13
		self._label7.Click += self.Label7Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.OrangeRed
		self.ClientSize = System.Drawing.Size(284, 262)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang54c"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		pi = 3.14159
		radius = float(self._textBox1.Text)
		area = round(pi * radius**2, 3)
		circum = round(radius * pi * 2, 3)
		self._label3.Text = str(area)
		self._label5.Text = str(circum)
		self._label7.Text = str(radius)
		
		

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._label3.Text = ""
		self._label5.Text = ""
		self._label7.Text = ""
		
		
	

	def Button3Click(self, sender, e):
		Application.Exit()

	def Label3Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label7Click(self, sender, e):
		pass