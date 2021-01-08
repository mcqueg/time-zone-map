# Creator: Garrett McCue
# Filename:  timezone.py
"""
this is a basic app showing the current time for each
time zone in the United States using PyQt5
"""

import sys
import pytz

from datetime import datetime
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QTimer, QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QIcon, QPixmap


class Window(QWidget):
    # constructor
    def __init__(self):
        QWidget.__init__(self)
        # set window title
        self.title = 'America\'s Big Ole Clock'
        # initialize getWindow to get time and date
        self.getWindow()


    # generate/update gui and call secondary functions
    def getWindow(self):
        self.setWindowTitle(self.title)
        self.get_map()
        self.get_date()
        self.get_time_zones()

        self.show()

    def get_map(self):
        # set the map as the background
        label = QLabel(self)
        pixmap = QPixmap('map.jpeg')
        label.setPixmap(pixmap)
        # reshape window to fit image
        label.setScaledContents(True)
        self.resize(pixmap.width(), pixmap.height())

        return self

    def get_date(self):
        # get date and reformat
        today = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        date = QLabel('<h1> %s <h1>' % today, parent=self)
        date.move(600, 500)

        return self

    def get_time_zones(self):
        # get current time
        now = QTime.currentTime()

        cst_time = now.toString('h:m')
        cst_label = QLabel('<h2> %s <h2>' % cst_time, parent=self)
        cst_label.move(390, 70)

        '''
        est_time = (now[0] + 1).toString('h:m:s')
        est_label = QLabel('<h2> %s <h2>' % est_time, parent=self)
        est_label.move(670, 400)
        '''

        # update/place est on window
        # est = QLabel('<h4> %s <h4>' % label_time, parent=self)
        # est.move(670, 400)

        return self


if __name__ == "__main__":
    # initialize app
    app = QApplication(sys.argv)
    # set up GUI and run applications event log
    gui = Window()
    # gui.show()
    # app.exec_()
    sys.exit(app.exec())
