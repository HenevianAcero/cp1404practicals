'''
Word Occurrences
Estimated time: 25 minutes
Actual time: 36 minutes
'''
word_repeats = {}
text = input("Text: ")
print(text)
# text = "this is a collection of words of nice words this is a fun thing it is"

words = text.split()
for word in words:
    frequency = word_repeats.get(word, 0)
    word_repeats[word] = frequency + 1

words = list(word_repeats.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}}: {word_repeats[word]}")

