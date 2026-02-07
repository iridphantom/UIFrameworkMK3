import unittest

from utils.logger.get_logger import get_logger

if __name__ == '__main__':
    logger = get_logger("uiLogger")
    logger.info("开始执行自动化测试用例")
    unittest.main()