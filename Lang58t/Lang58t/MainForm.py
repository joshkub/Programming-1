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
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(12, 134)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(87, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Dollars  :"
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(12, 157)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(87, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Quarters:"
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 180)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(87, 23)
		self._label3.TabIndex = 2
		self._label3.Text = "Dimes    :"
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(12, 203)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(87, 23)
		self._label4.TabIndex = 3
		self._label4.Text = "Nickles  :"
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(12, 226)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(87, 23)
		self._label5.TabIndex = 4
		self._label5.Text = "Pennies  :"
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.LightCoral
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 22)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(128, 27)
		self._textBox1.TabIndex = 5
		# 
		# label6
		# 
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(96, 134)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 6
		# 
		# label7
		# 
		self._label7.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.ForeColor = System.Drawing.Color.White
		self._label7.Location = System.Drawing.Point(96, 157)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 7
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.ForeColor = System.Drawing.Color.White
		self._label8.Location = System.Drawing.Point(96, 180)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 8
		# 
		# label9
		# 
		self._label9.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.ForeColor = System.Drawing.Color.White
		self._label9.Location = System.Drawing.Point(96, 203)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 9
		# 
		# label10
		# 
		self._label10.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.ForeColor = System.Drawing.Color.White
		self._label10.Location = System.Drawing.Point(96, 226)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 10
		# 
		# label11
		# 
		self._label11.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.ForeColor = System.Drawing.Color.White
		self._label11.Location = System.Drawing.Point(12, 0)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(136, 23)
		self._label11.TabIndex = 13
		self._label11.Text = "Purchase Price:"
		# 
		# label12
		# 
		self._label12.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.ForeColor = System.Drawing.Color.White
		self._label12.Location = System.Drawing.Point(146, 0)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(140, 23)
		self._label12.TabIndex = 15
		self._label12.Text = "Amount Given:"
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.LightCoral
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(146, 22)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(128, 27)
		self._textBox2.TabIndex = 14
		# 
		# label13
		# 
		self._label13.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label13.ForeColor = System.Drawing.Color.White
		self._label13.Location = System.Drawing.Point(12, 52)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(78, 23)
		self._label13.TabIndex = 17
		self._label13.Text = "Change:"
		# 
		# label14
		# 
		self._label14.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label14.Location = System.Drawing.Point(83, 52)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 18
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(205, 120)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 68)
		self._button1.TabIndex = 19
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(205, 189)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 68)
		self._button2.TabIndex = 20
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 9, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(205, 91)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 28)
		self._button3.TabIndex = 21
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Firebrick
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang58t"
		self.ResumeLayout(False)
		self.PerformLayout()

	def Button1Click(self, sender, e):
		Price = float(self._textBox1.Text)
		Money = float(self._textBox2.Text)
		Change = Money - Price
		Dollars = Change // 1
		Quarters = (Change - Dollars) // 0.25
		Dimes = ((Change - Dollars) - (Quarters * 0.25)) // 0.1
		Nickles = ((Change - Dollars) - (Quarters * 0.25) - (Dimes * 0.1)) // 0.05
		Pennies = ((Change - Dollars) - (Quarters * 0.25) - (Dimes * 0.1) - (Nickles * 0.05)) // 0.01
		self._label14.Text = str(Change)
		self._label6.Text = str(Dollars)
		self._label7.Text = str(Quarters)
		self._label8.Text = str(Dimes)
		self._label9.Text = str(Nickles)
		self._label10.Text = str(Pennies)

	def Button3Click(self, sender, e):
		Application.Exit()