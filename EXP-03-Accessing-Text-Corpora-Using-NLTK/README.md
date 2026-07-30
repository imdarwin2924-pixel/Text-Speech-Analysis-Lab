# Experiment 03

## Title

Accessing Text Corpora Using NLTK in Python

## Aim

To learn how to access, load, and analyze text corpora using the Natural Language Toolkit (NLTK) in Python for Natural Language Processing (NLP) applications.

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
nltk.download('brown')
nltk.download('reuters')
nltk.download('punkt')
nltk.download('punkt_tab')
```

## Algorithm

1. Import the required NLTK libraries.
2. Download the required corpora.
3. Load the Gutenberg corpus.
4. Display the available files.
5. Select a book from the corpus.
6. Display sample words and sentences.
7. Count the total number of words.
8. Calculate the vocabulary size.
9. Load the Brown corpus.
10. Display categories and sample words.
11. Load the Reuters corpus.
12. Display file IDs, categories, and sample text.
13. Display the results.

## Files

- experiment3.py
- requirements.txt
- sample_output.txt

## Result

The program successfully accessed and analyzed the Gutenberg, Brown, and Reuters corpora using NLTK. It displayed available files, sample words, sentences, vocabulary size, corpus categories, and sample news text, demonstrating how text corpora are used in Natural Language Processing applications.