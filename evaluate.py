"""Evaluate MoodAnalyzer against the predefined labeled sample posts."""

from typing import Dict, List, Sequence

from dataset import SAMPLE_POSTS, TRUE_LABELS
from mood_analyzer import MoodAnalyzer


def evaluate(posts: Sequence[str], labels: Sequence[str]) -> float:
    if len(posts) != len(labels):
        raise ValueError(
            f"Input/label count mismatch: {len(posts)} inputs, {len(labels)} labels."
        )

    if not posts:
        print("No labeled examples to evaluate.")
        return 0.0

    analyzer = MoodAnalyzer()
    correct = 0
    results_by_label: Dict[str, List[int]] = {}

    print("=== MoodAnalyzer Evaluation ===")
    for index, (text, expected) in enumerate(zip(posts, labels), start=1):
        predicted = analyzer.predict_label(text)
        passed = predicted == expected
        correct += int(passed)

        counts = results_by_label.setdefault(expected, [0, 0])
        counts[0] += int(passed)
        counts[1] += 1

        status = "PASS" if passed else "FAIL"
        print(
            f"{index:>2}. {status}: {text!r} "
            f"-> predicted={predicted!r}, expected={expected!r}"
        )

    accuracy = correct / len(posts)
    print(f"\nOverall: {correct}/{len(posts)} passed ({accuracy:.1%} accuracy)")
    print("Accuracy by expected label:")
    for label, (label_correct, label_total) in sorted(results_by_label.items()):
        label_accuracy = label_correct / label_total
        print(
            f"  {label}: {label_correct}/{label_total} "
            f"({label_accuracy:.1%})"
        )

    return accuracy


def main() -> None:
    evaluate(SAMPLE_POSTS, TRUE_LABELS)


if __name__ == "__main__":
    main()