_TEST_DETAILS = {
    "test_evaluate_rule_based_returns_accuracy_and_prints_predictions": (
        "Three labeled posts",
        "Calculates accuracy and prints predictions",
    ),
    "test_evaluate_rule_based_with_no_posts_returns_zero": (
        "Empty evaluation dataset",
        "Returns 0.0 and handles empty data gracefully",
    ),
    "test_run_batch_demo_predicts_and_prints_each_sample": (
        "Two sample posts",
        "Predicts and prints each post's mood",
    ),
    "test_interactive_loop_strips_input_predicts_and_exits_on_quit": (
        "Padded sentence followed by QUIT",
        "Strips input, predicts mood, and exits",
    ),
    "test_interactive_loop_exits_on_empty_input_without_predicting": (
        "Whitespace-only input",
        "Exits gracefully without making a prediction",
    ),
}

_TEST_RESULTS = {}


def pytest_runtest_logreport(report):
    if report.when == "call":
        _TEST_RESULTS[report.nodeid] = report.outcome.upper()


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.write_sep("=", "Automated test summary")

    rows = [("Test Input", "Evaluation Criteria", "Result")]

    for nodeid, result in _TEST_RESULTS.items():
        test_name = nodeid.rsplit("::", 1)[-1]
        test_input, criteria = _TEST_DETAILS.get(
            test_name,
            (test_name, "See test assertions"),
        )
        rows.append((test_input, criteria, result))

    widths = [
        max(len(row[column]) for row in rows)
        for column in range(3)
    ]

    for index, row in enumerate(rows):
        line = " | ".join(
            value.ljust(widths[column])
            for column, value in enumerate(row)
        )
        terminalreporter.write_line(line)

        if index == 0:
            terminalreporter.write_line(
                "-+-".join("-" * width for width in widths)
            )