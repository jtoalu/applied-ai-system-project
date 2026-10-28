# The Mood Machine: Exploring How Text Classifiers Work

The Mood Machine is a hands-on project for classifying short text as positive, negative, neutral, or mixed. It starts with a rule-based model and can be extended with a small machine-learning model, letting you compare how different approaches make predictions.

The project matters because it helps learners see how training data and design choices shape model behavior — and why classifiers can make mistakes, especially with limited data, slang, sarcasm, or neutral phrases. By testing examples and reflecting on failures, you can better understand model accuracy, fairness, and limitations.

---

## Architecture Overview

In main.py, the sample posts are passed to the rule-based MoodAnalyzer for evaluation and a batch demo. During evaluation, its predictions are compared with TRUE_LABELS, and the results and accuracy are printed for human review. In interactive mode, a user enters a sentence and receives a predicted mood and explanation. The diagram shows these paths through the analyzer and where people can inspect the results.

---

## Repo Structure

```plaintext
├── dataset.py         # Starter word lists and example posts (you will expand these)
├── mood_analyzer.py   # Rule based classifier with TODOs to improve
├── main.py            # Runs the rule based model and interactive demo
├── ml_experiments.py  # (New) A tiny ML classifier using scikit-learn
├── model_card.md      # Template to fill out after experimenting
└── requirements.txt   # Dependencies for optional ML exploration
```

---

## Getting Started

1. Open this folder in VS Code.
2. Make sure your Python environment is active.
3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the rule-based starter:

    ```bash
    python main.py
    ```

If pieces of the analyzer are not implemented yet, you will see helpful errors that guide you to the TODOs.

To try the ML model later, run:

```bash
python ml_experiments.py
```

---

## Sample Interactions

Here are examples of the Mood Machine’s input and output. Predictions can vary depending on whether you run the rule-based model or the ML model and on the current data and rules.

| Input | Example Output |
| ------------- | ------------- |
| “I love this sunny day!” | positive (illustrative) |
| “I feel awful and disappointed.” | negative (illustrative)
| “Today is Thursday” | ML model: negative (observed; a small training dataset can lead to unexpected predictions)

The examples marked illustrative show typical expected results; run the program to see its current predictions.

![Interactive Mood Machine (rule based)](images/Screenshot%202026-10-27%20202731.png)

---

## Design Decisions

The Mood Machine uses both a rule-based classifier and an optional small machine-learning model to make their behavior easy to compare. The rule-based approach is simple, fast, and transparent: learners can inspect and change the scoring rules. Its trade-off is that it depends on specific words and rules, so it can miss context, slang, sarcasm, or unfamiliar phrasing.

The optional ML model uses bag-of-words features and logistic regression. This keeps the experiment lightweight and introduces a common text-classification approach, but it does not understand word order or meaning. With a small dataset, it can also learn misleading associations and make unexpected predictions.

Batch evaluation and interactive input let learners examine predictions in different ways. The evaluation reports accuracy on the provided examples, which is useful for exploration but does not show how well the model will perform on new text. These trade-offs make the project a learning tool — not a reliable measure of a person’s actual mood.

---

## Testing Summary

The Mood Machine ran through its batch and interactive examples and produced mood predictions. The evaluator also compared rule-based predictions with the labeled examples and reported accuracy. One notable result was that the ML model classified “Today is Thursday” as negative, even though the sentence is neutral.

This showed that the model can pick up misleading word associations when trained on a small dataset. The rule-based approach is easier to inspect, but it can miss context and phrases that aren’t covered by its rules. I learned that a prediction is not necessarily a reliable judgment of someone’s mood, and that testing varied examples — and reviewing mistakes — is important.

---

## Reflection

This project taught me that AI predictions depend on the data and rules behind them — they aren’t automatically correct or human-like. Testing unexpected results helped me see the value of questioning assumptions, investigating failures, and improving a system step by step.

---

## What You Will Do

During this lab you will:

- Implement the missing parts of the rule based `MoodAnalyzer`.
- Add new positive and negative words.
- Expand the dataset with more posts, including slang, emojis, sarcasm, or mixed emotions.
- Observe unusual or incorrect predictions and think about why they happen.
- Train a tiny machine learning model and compare its behavior to your rule based system.
- Complete the model card with your findings about data, behavior, limitations, and improvements.
- The goal is to help you reason about how models behave, how data shapes them, and why even small design choices matter.

---

## Tips

- Start with preprocessing before updating scoring rules.
- When debugging, print tokens, scores, or intermediate choices.
- Ask an AI assistant to help create edge case posts or unusual wording.
- Try examples that mislead or confuse your model. Failure cases teach you the most.

## Observations
```
=== Interactive Mood Machine (ML model) ===
Type a sentence to analyze its mood.
Type 'quit' or press Enter on an empty line to exit.

You: Today is Thursday
ML model: negative

why is it negative?
```

Because the ML model is not “understanding” the sentence as a human would. It is learning from the tiny dataset using bag-of-words features.

What’s happening:
- The model turns text into word counts.
- It learns which words were associated with each label in your training set.
- In the dataset, the word “today” appears in a clearly negative example:
"Today was a terrible day"
- Since the training set is very small, that one negative association can bias the model.
- The sentence "Today is Thursday" contains "today", so the classifier sees a strong negative cue and predicts negative.

This is a classic small-dataset problem:
- few examples
- a lot of vocabulary is missing
- the model overfits to accidental word patterns
- neutral phrases can get pushed into a sentiment class

So:
- "Today is Thursday" is obviously neutral to a person
- but the ML model is not reasoning about meaning
- it is guessing from word frequencies and weak correlations

This is exactly why the rule-based model and the ML model often disagree or produce strange outputs on short, neutral sentences.

In short: it predicts negative because of the training data, not because "Thursday" is inherently negative.

![screenshot of ML Model](images/Screenshot%202026-10-08%20213252.png)