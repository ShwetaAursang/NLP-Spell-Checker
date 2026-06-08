import re
from collections import Counter

# Load corpus
def words(text):
    return re.findall(r'\w+', text.lower())

# Read training corpus
with open('big.txt', 'r', encoding='utf-8') as file:
    WORDS = Counter(words(file.read()))

# Probability of a word
def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N

# Most probable correction
def correction(word):
    return max(candidates(word), key=P)

# Generate candidate corrections
def candidates(word):
    return (
        known([word]) or
        known(edits1(word)) or
        known(edits2(word)) or
        [word]
    )

# Known words in dictionary
def known(words):
    return set(w for w in words if w in WORDS)

# Edit distance = 1
def edits1(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'

    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    deletes = [L + R[1:] for L, R in splits if R]

    transposes = [L + R[1] + R[0] + R[2:]
                  for L, R in splits if len(R) > 1]

    replaces = [L + c + R[1:]
                for L, R in splits if R for c in letters]

    inserts = [L + c + R
               for L, R in splits for c in letters]

    return set(deletes + transposes + replaces + inserts)

# Edit distance = 2
def edits2(word):
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

# Testing
while True:
    word = input("Enter word: ")
    print("Suggested correction:", correction(word))
