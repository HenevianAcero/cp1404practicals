"""
CP1404 Practical 10
wiki.py
Estimated time: 10 mins
Actual time: 11 mins
"""

import wikipedia

title = input("Title: ")
while title != '':
    wikipedia.search(title)
    summary = wikipedia.summary(title)
    wikipedia.exceptions.DisambiguationError: ""
    try:
        search = wikipedia.summary(title)
    except wikipedia.exceptions.DisambiguationError:
        print(title)
    except wikipedia.exceptions.PageError:
        print(f"{title} does not match any pages. Try another query!")
    page = wikipedia.page(title, autosuggest=False)
    url = title.url
    print(title, page, summary, url)
    name = input("Title: ")
print("Thank you.")
