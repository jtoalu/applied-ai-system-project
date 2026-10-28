import main


def print_test_details(capsys, test_name, details, output):
    """Print per-test diagnostics even when pytest's capsys fixture is active."""
    with capsys.disabled():
        print(f"\n--- {test_name} ---")
        for detail in details:
            print(detail)
        print("Application output:")
        print(output.rstrip() or "(no output)")


class FakeMoodAnalyzer:
    def __init__(self, predictions):
        self.predictions = predictions
        self.seen = []

    def predict_label(self, text):
        self.seen.append(text)
        return self.predictions[text]

    def explain(self, text):
        return f"reason for {text}"


def test_evaluate_rule_based_returns_accuracy_and_prints_predictions(
    monkeypatch, capsys
):
    posts = ["sunny day", "rough day", "okay day"]
    labels = ["happy", "happy", "neutral"]
    predictions = {
        "sunny day": "happy",
        "rough day": "sad",
        "okay day": "neutral",
    }
    analyzer = FakeMoodAnalyzer(predictions)
    monkeypatch.setattr(main, "MoodAnalyzer", lambda: analyzer)

    accuracy = main.evaluate_rule_based(posts, labels)
    output = capsys.readouterr().out
    print_test_details(
        capsys,
        "Test 1 of 5: evaluation accuracy and per-post output",
        [
            f"Input posts: {posts}",
            f"True labels: {labels}",
            f"Expected accuracy: {2 / 3:.6f}",
            f"Actual accuracy:   {accuracy:.6f}",
            f"Predictions requested: {analyzer.seen}",
        ],
        output,
    )

    assert accuracy == 2 / 3
    assert '"sunny day" -> predicted=happy, true=happy' in output
    assert '"rough day" -> predicted=sad, true=happy' in output
    assert "Rule based accuracy on SAMPLE_POSTS: 0.67" in output
    assert analyzer.seen == posts


def test_evaluate_rule_based_with_no_posts_returns_zero(monkeypatch, capsys):
    analyzer = FakeMoodAnalyzer({})
    monkeypatch.setattr(main, "MoodAnalyzer", lambda: analyzer)

    accuracy = main.evaluate_rule_based([], [])
    output = capsys.readouterr().out
    print_test_details(
        capsys,
        "Test 2 of 5: empty evaluation input",
        [
            "Input posts: []",
            "Input labels: []",
            "Expected accuracy: 0.0",
            f"Actual accuracy:   {accuracy}",
            f"Predictions requested: {analyzer.seen}",
        ],
        output,
    )

    assert accuracy == 0.0
    assert "No labeled examples to evaluate." in output
    assert analyzer.seen == []


def test_run_batch_demo_predicts_and_prints_each_sample(monkeypatch, capsys):
    samples = ["post one", "post two"]
    analyzer = FakeMoodAnalyzer({"post one": "happy", "post two": "sad"})
    monkeypatch.setattr(main, "MoodAnalyzer", lambda: analyzer)
    monkeypatch.setattr(main, "SAMPLE_POSTS", samples)

    main.run_batch_demo()
    output = capsys.readouterr().out
    print_test_details(
        capsys,
        "Test 3 of 5: batch predictions",
        [
            f"Input sample posts: {samples}",
            "Expected predictions: post one -> happy; post two -> sad",
            f"Predictions requested: {analyzer.seen}",
        ],
        output,
    )

    assert '"post one" -> happy' in output
    assert '"post two" -> sad' in output
    assert analyzer.seen == samples


def test_interactive_loop_strips_input_predicts_and_exits_on_quit(
    monkeypatch, capsys
):
    inputs = ["  I feel good  ", "QUIT"]
    analyzer = FakeMoodAnalyzer({"I feel good": "happy"})
    monkeypatch.setattr(main, "MoodAnalyzer", lambda: analyzer)
    input_iter = iter(inputs)
    monkeypatch.setattr("builtins.input", lambda _prompt: next(input_iter))

    main.run_interactive_loop()
    output = capsys.readouterr().out
    print_test_details(
        capsys,
        "Test 4 of 5: interactive prediction and quit command",
        [
            f"Typed input sequence: {inputs}",
            "Expected behavior: strip sentence, predict happy, exit on QUIT",
            f"Predictions requested: {analyzer.seen}",
        ],
        output,
    )

    assert "Model: happy (reason for I feel good)" in output
    assert "Goodbye from the Mood Machine." in output
    assert analyzer.seen == ["I feel good"]


def test_interactive_loop_exits_on_empty_input_without_predicting(
    monkeypatch, capsys
):
    analyzer = FakeMoodAnalyzer({})
    monkeypatch.setattr(main, "MoodAnalyzer", lambda: analyzer)
    monkeypatch.setattr("builtins.input", lambda _prompt: "   ")

    main.run_interactive_loop()
    output = capsys.readouterr().out
    print_test_details(
        capsys,
        "Test 5 of 5: interactive exit on blank input",
        [
            "Typed input: three spaces",
            "Expected behavior: exit without predicting",
            f"Predictions requested: {analyzer.seen}",
        ],
        output,
    )

    assert "Goodbye from the Mood Machine." in output
    assert analyzer.seen == []