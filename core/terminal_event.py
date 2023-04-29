from typing import Optional
from PySide6.QtCore import QObject,Signal


class TerminalEvent(QObject):
    on_close_terminal = Signal(int)

    def close_terminal(self):
        self.on_close_terminal.emit(0)