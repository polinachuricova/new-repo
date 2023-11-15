import io
import sys

from PyQt5 import uic 
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5.QtGui import QPainter, QColor

from random import randint


template = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>141</width>
      <height>61</height>
     </rect>
    </property>
    <property name="text">
     <string>кнопка</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
"""


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self) 
        self.initUI()

    def initUI(self):
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        qp.setBrush(QColor(255, 210, 133))
        qp.drawEllipse(100, 100, randint(10, 300), randint(10, 300))
        qp.setBrush(QColor(255, 191, 82))
        qp.drawEllipse(200, 200, randint(10, 300), randint(10, 300))
        qp.setBrush(QColor(255, 250, 13))
        qp.drawEllipse(300, 300, randint(10, 300), randint(10, 300))
        qp.setBrush(QColor(255, 215, 0))
        qp.drawEllipse(150, 350, randint(10, 300), randint(10, 300))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())