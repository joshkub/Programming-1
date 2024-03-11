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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label6 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(12, 200)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 52)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(128, 200)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 52)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button3.Font = System.Drawing.Font("Microsoft YaHei", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.White
		self._button3.Location = System.Drawing.Point(196, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(49, 27)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(13, 2)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(79, 43)
		self._label1.TabIndex = 3
		self._label1.Text = "Pounds:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(5, 47)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(87, 43)
		self._label2.TabIndex = 4
		self._label2.Text = "Shillings:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(32, 139)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(60, 34)
		self._label3.TabIndex = 5
		self._label3.Text = "Value:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(27, 90)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(65, 43)
		self._label4.TabIndex = 6
		self._label4.Text = "Pence:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(90, 98)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 46)
		self._label5.TabIndex = 7
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(90, 98)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 27)
		self._textBox1.TabIndex = 8
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(90, 55)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 27)
		self._textBox2.TabIndex = 9
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.ForeColor = System.Drawing.Color.White
		self._textBox3.Location = System.Drawing.Point(90, 12)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 27)
		self._textBox3.TabIndex = 10
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.FlatStyle = System.Windows.Forms.FlatStyle.Flat
		self._label6.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.ForeColor = System.Drawing.Color.White
		self._label6.Location = System.Drawing.Point(90, 145)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 22)
		self._label6.TabIndex = 11
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Navy
		self.ClientSize = System.Drawing.Size(255, 264)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.ResumeLayout(False)
		self.PerformLayout()
		
		
		

	def Button1Click(self, sender, e):
		Pound = float(self._textBox3.Text)
		Shilling = float(self._textBox2.Text)
		Pence = float(self._textBox1.Text)
		Dpounds = round(Pound + (Shilling*0.05) + (Pence*0.00416666666), 2)
		self._label6.Text = str(Dpounds)


	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._label6.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()