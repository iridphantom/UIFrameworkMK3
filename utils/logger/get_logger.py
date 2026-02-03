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
    """
    获取 logger 实例
    :param name: logger 名称，对应 log_conf.ini 中的 qualname
    """
    global _is_configured

    if not _is_configured:
        # 确保 logs 目录存在
        log_dir = os.path.join(BASE_DIR, "logs")
        os.makedirs(log_dir, exist_ok=True)

        # 当前日期
        today = datetime.now().strftime("%Y-%m-%d")
        ui_log = os.path.join(log_dir, f"{today}_ui_test.log")
        error_log = os.path.join(log_dir, f"{today}_error.log")
        logging.config.fileConfig(
            LOG_CONF_PATH,
            disable_existing_loggers=False,
            defaults={
                "ui_log": ui_log,
                "error_log": error_log
            }
        )
        _is_configured = True

    return logging.getLogger(name)
