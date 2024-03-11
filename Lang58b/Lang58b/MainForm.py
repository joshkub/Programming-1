import math
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
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.SeaGreen
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(3, 192)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(91, 66)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.SeaGreen
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(91, 192)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 66)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(38, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(134, 20)
		self._textBox1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(38, 38)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(134, 20)
		self._textBox2.TabIndex = 3
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(38, 64)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(134, 20)
		self._textBox3.TabIndex = 4
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(11, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(21, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "A"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 61)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(21, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "C"
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(-1, 139)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(91, 23)
		self._label6.TabIndex = 9
		self._label6.Text = "Root(-):"
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(80, 139)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 10
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(86, 100)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 8
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(-1, 100)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(91, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Root(+):"
		self._label4.Click += self.Label4Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(11, 35)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(21, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "B"
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.SeaGreen
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(179, 192)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(49, 66)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.PaleGreen
		self.ClientSize = System.Drawing.Size(236, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang58b"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		A = float(self._textBox1.Text)
		B = float(self._textBox2.Text)
		C = float(self._textBox3.Text)
		Rootone = (-B + math.sqrt(B**2 -4*A*C))/(2*A)
		Roottwo = (-B - math.sqrt(B**2 -4*A*C))/(2*A)
		self._label5.Text = str(Rootone)
		self._label7.Text = str(Roottwo)
		
	def Button2Click(self, sender, e):
		self._textbox1.Text = ""
		self._textbox2.Text = ""
		self._textbox3.Text = ""
		self._label5.Text = ""
		self._label6.Text = ""

	def Label6Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Application.Exit()