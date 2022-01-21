from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5 import QtCore
import sys, os


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.player.setVolume(100)
        self.songname = ""

    def initUI(self):

        self.player = QMediaPlayer()    

        vbox = QVBoxLayout()
        hbox0 = QHBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        self.title = QLabel(self)
        self.title.setText("")
        self.title.setStyleSheet(titleStyle)
        hbox0.addWidget(self.title, alignment=QtCore.Qt.AlignCenter)

        pixmap = QPixmap("")
        cover = QLabel(self)
        cover.setPixmap(pixmap)
        cover.resize(pixmap.width(), pixmap.height())
        hbox1.addWidget(cover, alignment=QtCore.Qt.AlignCenter)

        self.prgsBar = QSlider(Qt.Horizontal)
        self.prgsBar.setRange(0, 0)
        self.prgsBar.setFixedWidth(500)
        self.player.durationChanged.connect(self.duration_changed)
        self.player.positionChanged.connect(self.position_changed)


        vbox.addLayout(hbox0)
        vbox.addLayout(hbox1)
        vbox.addWidget(self.prgsBar, alignment=QtCore.Qt.AlignCenter)
        vbox.addLayout(hbox2)

        sld = QSlider(Qt.Horizontal, self)
        sld.setRange(0, 100)
        sld.setValue(100)
        sld.setMaximumWidth(200)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setPageStep(5)

        sld.valueChanged.connect(self.updateLabel)

        self.fButton = QPushButton("Import")
        self.fButton.clicked.connect(self.fButton_clicked)

        self.pButton = QPushButton("", self)
        self.pButton.setIcon(QIcon('playButton.ico'))
        self.pButton.setCheckable(True)
        self.pButton.clicked.connect(self.pButton_clicked)

        hbox2.addWidget(self.fButton)
        hbox2.addSpacing(50)
        hbox2.addWidget(self.pButton)
        hbox2.addSpacing(50)
        hbox2.addWidget(sld)

        
        self.setLayout(vbox)

        self.setGeometry(400, 300, 800, 450)
        self.setWindowTitle('Python Music Player')
        self.show()

    def updateLabel(self, value):
    
        self.player.setVolume(value)

    def fButton_clicked(self):

        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Audio files (*.mp3 *.wav)")
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        songname = fname[0]
        print(songname)
        songTitle = songname[23:-4]
        print(songTitle)
        self.title.setText(songTitle)
        full_file_path = os.path.join(os.getcwd(), songname)
        url = QUrl.fromLocalFile(full_file_path)
        content = QMediaContent(url)
        self.player.setMedia(content)

    def pButton_clicked(self):
            
        # sets color to red when pressed
        if self.pButton.isChecked():
            self.pButton.setIcon(QIcon('pause.ico'))
            self.player.play()
        
        # pause button changes color and mutes music
        else:
            self.pButton.setIcon(QIcon('playButton.ico'))
            self.player.pause()

    def position_changed(self, position):
        self.prgsBar.setValue(position)

    def duration_changed(self, duration):
        self.prgsBar.setRange(0, duration)

titleStyle = "font-family: gothom, sans-serif;font-size: 20px; color: black"

def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()