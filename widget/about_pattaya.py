from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt,QUrl
from designer.ui_about_pattaya import Ui_AboutPattayaWidget
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput


class AboutPattayaWidget(QWidget, Ui_AboutPattayaWidget):
    def __init__(self):
        super().__init__()        
        self.setupUi(self)
        
        self.player = QMediaPlayer()
        self.audio = QAudioOutput()
        self.player.setSource(QUrl('qrc:/assets/sound/Reloaded.mp3'))
        self.audio.setVolume(0.5)

        self.player.setAudioOutput(self.audio)

    def closeEvent(self, event):
        self.player.stop()

    def play_sound(self):
        self.player.play()

