import sys
from PyQt5.QtWidgets import QApplication, QDialog, QErrorMessage

import painterAssistant.paintCanCalculator as canCalculator
import roomBuilder.room as room

from window import Ui_Dialog


class HelloWindow(QDialog):
    def __init__(self):
        super(HelloWindow, self).__init__()

        self.roomBuilder = room.RoomBuilder()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWindowTitle("Painter assistant app")

        self.ui.btnCalculate.clicked.connect(self.onCalculateBtnClicked)
        self.ui.btnAddWall.clicked.connect(self.onAddWallBtnClicked)
        self.ui.btnResetRoom.clicked.connect(self.onResetRoomBtnClicked)

    def onResetRoomBtnClicked(self):
        self.roomBuilder = room.RoomBuilder()
        self.ui.tbTotalSurface.setText('')

    def onAddWallBtnClicked(self):
        try:
            width = float(self.ui.tbWidth.text())
            height = float(self.ui.tbHeight.text())

            self.roomBuilder.add_wall(width, height)
            self.ui.tbTotalSurface.setText(str(round(self.roomBuilder.current_total_surface, 2)))
        except ValueError:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Some error occurred. Please validate your data.')
            error_dialog.exec()

    def onCalculateBtnClicked(self):
        try:
            efficiency = float(self.ui.tbEfficiency.text())
            min_excess = float(self.ui.tbMinExcess.text())

            calculator = canCalculator.PaintCanNeededCalculator()
            calculator.set_min_excess(min_excess)
            calculator.set_paint_can_efficiency(efficiency)

            result_cans_needed, total_excess = calculator.calculate(self.roomBuilder.build())

            self.ui.lblResult.setText(str(result_cans_needed))
            self.ui.lblExcessResult.setText(str(round(total_excess, 2)))
        except ValueError:
            error_dialog = QErrorMessage()
            error_dialog.showMessage('Some error occurred. Please validate your data.')
            error_dialog.exec()


app = QApplication(sys.argv)
widget = HelloWindow()
widget.show()
sys.exit(app.exec_())


