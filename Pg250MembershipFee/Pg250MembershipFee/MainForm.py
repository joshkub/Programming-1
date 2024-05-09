import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._panel1 = System.Windows.Forms.Panel()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._panel2 = System.Windows.Forms.Panel()
		self._panel3 = System.Windows.Forms.Panel()
		self._panel4 = System.Windows.Forms.Panel()
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._radioButton4 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._panel1.SuspendLayout()
		self._panel2.SuspendLayout()
		self._panel3.SuspendLayout()
		self._panel4.SuspendLayout()
		self.SuspendLayout()
		# 
		# panel1
		# 
		self._panel1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel1.Controls.Add(self._radioButton4)
		self._panel1.Controls.Add(self._radioButton3)
		self._panel1.Controls.Add(self._radioButton2)
		self._panel1.Controls.Add(self._radioButton1)
		self._panel1.ForeColor = System.Drawing.Color.White
		self._panel1.Location = System.Drawing.Point(10, 13)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(203, 118)
		self._panel1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(84, 281)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 2
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(180, 281)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(277, 281)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		# 
		# panel2
		# 
		self._panel2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel2.Controls.Add(self._checkBox3)
		self._panel2.Controls.Add(self._checkBox2)
		self._panel2.Controls.Add(self._checkBox1)
		self._panel2.ForeColor = System.Drawing.Color.White
		self._panel2.Location = System.Drawing.Point(219, 13)
		self._panel2.Name = "panel2"
		self._panel2.Size = System.Drawing.Size(203, 118)
		self._panel2.TabIndex = 1
		# 
		# panel3
		# 
		self._panel3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel3.Controls.Add(self._label5)
		self._panel3.Controls.Add(self._label4)
		self._panel3.Controls.Add(self._label3)
		self._panel3.Controls.Add(self._label2)
		self._panel3.ForeColor = System.Drawing.Color.White
		self._panel3.Location = System.Drawing.Point(219, 137)
		self._panel3.Name = "panel3"
		self._panel3.Size = System.Drawing.Size(203, 118)
		self._panel3.TabIndex = 3
		# 
		# panel4
		# 
		self._panel4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._panel4.Controls.Add(self._label1)
		self._panel4.Controls.Add(self._textBox1)
		self._panel4.ForeColor = System.Drawing.Color.White
		self._panel4.Location = System.Drawing.Point(10, 137)
		self._panel4.Name = "panel4"
		self._panel4.Size = System.Drawing.Size(203, 118)
		self._panel4.TabIndex = 2
		# 
		# radioButton1
		# 
		self._radioButton1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton1.ForeColor = System.Drawing.Color.Black
		self._radioButton1.Location = System.Drawing.Point(28, 3)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(145, 25)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "Standard Adult"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton2.ForeColor = System.Drawing.Color.Black
		self._radioButton2.Location = System.Drawing.Point(28, 33)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(170, 25)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "Child (12 and under)"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton3.ForeColor = System.Drawing.Color.Black
		self._radioButton3.Location = System.Drawing.Point(28, 63)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(145, 25)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "Student"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# radioButton4
		# 
		self._radioButton4.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._radioButton4.ForeColor = System.Drawing.Color.Black
		self._radioButton4.Location = System.Drawing.Point(28, 93)
		self._radioButton4.Name = "radioButton4"
		self._radioButton4.Size = System.Drawing.Size(145, 25)
		self._radioButton4.TabIndex = 3
		self._radioButton4.TabStop = True
		self._radioButton4.Text = "Senior Citizen"
		self._radioButton4.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox1.ForeColor = System.Drawing.Color.Black
		self._checkBox1.Location = System.Drawing.Point(14, 15)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(161, 24)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "Yoga"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox2.ForeColor = System.Drawing.Color.Black
		self._checkBox2.Location = System.Drawing.Point(14, 45)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(161, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "Karate"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._checkBox3.ForeColor = System.Drawing.Color.Black
		self._checkBox3.Location = System.Drawing.Point(14, 75)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(161, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "Personal Trainer"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(58, 74)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(77, 25)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.ForeColor = System.Drawing.Color.Black
		self._label1.Location = System.Drawing.Point(48, 31)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 40)
		self._label1.TabIndex = 1
		self._label1.Text = "Enter the # of Months"
		# 
		# label2
		# 
		self._label2.ForeColor = System.Drawing.Color.Black
		self._label2.Location = System.Drawing.Point(3, 31)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 2
		self._label2.Text = "Monthly Fee:"
		# 
		# label3
		# 
		self._label3.ForeColor = System.Drawing.Color.Black
		self._label3.Location = System.Drawing.Point(50, 63)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(54, 23)
		self._label3.TabIndex = 3
		self._label3.Text = "Total:"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.ForeColor = System.Drawing.Color.Black
		self._label4.Location = System.Drawing.Point(98, 31)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(66, 23)
		self._label4.TabIndex = 4
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.ForeColor = System.Drawing.Color.Black
		self._label5.Location = System.Drawing.Point(98, 63)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(66, 23)
		self._label5.TabIndex = 5
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(432, 316)
		self.Controls.Add(self._panel3)
		self.Controls.Add(self._panel4)
		self.Controls.Add(self._panel2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._panel1)
		self.Font = System.Drawing.Font("Microsoft YaHei", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self.Name = "MainForm"
		self.Text = "Pg250MembershipFee"
		self._panel1.ResumeLayout(False)
		self._panel2.ResumeLayout(False)
		self._panel3.ResumeLayout(False)
		self._panel4.ResumeLayout(False)
		self._panel4.PerformLayout()
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		months = int(self._textBox1.Text)
			
		if self._radioButton1.Checked == True:
			base_fee = 40
		if self._radioButton2.Checked == True:
			base_fee = 20
		if self._radioButton3.Checked == True:
			base_fee = 25
		if self._radioButton4.Checked == True:
			base_fee = 30
		if self._checkBox1.Checked == True:
			yoga = 10
		if self._checkBox1.Checked == False:
			yoga = 0
		if self._checkBox2.Checked == True:
			karate = 30
		if self._checkBox2.Checked == False:	
			karate = 0	
		if self._checkBox3.Checked == True:
			personal_trainer = 50
		if self._checkBox3.Checked == False:
			personal_trainer = 0	
		if months <= 3:
			discount = 0
		if months >= 4 and months <= 6:
			discount = base_fee * 0.05
		elif months >= 7 and months <= 9:
			discount = base_fee * 0.08
		elif months >= 0:
			discount = base_fee * 0.1
		else:
			pass
			
		monthly_fee = base_fee + yoga + karate + personal_trainer
		
		total = (monthly_fee * months) - discount
		
		self._label4.Text = str(monthly_fee)
		
		self._label5.Text = str(total)
		
		
		

		