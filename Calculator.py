import os
import sys
import math
from PyQt5 import QtCore, QtGui, uic, QtWidgets
from functools import partial

qtCreatorFile = "AppGui.ui"
if os.path.isfile ( qtCreatorFile ):
	# Use AppGui.ui file for debug
	Ui_MainWindow, QtBaseClass = uic.loadUiType ( qtCreatorFile )
else:
	# Use converted AppGui.py file for release
	from AppGui import Ui_MainWindow


class Calculator ( QtWidgets.QMainWindow, Ui_MainWindow ):
	'''
	Calculator application.
	'''
	def __init__ ( self ):
		QtWidgets.QMainWindow.__init__ ( self )
		Ui_MainWindow.__init__ ( self )
		self.setupUi ( self )
		self.setWindowFlags ( QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint |
		                      QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowStaysOnTopHint |
		                      QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint )

		self.listButtons = [ self.btn0,    self.btn1,     self.btn2,        self.btn3,
							 self.btn4,    self.btn5,     self.btn6,        self.btn7,
							 self.btn8,    self.btn9,     self.btnDot,
							 self.btnPlus, self.btnMinus, self.btnMultiply, self.btnDivide,
							 self.btnDel,  self.btnAc,    self.btnEqual,    self.btnSquareRoot ]

		for index in range ( 15 ):
			# for some reason, lamda doesn't work here but partial works
			#self.listButtons [ index ].clicked.connect ( lambda: self.cbBtnNumberClicked ( self.listButtons [ index ].text () ) )
			self.listButtons [ index ].clicked.connect ( partial ( self.cbBtnNumberClicked, self.listButtons [ index ].text () ) )

		self.btnDel.clicked.connect ( self.cbBtnDelClicked )
		self.btnAc.clicked.connect ( self.cbBtnAcClicked )
		self.btnEqual.clicked.connect ( self.cbBtnEqualClicked )
		self.btnSquareRoot.clicked.connect ( self.cbBtnSquareRootClicked )

	def cbBtnNumberClicked ( self, text ):
		current_value = self.txtResult.text ()
		new_value = current_value + str ( text )
		self.txtResult.setText ( new_value )

	def cbBtnEqualClicked ( self ):
		result = eval ( self.txtResult.text () )
		self.txtResult.setText ( str ( result ) )

	def cbBtnAcClicked ( self ):
		self.txtResult.setText ( "" )

	def cbBtnDelClicked ( self ):
		current_value = self.txtResult.text ()
		self.txtResult.setText ( current_value[:-1] )

	def cbBtnSquareRootClicked ( self ):
		value = float ( self.txtResult.text () )
		self.txtResult.setText ( str ( math.sqrt ( value ) ) )



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	window = Calculator()
	window.show()
	sys.exit(app.exec_())
