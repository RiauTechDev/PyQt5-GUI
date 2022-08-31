from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import sys

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# Load the ui file
		uic.loadUi("cal_34.ui", self)

		# Define our widgets

		# Show The App
		self.show()

# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()