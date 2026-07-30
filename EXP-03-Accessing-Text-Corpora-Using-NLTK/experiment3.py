# ============================================================
# Experiment No. 3
# Title:
# Accessing Text Corpora Using NLTK in Python
# ============================================================

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import brown
from nltk.corpus import reuters

# ------------------------------------------------------------
# Download Required Corpora (Run only once)
# ------------------------------------------------------------
nltk.download('gutenberg')
nltk.download('brown')
nltk.download('reuters')
nltk.download('punkt')
nltk.download('punkt_tab')

# ------------------------------------------------------------
# Gutenberg Corpus
# ------------------------------------------------------------

print("=" * 70)
print("GUTENBERG CORPUS")
print("=" * 70)

print("\nAvailable Gutenberg Files:\n")
print(gutenberg.fileids())

book = "austen-emma.txt"

words = gutenberg.words(book)
sentences = gutenberg.sents(book)

print("\nSelected Book :", book)

print("\nFirst 20 Words")
print(words[:20])

print("\nFirst 3 Sentences")

for sentence in sentences[:3]:
    print(sentence)

print("\nTotal Number of Words :", len(words))
print("Vocabulary Size       :", len(set(words)))

# ------------------------------------------------------------
# Brown Corpus
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("BROWN CORPUS")
print("=" * 70)

print("\nAvailable Categories\n")
print(brown.categories())

print("\nSample Words from News Category")
print(brown.words(categories='news')[:30])

print("\nTotal Words in News Category")
print(len(brown.words(categories='news')))

# ------------------------------------------------------------
# Reuters Corpus
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("REUTERS CORPUS")
print("=" * 70)

print("\nFirst 10 File IDs")
print(reuters.fileids()[:10])

print("\nFirst 10 Categories")
print(reuters.categories()[:10])

print("\nSample Reuters Text")
print(reuters.words(reuters.fileids()[0])[:40])