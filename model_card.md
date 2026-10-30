# Model Card: Mood Machine

This model card is for the Mood Machine project, which includes **two** versions of a mood classifier:

1. A **rule based model** implemented in `mood_analyzer.py`
2. A **machine learning model** implemented in `ml_experiments.py` using scikit learn

You may complete this model card for whichever version you used, or compare both if you explored them.

## 1. Model Overview

**Model type:**  
Describe whether you used the rule based model, the ML model, or both.  
Example: “I used the rule based model only” or “I compared both models.”

**Intended purpose:**  
What is this model trying to do?  
Example: classify short text messages as moods like positive, negative, neutral, or mixed.

**How it works (brief):**  
For the rule based version, describe the scoring rules you created.  
For the ML version, describe how training works at a high level (no math needed).



## 2. Data

**Dataset description:**  
Summarize how many posts are in `SAMPLE_POSTS` and how you added new ones.

**Labeling process:**  
Explain how you chose labels for your new examples.  
Mention any posts that were hard to label or could have multiple valid labels.

**Important characteristics of your dataset:**  
Examples you might include:  

- Contains slang or emojis  
- Includes sarcasm  
- Some posts express mixed feelings  
- Contains short or ambiguous messages

**Possible issues with the dataset:**  
Think about imbalance, ambiguity, or missing kinds of language.

## 3. How the Rule Based Model Works (if used)

**Your scoring rules:**  
Describe the modeling choices you made.  
Examples:  

- How positive and negative words affect score  
- Negation rules you added  
- Weighted words  
- Emoji handling  
- Threshold decisions for labels

**Strengths of this approach:**  
Where does it behave predictably or reasonably well?

**Weaknesses of this approach:**  
Where does it fail?  
Examples: sarcasm, subtlety, mixed moods, unfamiliar slang.

## 4. How the ML Model Works (if used)

**Features used:**  
Describe the representation.  
Example: “Bag of words using CountVectorizer.”

**Training data:**  
State that the model trained on `SAMPLE_POSTS` and `TRUE_LABELS`.

**Training behavior:**  
Did you observe changes in accuracy when you added more examples or changed labels?

**Strengths and weaknesses:**  
Strengths might include learning patterns automatically.  
Weaknesses might include overfitting to the training data or picking up spurious cues.

## 5. Evaluation

### Automated Tests

Automated Test Summary 

| Test Input | Evaluation Criteria | Result |
| ------------- | ------------- | --------- |
| Three labeled posts | Calculates accuracy and prints predictions | PASSED |
| Empty evaluation dataset | Returns 0.0 and handles empty data gracefully | PASSED |
| Two sample posts | Predicts and prints each post's mood | PASSED |
| Padded sentence followed by QUIT | Strips input, predicts mood, and exits | PASSED |
| Whitespace-only input | Exits gracefully without making a prediction | PASSED |

- 5 passed in 0.02s

### Reliability

I was surprised that passing the automated tests didn’t necessarily mean the mood predictions were reliable. The tests confirmed that the program handled inputs and produced results, but they didn’t establish that its labels were accurate. I also noticed how easily a short or ambiguous message could be interpreted in different ways. That made me realize the model’s reliability depends heavily on the examples and labels it was given, and it may struggle with sarcasm, slang, or mixed feelings.

**How you evaluated the model:**  
Both versions can be evaluated on the labeled posts in `dataset.py`.  
Describe what accuracy you observed.

**Examples of correct predictions:**  
Provide 2 or 3 examples and explain why they were correct.

**Examples of incorrect predictions:**  
Provide 2 or 3 examples and explain why the model made a mistake.  
If you used both models, show how their failures differed.

## 6. Limitations

- Limited data and generalization: A small set of short posts may not represent longer messages or language outside the examples.
- Ambiguity and context: Sarcasm, mixed feelings, subtle wording, slang, and emojis can be difficult to interpret.
- Model-specific weaknesses: A rule-based model depends on its chosen words, scoring, and negation rules. An ML model can overfit or rely on misleading patterns in its training examples.
- Evaluation may be misleading: The card mentions evaluating on labeled posts, but doesn’t say whether those posts are separate from training data. If they overlap, accuracy may overstate performance. The listed automated tests check program behavior, not whether mood predictions are accurate or fair.
- Potential bias and harm: Language communities may express emotion differently, leading to uneven errors. Misreading distress could have serious consequences, and analyzing personal messages raises privacy concerns.

Describe the most important limitations.  
Examples:  

- The dataset is small  
- The model does not generalize to longer posts  
- It cannot detect sarcasm reliably  
- It depends heavily on the words you chose or labeled

## 7. Ethical Considerations

A mood classifier could be misused to monitor people without their consent, label them unfairly, target them with manipulative messages, or make decisions about them at work, school, or in services. It can also misread sarcasm, slang, or distress — so treating its prediction as fact could harm someone.

To reduce those risks:
- Limit its purpose: use it for experimentation or voluntary, low-stakes feedback—not diagnosis, surveillance, or decisions about individuals.
- Be transparent and get consent: explain what text is analyzed, why, and how results are used; let people opt out.
- Protect the data: collect as little as possible, avoid retaining identifiable messages, restrict access, and set a deletion schedule.
- Keep a person in control: present results as uncertain estimates, not facts, and require human review before any action.
- Test for uneven errors: evaluate on a separate test set and check performance across different language styles and communities. Don’t deploy if it performs poorly or inconsistently.
- Plan for misuse: restrict who can use it, monitor use, and provide a way to report or challenge harmful results.

Discuss any potential impacts of using mood detection in real applications.  
Examples: 

- Misclassifying a message expressing distress  
- Misinterpreting mood for certain language communities  
- Privacy considerations if analyzing personal messages

## 8. Ideas for Improvement

List ways to improve either model.  
Possible directions:  

- Add more labeled data  
- Use TF IDF instead of CountVectorizer  
- Add better preprocessing for emojis or slang  
- Use a small neural network or transformer model  
- Improve the rule based scoring method  
- Add a real test set instead of training accuracy only

## 9. Machine Learning in Python
- Simple and efficient tools for predictive data analysis
- Accessible to everybody, and reusable in various contexts
- Built on NumPy, SciPy, and matplotlib
- Open source, commercially usable - BSD license

[Machine Learning in Python](https://scikit-learn.org/stable/index.html)