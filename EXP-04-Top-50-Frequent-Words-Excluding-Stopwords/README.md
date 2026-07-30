# Experiment 04

## Title

Write a Function that Finds the 50 Most Frequently Occurring Words of a Text that are Not Stop Words

## Aim

To develop a Python program using the Natural Language Toolkit (NLTK) that removes stop words from a text and identifies the 50 most frequently occurring meaningful words using frequency distribution.

## Software Requirements

- Python 3.x
- NLTK Library
- VS Code / Jupyter Notebook

## Installation

```bash
pip install nltk
```

```python
import nltk

nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')
```

## Algorithm

1. Import the required NLTK libraries.
2. Download the required datasets.
3. Load the Gutenberg corpus.
4. Convert all words to lowercase.
5. Remove punctuation and English stop words.
6. Create a frequency distribution.
7. Retrieve the top 50 most frequent words.
8. Display the words and their frequencies.

## Files

- experiment4.py
- requirements.txt
- sample_output.txt

## Result

The program successfully removed stop words from the selected text corpus and displayed the 50 most frequently occurring meaningful words using NLTK's Frequency Distribution.