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
		self._button2 = System.Windows.Forms.Button()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Transparent
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(52, 5)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(71, 23)
		self._label1.TabIndex = 1
		self._label1.Text = "Sales:"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Transparent
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(26, 32)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(91, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Adv, Pay:"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Transparent
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(4, 59)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(110, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Comm. Rate:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Transparent
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(4, 87)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(97, 23)
		self._label4.TabIndex = 4
		self._label4.Text = "Commision:"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Transparent
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.ForeColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(23, 114)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(91, 23)
		self._label5.TabIndex = 5
		self._label5.Text = "Net Pay:"
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(123, 138)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 43)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.White
		self._label6.ForeColor = System.Drawing.Color.Black
		self._label6.Location = System.Drawing.Point(120, 59)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.White
		self._label7.ForeColor = System.Drawing.Color.Black
		self._label7.Location = System.Drawing.Point(120, 86)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 8
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.White
		self._label8.ForeColor = System.Drawing.Color.Black
		self._label8.Location = System.Drawing.Point(120, 114)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 9
		# 
		# textBox1
		# 
		self._textBox1.ForeColor = System.Drawing.Color.Black
		self._textBox1.Location = System.Drawing.Point(120, 6)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 10
		# 
		# textBox2
		# 
		self._textBox2.ForeColor = System.Drawing.Color.Black
		self._textBox2.Location = System.Drawing.Point(120, 32)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 11
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(18, 138)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(99, 43)
		self._button1.TabIndex = 12
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Turquoise
		self.ClientSize = System.Drawing.Size(233, 182)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Pg240Comm"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		sales = int(self._textBox1.Text)
		advpay = int(self._textBox2.Text)
		if sales < 10000:
			CommRate = 0.05
		elif sales >= 10000 and sales <= 14999:
			CommRate = 0.10
		elif sales >= 15000 and sales <= 17999:
			CommRate = 0.12
		elif sales >= 18000 and sales <= 21999:
			CommRate = 0.14
		elif sales >= 22000:
			CommRate = 0.16
		Comm = sales * CommRate
		NetPay = Comm - advpay
		self._label6.Text = str(CommRate)
		self._label7.Text = str(Comm)
		self._label8.Text = str(NetPay)
		
		