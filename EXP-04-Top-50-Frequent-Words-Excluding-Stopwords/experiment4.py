# ============================================================
# Experiment No. 4
# Title:
# Find the 50 Most Frequently Occurring Words
# Excluding Stop Words
# ============================================================

import nltk
from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk import FreqDist

# ------------------------------------------------------------
# Download Required Datasets (Run only once)
# ------------------------------------------------------------
nltk.download('gutenberg')
nltk.download('stopwords')
nltk.download('punkt')

# ------------------------------------------------------------
# Load Gutenberg Corpus
# ------------------------------------------------------------
words = gutenberg.words('austen-emma.txt')

# ------------------------------------------------------------
# Load English Stop Words
# ------------------------------------------------------------
stop_words = set(stopwords.words('english'))

# ------------------------------------------------------------
# Remove Stop Words and Punctuation
# ------------------------------------------------------------
filtered_words = []

for word in words:
    word = word.lower()

    if word.isalpha() and word not in stop_words:
        filtered_words.append(word)

# ------------------------------------------------------------
# Frequency Distribution
# ------------------------------------------------------------
fdist = FreqDist(filtered_words)

# ------------------------------------------------------------
# Function to Display Top 50 Frequent Words
# ------------------------------------------------------------
def top50_words():
    print("=" * 60)
    print("Top 50 Most Frequently Occurring Words")
    print("=" * 60)

    print(f"\n{'Word':20}Frequency")
    print("-" * 35)

    for word, frequency in fdist.most_common(50):
        print(f"{word:20}{frequency}")

# ------------------------------------------------------------
# Main Function
# ------------------------------------------------------------
if __name__ == "__main__":
    top50_words()