# Experiment 1
# Title: Create Regular Expressions in Python for Detecting Word Patterns and Tokenizing Text

import re

text = """
John Smith joined ABC Technologies on 12/05/2025.
His email is john.smith@gmail.com and alternate email is john@yahoo.com.
Contact number: +91-9876543210.
Website: https://www.abctech.com
Python is amazing!
Natural Language Processing is interesting.
"""

print("=" * 60)
print("Original Text")
print("=" * 60)
print(text)

# Word Extraction
words = re.findall(r'\b\w+\b', text)
print("\nWords")
print(words)

# Number Extraction
numbers = re.findall(r'\d+', text)
print("\nNumbers")
print(numbers)

# Email Detection
emails = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', text)
print("\nEmails")
print(emails)

# Phone Number Detection
phones = re.findall(r'\+91-\d{10}', text)
print("\nPhone Numbers")
print(phones)

# Date Detection
dates = re.findall(r'\d{2}/\d{2}/\d{4}', text)
print("\nDates")
print(dates)

# URL Detection
urls = re.findall(r'https?://[^\s]+', text)
print("\nURLs")
print(urls)

# Capitalized Words
caps = re.findall(r'\b[A-Z][a-z]+\b', text)
print("\nCapitalized Words")
print(caps)

# Tokenization
tokens = re.findall(r"\w+|[^\w\s]", text)
print("\nTokens")
print(tokens)