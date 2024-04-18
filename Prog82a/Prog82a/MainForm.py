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
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.Color.White
		self._textBox1.Location = System.Drawing.Point(136, 39)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(51, 24)
		self._textBox1.TabIndex = 0
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._textBox2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.ForeColor = System.Drawing.Color.White
		self._textBox2.Location = System.Drawing.Point(137, 12)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(51, 24)
		self._textBox2.TabIndex = 1
		self._textBox2.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(23, 66)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(109, 24)
		self._label1.TabIndex = 2
		self._label1.Text = "Ticket Cost:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(9, 110)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(87, 56)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(1, 39)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(131, 24)
		self._label2.TabIndex = 4
		self._label2.Text = "Vehicle Speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._button2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.White
		self._button2.Location = System.Drawing.Point(102, 110)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(87, 56)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.ForeColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(12, 12)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(121, 24)
		self._label3.TabIndex = 6
		self._label3.Text = "Speed Limit:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.SystemColors.MenuHighlight
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.ForeColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(135, 66)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(52, 24)
		self._label4.TabIndex = 7
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.CornflowerBlue
		self.ClientSize = System.Drawing.Size(201, 179)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Prog82a"
		self.ResumeLayout(False)
		self.PerformLayout()

		
	def Button1Click(self, sender, e):
		Speed = float(self._textBox1.Text)
		SpeedLimit = float(self._textBox2.Text)
		Speeding = Speed - SpeedLimit
		Ticket = 20 + (Speeding * 5)
		self._label4.Text = str(Ticket)

	def Button2Click(self, sender, e):
		self._label4.Text = ""
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		