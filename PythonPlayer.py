# ui imports
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QLabel, QInputDialog, QFileDialog

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
        self.setFixedSize(1300,750)
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
        back.resize(650, 50)
        back.move(0, 350)


        # creates a play button
        self.pButton = QPushButton('', self)
        self.pButton.move(280, 360)
        self.pButton.setCheckable(True)
        self.pButton.clicked.connect(self.pButton_clicked)
        self.pButton.clicked.connect(self.playAudio)
        self.pButton.setStyleSheet(playStyle)
        self.pButton.setIcon(QIcon('playButton.ico'))

        # creates a file button
        self.fButton = QPushButton('', self)
        self.fButton.move(420, 460)
        self.fButton.setCheckable(True)
        self.fButton.clicked.connect(self.fButton_clicked)
        #self.pButton.clicked.connect(self.playAudio)
        self.fButton.setStyleSheet(fStyle)
        #self.pButton.setIcon(QIcon('playButton.ico'))

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
    
    def fButton_clicked(self): 


        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Audio files (*.mp3 *.wav)")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        print()
        #it spits out ('C:/Users/Ian/OneDrive/Documents/VScode Projects/music.mp3', 'All Files (*)') rather tha just the file name so the media player does not recongnize the file address
        '''
        full_file_path = os.path.join(os.getcwd(), fname)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMuted(False)
        self.player.setMedia(content)
        self.player.play()'''

    # audio player
    def playAudio(self):  
        full_file_path = os.path.join(os.getcwd(), 'fname')
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)

        self.player.setMedia(content)
        self.player.play()



playStyle = "background-color : green; border: 2px solid black"
fStyle = "background-color : light-gray; border 2px solid black"
titleStyle = "font-family: gothom, sans-serif;font-size: 20px; color: white"
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())

