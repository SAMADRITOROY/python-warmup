from log_generator import generate_log_lines
import re

def test_generate_log_lines_with_no_parameters():
    log_lines = generate_log_lines()
    assert len(log_lines) == 10

def test_generate_log_lines_with_custom_number_of_lines():
    log_lines = generate_log_lines(5)
    assert len(log_lines) == 5

def test_generate_log_lines_has_correct_format():
    log_lines = generate_log_lines(10)
    for line in log_lines:
        if line.startswith("this is a garbled log line"):
            continue
        pattern = r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}:\d{2} \[(INFO|WARNING|ERROR)\] service=(user-service|order-service|payment-service) [a-zA-Z0-9\s,.]*$"
        assert re.fullmatch(pattern, line)