import sys
# from PyQt5 import uic  # Импортируем uic
# from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QFileDialog
# from chose_hero import Chose_hero
# from technik import technik
# from play import play
from start import Ui_MainWindow


class Start(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        stylesheet = """
                            QMainWindow {
                                background-image: url("img.jpg");
                                background-repeat: no-repeat; 
                                background-position: center;
                            }
                        """
        self.setStyleSheet(stylesheet)
        self.pushButton.setStyleSheet("""
                                QPushButton{
                                    font-style: oblique;
                                    font-weight: bold;
                                    border: 1px solid #1DA1F2;
                                    border-radius: 15px;
                                    color: #1DA1F2;
                                    background-color: #fff;
                                }
                                """)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        uic.loadUi("chose_hero.ui", self)
        self.radioButton.clicked.connect(self.hero_chosed)
        self.radioButton_2.clicked.connect(self.hero_chosed)
        self.radioButton_3.clicked.connect(self.hero_chosed)
        self.radioButton_4.clicked.connect(self.hero_chosed)


    def hero_chosed(self):
        uic.loadUi("play.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Start()
    ex.show()
    sys.exit(app.exec_())
