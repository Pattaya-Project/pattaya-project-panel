from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt,QUrl
from designer.ui_about_pattaya import Ui_AboutPattayaWidget
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput


class AboutPattayaWidget(QWidget, Ui_AboutPattayaWidget):
    def __init__(self):
        super().__init__()        
        
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setSource(QUrl('qrc:/assets/sound/Reloaded.mp3'))
        self.player.setAudioOutput(self.audio)
        self.audio.setVolume(50)
        self.setupUi(self)    

    def closeEvent(self, event):
        self.player.stop()

    def play_sound(self):
        self.player.play()

