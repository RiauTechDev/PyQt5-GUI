from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
from PyQt5 import uic
import sys
from PyQt5.QtCore import QTime, QTimer
from datetime import datetime

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("lcd_35.ui", self)

		# Define our widgets
		self.lcd = self.findChild(QLCDNumber, "lcdNumber")

		# Create A Timer
		self.timer = QTimer()
		self.timer.timeout.connect(self.lcd_number)

		# Start the timer and update every second
		self.timer.start(1)

		# Call the lcd function
		self.lcd_number()

		# Show The App
		self.show()

	
	def lcd_number(self):
		# Get the time
		time = datetime.now()
		formatted_time = time.strftime("%I:%M:%S:%f")
		formatted_time = formatted_time[:-3]
		ampm = time.strftime(" %p")

		# Set number of LCD Digits
		self.lcd.setDigitCount(16)
		# Make Text Flat (no white outline)
		self.lcd.setSegmentStyle(QLCDNumber.Flat)

		# Display The Time
		self.lcd.display(f'{formatted_time}{ampm}')

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()