# ============================================================
# Experiment No. 2
# Title:
# Getting Started with Python and NLTK – Searching Text,
# Counting Vocabulary, Frequency Distribution,
# Collocations, and Bigrams
# ============================================================

import nltk
from nltk import FreqDist
from nltk.util import bigrams
from nltk.book import *

# ------------------------------------------------------------
# Download NLTK Book Corpus (Run only once)
# ------------------------------------------------------------
nltk.download('book')

# ------------------------------------------------------------
# Load Genesis Corpus
# ------------------------------------------------------------
text = text3

print("=" * 70)
print("Sample Text")
print("=" * 70)
print(text[:40])

# ------------------------------------------------------------
# Search Word
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("Searching for the word 'God'")
print("=" * 70)

text.concordance("God")

# ------------------------------------------------------------
# Vocabulary Count
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("Text Statistics")
print("=" * 70)

print("Total Number of Words :", len(text))
print("Vocabulary Size       :", len(set(text)))

# ------------------------------------------------------------
# Frequency Distribution
# ------------------------------------------------------------
fdist = FreqDist(text)

print("\nTop 20 Frequent Words")
print("-" * 40)

for word, frequency in fdist.most_common(20):
    print(f"{word:15} {frequency}")

# ------------------------------------------------------------
# Frequency of Specific Word
# ------------------------------------------------------------
print("\nFrequency of 'God' :", fdist["God"])

# ------------------------------------------------------------
# Collocations
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("Collocations")
print("=" * 70)

text.collocations()

# ------------------------------------------------------------
# Bigrams
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("First 20 Bigrams")
print("=" * 70)

bigram_list = list(bigrams(text))

for bg in bigram_list[:20]:
    print(bg)