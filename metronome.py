from PyQt5 import QtCore, QtGui, QtWidgets
from metronome_ui import Ui_MainWindow
from time import sleep
import sys
import pyttsx3

class MetronomeApp(QtWidgets.QMainWindow):

    def __init__(self):

        super(MetronomeApp, self).__init__()

        self.qt = Ui_MainWindow()

        self.qt.setupUi(self)

        self.qt.retranslateUi(self)

        self.add_func()

        self.engine = pyttsx3.init()

    def play_sound(self):

        try:

            delay = float(self.qt.textEdit.toPlainText())

            while True:

                sleep(delay)

                self.engine.say("Bip")

                self.engine.runAndWait()

        except ValueError:

            self.qt.textEdit.setText("You\'ve wrote not a number")

    def stop_program(self):

        exit()

    def add_func(self):

        self.qt.pushButton.clicked.connect(self.play_sound)

        self.qt.pushButton_2.clicked.connect(self.stop_program)

def app():

    app = QtWidgets.QApplication(sys.argv)

    window = MetronomeApp()

    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    app()
