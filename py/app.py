import sys
from tkinter.tix import ButtonBox

from partRunTime import runTimeLeft
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton
)


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets App")

        partsLeft = QLineEdit
        timePerPart = QLineEdit
        button = QPushButton
        

        layout = QVBoxLayout()
        widgets = [
            partsLeft,
            timePerPart,
            button
        ]

        for w in widgets:
            layout.addWidget(w())

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

runTimeLeft(32,12)