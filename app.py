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
        base = float(self.lineEdit.text())
        nic_str = float(self.lineEdit_2.text())
        booster_str = float(self.lineEdit_3.text())
        total_flavor_percentage = float(self.lineEdit_4.text())

        nic_ans = (base * nic_str) / booster_str
        flavors_ans = (total_flavor_percentage * base) / 100
        base_ans = base - (nic_ans + flavors_ans)

        self.textEdit.setText(f'Booster: {nic_ans:.1f} ml \n'+
                              f'Flavors: {flavors_ans:.1f} ml \n'+
                              f'Base: {base_ans:.1f} ml \n')


app = QApplication([])

window = MyApp()
window.show()

app.exec()
