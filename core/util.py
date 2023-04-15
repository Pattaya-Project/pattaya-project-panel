from datetime import datetime

class PattayaPanelUtil:

    @staticmethod
    def setup(qtext_browser):
        PattayaPanelUtil._panel_log_viewer_instance = qtext_browser
    
    @staticmethod
    def panel_log_info(message):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        PattayaPanelUtil._panel_log_viewer_instance.append(f'<p style="color: #33FF52;">[{formatted_time}] - [INFO] - [{message}]</p>')

    @staticmethod
    def panel_log_error(message):
        current_time = datetime.now()
        formatted_time = current_time.strftime('%d:%m:%Y %H:%M:%S')
        PattayaPanelUtil._panel_log_viewer_instance.append(f'<p style="color: #E50A0A;">[{formatted_time}] - [ERROR] - [{message}]</p>')