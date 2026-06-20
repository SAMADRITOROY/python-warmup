from log_parser import parse_log_line, LogEntry, summarize_logs, LogSummary
from datetime import datetime
import pytest


def test_parse_log_line():
    log_line = "2026-06-13T11:02:21.222819+00:00 [INFO] service=order-service Order placed successfully"
    expected = LogEntry(
        datetime.fromisoformat("2026-06-13T11:02:21.222819+00:00"),
        "INFO",
        "order-service",
        "Order placed successfully",
    )
    assert expected == parse_log_line(log_line)


def test_parse_log_line_with_wrong_no_of_log_items():
    log_line = "garbled"
    with pytest.raises(ValueError) as exc_info:
        parse_log_line(log_line)
    assert (
        str(exc_info.value) == "Incorret log format: atleast 4 log-items were expected"
    )


def test_parse_log_line_with_wrong_timestamp():
    log_line = (
        "wrong_timestamp_format [INFO] service=order-service Order placed successfully"
    )
    with pytest.raises(ValueError) as exc_info:
        parse_log_line(log_line)
    assert str(exc_info.value) == "Incorrect timestamp format"


def test_parse_log_line_with_service_format():
    log_line = "2026-06-13T11:02:21.222819+00:00 [INFO] order-service Order placed successfully"
    with pytest.raises(ValueError) as exc_info:
        parse_log_line(log_line)
    assert str(exc_info.value) == "Incorrect service format"


def test_summarize_logs():
    log_entries = [
        LogEntry(
            datetime.fromisoformat("2026-06-13T11:02:21.222819+00:00"),
            "INFO",
            "order-service",
            "Order placed successfully",
        ),
        LogEntry(
            datetime.fromisoformat("2026-06-13T11:02:21.223919+00:00"),
            "INFO",
            "user-service",
            "User logged in",
        ),
    ]
    expected = LogSummary(
        {"INFO": 2}, ["Order placed successfully", "User logged in"], 11
    )
    assert expected == summarize_logs(log_entries)


def test_summarize_logs_empty_log_entries():
    log_entries = []
    with pytest.raises(ValueError) as exc_info:
        summarize_logs(log_entries)
    assert str(exc_info.value) == "The list of input LogEntry objects is empty"
