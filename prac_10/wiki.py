""""
CP1404 Practical
wiki.py
Estimated time: 10 mins
Actual time: 10 mins
"""

import wikipedia

name = input("Title: ")
while name != '':
    wikipedia.search(name)
    wikipedia.summary(name)
    wikipedia.page(name, autosuggest=False)
    name = input("Title: ")


