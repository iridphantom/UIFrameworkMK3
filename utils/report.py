from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable


@dataclass
class TestCaseResult:
    name: str
    outcome: str
    details: str | None = None


def _collect_case_results(result) -> list[TestCaseResult]:
    failures = {case.id(): detail for case, detail in result.failures}
    errors = {case.id(): detail for case, detail in result.errors}
    skipped = {case.id(): detail for case, detail in result.skipped}

    case_results: list[TestCaseResult] = []
    for test in result.testsRunList:
        test_id = test.id()
        if test_id in failures:
            case_results.append(TestCaseResult(test_id, "FAIL", failures[test_id]))
        elif test_id in errors:
            case_results.append(TestCaseResult(test_id, "ERROR", errors[test_id]))
        elif test_id in skipped:
            case_results.append(TestCaseResult(test_id, "SKIP", skipped[test_id]))
        else:
            case_results.append(TestCaseResult(test_id, "PASS"))
    return case_results


def generate_html_report(result, report_path: str, title: str = "UI Test Report") -> Path:
    """Generate a minimal HTML report from unittest result."""
    report_file = Path(report_path)
    report_file.parent.mkdir(parents=True, exist_ok=True)

    case_results = _collect_case_results(result)

    html = [
        "<!DOCTYPE html>",
        "<html lang='en'>",
        "<head>",
        f"<meta charset='UTF-8'><title>{title}</title>",
        "<style>",
        "body{font-family:Arial,Helvetica,sans-serif;margin:24px;}",
        "table{border-collapse:collapse;width:100%;}",
        "th,td{border:1px solid #ddd;padding:8px;}",
        "th{background:#f5f5f5;}",
        ".PASS{color:#2e7d32;font-weight:bold;}",
        ".FAIL,.ERROR{color:#c62828;font-weight:bold;}",
        ".SKIP{color:#f9a825;font-weight:bold;}",
        "pre{white-space:pre-wrap;background:#fafafa;border:1px solid #eee;padding:8px;}",
        "</style>",
        "</head>",
        "<body>",
        f"<h1>{title}</h1>",
        f"<p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>",
        "<h2>Summary</h2>",
        "<ul>",
        f"<li>Total: {result.testsRun}</li>",
        f"<li>Failures: {len(result.failures)}</li>",
        f"<li>Errors: {len(result.errors)}</li>",
        f"<li>Skipped: {len(result.skipped)}</li>",
        "</ul>",
        "<h2>Details</h2>",
        "<table>",
        "<tr><th>Test Case</th><th>Status</th><th>Details</th></tr>",
    ]

    for case in case_results:
        detail_html = f"<pre>{case.details}</pre>" if case.details else ""
        html.append(
            "<tr>"
            f"<td>{case.name}</td>"
            f"<td class='{case.outcome}'>{case.outcome}</td>"
            f"<td>{detail_html}</td>"
            "</tr>"
        )

    html.extend(["</table>", "</body>", "</html>"])
    report_file.write_text("\n".join(html), encoding="utf-8")
    return report_file


class HtmlTestRunner:
    """Simple runner that stores results and outputs HTML report."""

    def __init__(self, report_path: str, title: str = "UI Test Report") -> None:
        self.report_path = report_path
        self.title = title

    def run(self, suite) -> object:
        import unittest

        result = unittest.TestResult()
        result.testsRunList = []

        def _start_test(test):
            result.testsRunList.append(test)
            unittest.TestResult.startTest(result, test)

        result.startTest = _start_test
        suite.run(result)
        generate_html_report(result, self.report_path, self.title)
        return result
