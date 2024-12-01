"""
CP1404 Practical 5
word_occurrences.py
Estimated time: 30 mins
Actual time: 40 mins

"""

word_to_count = {}
text = input("Text: ")
# text: "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    occurrence = word_to_count.get(word, 0)
    word_to_count[word] = occurrence + 1

words = list(word_to_count.keys())
words.sort()

width = max((len(word) for word in words))
for word in words:
    print(f"{word:{width}} : {word_to_count[word]}")
