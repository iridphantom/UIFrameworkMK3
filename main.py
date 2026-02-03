import unittest
from datetime import datetime

from utils.logger import setup_logger
from utils.report import HtmlTestRunner


if __name__ == "__main__":
    logger = setup_logger("ui-framework", "logs/ui-framework.log")
    logger.info("Discovering tests...")

    suite = unittest.defaultTestLoader.discover("test_cases")
    report_name = datetime.now().strftime("reports/ui-report-%Y%m%d-%H%M%S.html")

    logger.info("Running tests...")
    runner = HtmlTestRunner(report_path=report_name, title="UI Automation Report")
    result = runner.run(suite)

    logger.info(
        "Finished. Total=%s Failures=%s Errors=%s Skipped=%s",
        result.testsRun,
        len(result.failures),
        len(result.errors),
        len(result.skipped),
    )
