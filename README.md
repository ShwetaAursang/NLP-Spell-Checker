# NLP Spell Checker

An intelligent spell-checking and correction system based on **Peter Norvig's Probabilistic Spelling Correction Algorithm**. The application automatically detects misspelled words and suggests the most probable corrections using word frequency statistics and edit-distance techniques.

## Features

* Automatic spell correction
* Candidate word generation
* Edit distance-based matching
* Probability-based word ranking
* Text preprocessing and normalization
* Web interface using Flask

## How It Works

The system follows Peter Norvig's approach:

1. Build a vocabulary from a corpus.
2. Generate candidate words within one or two edit distances.
3. Calculate word probabilities based on frequency.
4. Select the most probable correction.

### Example

Input:

```text
speling
```

Output:

```text
spelling
```

Input:

```text
langauge
```

Output:

```text
language
```

## Technologies Used

* Python
* Flask
* Natural Language Processing (NLP)
* Regular Expressions
* Probability Models

## Applications

* Spell checking systems
* Search query correction
* Text preprocessing
* NLP pipelines
* Chatbots and virtual assistants

## Reference

Inspired by Peter Norvig's article:
"How to Write a Spelling Corrector"


