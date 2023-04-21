from datetime import datetime

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