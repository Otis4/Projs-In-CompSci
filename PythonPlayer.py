# ui imports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel

# image imports
from PyQt5.QtGui import QIcon, QPixmap

# audio imports
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
import sys, os

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # sets parameters of window
        #why are these variables, they arent even constants
        x = 650
        y = 400
        xpos = 635
        ypos = 340
        self.setGeometry(xpos, ypos, x, y) # just put in the numbers you want
        self.setWindowTitle("Epic Music Player")
        self.setWindowIcon(QIcon('playButton.ico'))
        self.setStyleSheet("background-color: #202020;")

        # creates a label
        label = QtWidgets.QLabel(self)
        label.setText("Epic Music")
        label.setStyleSheet(titleStyle)
        label.move(200, 15)

        # kanye pic
        pixmap = QPixmap("kanye-face.gif")
        kPic = QLabel(self)
        kPic.setPixmap(pixmap)
        kPic.resize(pixmap.width(), pixmap.height())
        kPic.move(20, 50)

        back = QLabel(self)
        back.setStyleSheet("background-color: #262626;")
        back.resize(650, 50)# why not use the variables you created here
        back.move(0, 350)

        # creates a button
        self.pButton = QPushButton('', self)
        self.pButton.move(280, 360)
        self.pButton.setCheckable(True)
        self.pButton.clicked.connect(self.pButton_clicked)
        self.pButton.clicked.connect(self.playAudio)
        self.pButton.setStyleSheet(playStyle)
        self.pButton.setIcon(QIcon('playButton.ico'))

        # sets volume -add a slider-
        self.player = QMediaPlayer()
        self.player.setVolume(50)
        
        # shows the window
        self.update()
        self.show()

    # defines what happens when button is pressed -spaghetti code rn-
    def pButton_clicked(self):

        # sets color to red when pressed
        if self.pButton.isChecked():
            self.pButton.setIcon(QIcon('pause.ico'))
            self.pButton.setStyleSheet("background-color : red; border: 2px solid black")
            self.player.setMuted(False)
        
        # pause button changes color and mutes music
        else:
            self.pButton.setStyleSheet(playStyle)
            self.pButton.setIcon(QIcon('playButton.ico'))
            self.player.setMuted(True)


    # audio player
    def playAudio(self):  
        full_file_path = os.path.join(os.getcwd(), 'Pursuit_of_happiness.mp3')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()



playStyle = "background-color : green; border: 2px solid black"
titleStyle = "font-family: gothom, sans-serif;font-size: 20px; color: white"
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())

