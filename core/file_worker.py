from PySide6.QtCore import QObject, Signal


class FileWorker(QObject):
    finished = Signal(str)
    progress = Signal(str)

    file = ''
    filename = ''
    path = ''

    def setup_data(self, file, filename, path):
        self.file = file
        self.filename = filename
        self.path = path

    
    def doWork(self):
        print("Working...")
        print(self.file)
        print(self.filename)

        