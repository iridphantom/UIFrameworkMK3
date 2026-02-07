import os
import logging
import logging.config

from datetime import datetime

# 日志配置文件路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
LOG_CONF_PATH = os.path.join(BASE_DIR, "utils", "logger", "log_conf.ini")

# 是否已经初始化过 logging（防止重复加载）
_is_configured = False


def get_logger(name="uiLogger"):
    global _is_configured

    if not _is_configured:
        log_dir = os.path.join(BASE_DIR, "logs")
        os.makedirs(log_dir, exist_ok=True)

        today = datetime.now().strftime("%Y-%m-%d")
        ui_log = os.path.join(log_dir, f"{today}_ui_test.log").replace("\\", "/")
        error_log = os.path.join(log_dir, f"{today}_error.log").replace("\\", "/")

        logging.config.fileConfig(
            LOG_CONF_PATH,
            encoding="utf-8",
            disable_existing_loggers=False,
            defaults={
                "ui_log": ui_log,
                "error_log": error_log
            }
        )
        _is_configured = True

    return logging.getLogger(name)
