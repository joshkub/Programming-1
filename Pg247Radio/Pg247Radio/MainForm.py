import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.ForeColor = System.Drawing.Color.White
		self._radioButton1.Location = System.Drawing.Point(18, 26)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(104, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Choice 1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.ForeColor = System.Drawing.Color.White
		self._radioButton2.Location = System.Drawing.Point(18, 84)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(104, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Choice 2"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.ForeColor = System.Drawing.Color.White
		self._radioButton3.Location = System.Drawing.Point(18, 151)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(104, 24)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Choice 3"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.ForeColor = System.Drawing.Color.White
		self._checkBox1.Location = System.Drawing.Point(163, 27)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 3
		self._checkBox1.Text = "Choice 4"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.ForeColor = System.Drawing.Color.White
		self._checkBox2.Location = System.Drawing.Point(163, 85)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 4
		self._checkBox2.Text = "Choice 5"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Microsoft YaHei", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.ForeColor = System.Drawing.Color.White
		self._checkBox3.Location = System.Drawing.Point(163, 152)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 5
		self._checkBox3.Text = "Choice 6"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(157, 215)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(115, 34)
		self._button2.TabIndex = 7
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 215)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(115, 34)
		self._button1.TabIndex = 8
		self._button1.Text = "Ok"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.IndianRed
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "Pg247Radio"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			strMessage = "You selected choice 1"
		if self._radioButton2.Checked == True:
			strMessage = "You selected choice 2"
		if self._radioButton3.Checked == True:
			strMessage = "You selected choice 3"
		if self._checkBox1.Checked == True:
			strMessage += " and choice 4"
		if self._checkBox2.Checked == True:
			strMessage += " and choice 5"
		if self._checkBox3.Checked == True:
			strMessage += " and choice 6"
		MessageBox.Show(strMessage)

	def Button2Click(self, sender, e):
		Application.Exit()