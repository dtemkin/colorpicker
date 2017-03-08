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
from colorpicker.QColorPaletteWidget import *

#
# Main
#
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

    def setup(self):
        self.resize(400, 440)

        self.circleWidget = QHueCircleWidget(self)
        self.circleWidget.move(10, 10)

        self.colorBar = QColorBarWidget(self, 0)
        self.colorBar.move(10, 220)
        self.colorBar.resize(200, 20)

        self.setWidget = QColorSetWidget(self)
        self.setWidget.move(10, 250)
        # self.setWidget.resize(200, 70)

        self.paletteWidget = QColorPaletteWidget(self)
        self.paletteWidget.move(10, 330)
        # self.paletteWidget.resize(180+2, 100+2)

        color = QColor(255, 0, 0, 255)
        self.circleWidget.setColor(color)
        self.colorBar.setColor(color)
        self.paletteWidget.setColor(color)
        self.setWidget.setColor(color)

        self.colorBar.colorChanged.connect(self.onUpdateColorFromBar)
        self.setWidget.colorChanged.connect(self.onUpdateColorFromSet)
        self.circleWidget.colorChanged.connect(self.onUpdateColorFromCircle)
        self.paletteWidget.colorChanged.connect(self.onUpdateColorFromPalette)

    @Slot()
    def onUpdateColorFromBar(self):
        color = self.colorBar.getColor()
        self.circleWidget.setColor(color)
        self.paletteWidget.setColor(color)
        self.setWidget.setColor(color)

    @Slot()
    def onUpdateColorFromSet(self):
        color = self.setWidget.getColor()
        self.circleWidget.setColor(color)
        self.colorBar.setColor(color)
        self.paletteWidget.setColor(color)

    @Slot()
    def onUpdateColorFromCircle(self):
        color = self.circleWidget.getColor()
        self.colorBar.setColor(color)
        self.paletteWidget.setColor(color)
        self.setWidget.setColor(color)

    def onUpdateColorFromPalette(self):
        color = self.paletteWidget.getColor()
        self.circleWidget.setColor(color)
        self.setWidget.setColor(color)
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
