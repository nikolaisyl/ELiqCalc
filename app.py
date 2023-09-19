import sys
import typing
from PyQt6 import QtCore
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton,
    QLineEdit, QVBoxLayout, QTextEdit
)
from PyQt6.uic.load_ui import loadUi


class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        loadUi('ui.ui', self)
        self.setWindowTitle('E-Liquid Calculator')
        self.pushButton.clicked.connect(self.calculate)

    def calculate(self) -> None:
        pass


app = QApplication([])

window = MyApp()
window.show()

app.exec()
