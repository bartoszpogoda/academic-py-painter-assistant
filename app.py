import sys
from PyQt5.QtWidgets import QApplication, QDialog
import painterAssistant.paintCanCalculator as canCalculator

from window import Ui_Dialog


class HelloWindow(QDialog):
    def __init__(self):
        super(HelloWindow, self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Painter assistant app")

        self.ui.btnCalculate.clicked.connect(self.onCalculateBtnClicked)

    def onCalculateBtnClicked(self):
        try:
            width = float(self.ui.tbWidth.text())
            height = float(self.ui.tbHeight.text())
            efficiency = float(self.ui.tbEfficiency.text())

            result = canCalculator.how_many_needed(width, height, efficiency)
            self.ui.lblResult.setText(str(result))
        except ValueError:
            self.ui.lblResult.setText('-')


app = QApplication(sys.argv)
widget = HelloWindow()
widget.show()
sys.exit(app.exec_())


