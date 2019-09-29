from extensoes.Dependencies import *


class FormulaInputClass(QLineEdit):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLineEdit.mousePressEvent(self, event)






