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
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(146, 17)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(121, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(127, 55)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(121, 20)
		self._textBox2.TabIndex = 1
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 121)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(80, 53)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(84, 90)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(121, 20)
		self._label1.TabIndex = 3
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 90)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(66, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "Salary:"
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(192, 121)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(80, 53)
		self._button2.TabIndex = 5
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(102, 121)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(80, 53)
		self._button3.TabIndex = 6
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 52)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(118, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Pay Periods:"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 14)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(128, 23)
		self._label4.TabIndex = 8
		self._label4.Text = "Annual Salary:"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
		self.ClientSize = System.Drawing.Size(284, 183)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Salary Calculation"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		AnSal = float(self._textBox1.Text)
		PayPer = float(self._textBox2.Text)
		Sal = AnSal/PayPer
		self._label1.Text = str(round(Sal, 2))


	def Button3Click(self, sender, e):
		self._label1.Text = ""

	def Button2Click(self, sender, e):
		Application.Exit()