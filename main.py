import sys
from PyQt5 import uic, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog, QDialog, QInputDialog, QMessageBox

from dialog import Ui_dialog
from start import Ui_MainWindow

SCREEN_SIZE = [1920, 1080]


# class Dialog(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)
#         # self.Yes_button.setStyleSheet(self.stylesheet)
#         # self.No_button.setStyleSheet(self.stylesheet)
#         # self.Yes_button.clicked.connect(self.hero_chosed)
#         # self.No_button.clicked.connect(self.run)
#     def initUI(self):


class Start(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resize(*SCREEN_SIZE)
        self.setStyleSheet("""
                            QMainWindow {
                                background-image: url("img/main.jpg");
                                background-repeat: no-repeat; 
                                background-position: center;
                            }
                        """)
        self.stylesheet = """QPushButton{font-style: oblique;
                                    font-weight: bold;
                                    border: 1px solid #1DA1F2;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: #fff;
                                }
                                """
        self.pushButton.setStyleSheet(self.stylesheet)
        self.pushButton_2.setStyleSheet(self.stylesheet)
        self.pushButton.clicked.connect(self.run)

    def reverse(self):
        uic.loadUi("ui/start.ui", self)
        self.pushButton.setStyleSheet(self.stylesheet)
        self.pushButton_2.setStyleSheet(self.stylesheet)
        self.pixmap = QPixmap('img/avatar.png')
        self.label.setPixmap(self.pixmap)
        self.pushButton.clicked.connect(self.run)

    # def create_button(self, dialog, title, message):
    #     command = lambda: print(dialog(title, message))
    #     btn = tk.Button(self, text=title, command=command)
    #     btn.pack(padx=40, pady=5, expand=True, fill=tk.BOTH)

    def run(self):
        uic.loadUi("ui/chose_hero.ui", self)
        self.ReverseButton.setStyleSheet(self.stylesheet)
        self.ReverseButton.clicked.connect(self.reverse)
        self.radioButton.clicked.connect(self.confirmation)
        self.radioButton_2.clicked.connect(self.confirmation)
        self.radioButton_3.clicked.connect(self.confirmation)
        self.radioButton_4.clicked.connect(self.confirmation)

    def confirmation(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Начать игру?")
        msgBox.setText("")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        ret = msgBox.exec_()

        if ret == QMessageBox.Yes:
            self.hero_chosed()
        if ret == QMessageBox.No:
            self.run()

    def hero_chosed(self):
        uic.loadUi("ui/play.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec_())
