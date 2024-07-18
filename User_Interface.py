import sys
from PyQt5 import QtWidgets, QtGui
import qdarktheme
from PyQt5.QtWidgets import QPushButton, QApplication, QWidget, QVBoxLayout, QLabel


class ToggleSwitch(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setChecked(False)
        self.setText('OFF')
        self.clicked.connect(self.toggle_state)

    def toggle_state(self):
        if self.isChecked():
            self.setText('ON')
        else:
            self.setText('OFF')


app= QtWidgets.QApplication(sys.argv)
qdarktheme.enable_hi_dpi()
window = QWidget()
top_sec = QVBoxLayout()

layout = QVBoxLayout()

label = QLabel("Press button to Activate kevin")

switch = ToggleSwitch()
top_sec.addWidget(switch)
top_sec.addWidget(label)
layout.addWidget(top_sec)


window.setLayout(layout)
window.resize(500,500)
window.move(100,100)
window.setWindowTitle('Voice_Automate')
window.setWindowIcon(QtGui.QIcon('newicon.ico'))
window.show()
app.exec_()



