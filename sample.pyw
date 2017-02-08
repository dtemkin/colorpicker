# coding:utf-8
from __future__ import division, print_function, unicode_literals, absolute_import
# noinspection PyUnresolvedReferences
from future_builtins import *

import sys

from PySide.QtGui import *
from PySide.QtCore import *

from colorpicker.QColorBarWidget import *
from colorpicker.QHueCircleWidget import *
from colorpicker.QColorSetWidget import *

#
# Main
#
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def setup(self):
        self.resize(400, 400)

        self.circleWidget = QHueCircleWidget(self)
        self.circleWidget.move(10, 10)

        self.colorBar = QColorBarWidget(self, 0)
        self.colorBar.move(10, 220)
        self.colorBar.resize(200, 20)

        self.colorSetWidget = QColorSetWidget(self)
        self.colorSetWidget.move(10, 250)

        self.colorBar.colorChanged.connect(self.onUpdateColorFromBar)
        self.colorSetWidget.colorChanged.connect(self.onUpdateColorFromSet)
        self.circleWidget.colorChanged.connect(self.onUpdateColorFromCircle)

    @Slot()
    def onUpdateColorFromBar(self):
        color = self.colorBar.getColor()
        self.colorSetWidget.setColor(color)
        self.circleWidget.setColor(color)

    @Slot()
    def onUpdateColorFromSet(self):
        color = self.colorSetWidget.getColor()
        self.circleWidget.setColor(color)
        self.colorBar.setColor(color)

    @Slot()
    def onUpdateColorFromCircle(self):
        color = self.circleWidget.getColor()
        self.colorSetWidget.setColor(color)
        self.colorBar.setColor(color)

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.resize(500, 500)
    main_window.setWindowTitle('QtSample')
    main_window.setup()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
