# ============================================================
# Experiment No. 5
# Title:
# Implementation of the Word2Vec Model Using Python
# ============================================================

from gensim.models import Word2Vec
import nltk
from nltk.tokenize import word_tokenize

# ------------------------------------------------------------
# Download Required Dataset (Run only once)
# ------------------------------------------------------------
nltk.download('punkt')
nltk.download('punkt_tab')

# ------------------------------------------------------------
# Sample Text Corpus
# ------------------------------------------------------------
text = [
    "Natural Language Processing is an exciting field.",
    "Python is widely used for machine learning.",
    "Word2Vec creates meaningful word embeddings.",
    "Machine learning improves intelligent systems.",
    "Deep learning and NLP are closely related.",
    "Artificial Intelligence uses machine learning algorithms."
]

# ------------------------------------------------------------
# Tokenize Sentences
# ------------------------------------------------------------
corpus = []

for sentence in text:
    tokens = word_tokenize(sentence.lower())
    corpus.append(tokens)

# ------------------------------------------------------------
# Train Word2Vec Model
# ------------------------------------------------------------
model = Word2Vec(
    sentences=corpus,
    vector_size=100,
    window=5,
    min_count=1,
    workers=4,
    sg=1      # Skip-Gram Model
)

# ------------------------------------------------------------
# Display Vocabulary
# ------------------------------------------------------------
print("=" * 70)
print("Vocabulary")
print("=" * 70)

print(model.wv.index_to_key)

# ------------------------------------------------------------
# Display Word Vector
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("Word Vector for 'learning'")
print("=" * 70)

print(model.wv["learning"])

# ------------------------------------------------------------
# Similar Words
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("Most Similar Words to 'learning'")
print("=" * 70)

for word, score in model.wv.most_similar("learning", topn=5):
    print(f"{word:15} {score:.4f}")

# ------------------------------------------------------------
# Similarity Score
# ------------------------------------------------------------
print("\n" + "=" * 70)
print("Similarity between 'machine' and 'learning'")
print("=" * 70)

print(model.wv.similarity("machine", "learning"))