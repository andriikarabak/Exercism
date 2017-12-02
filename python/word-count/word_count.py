from collections import Counter
# Regular expressions module is used as the solution become more pythonic with it.
import re

def word_count(phrase):
    # Using str.lower method make a string lowercased, so, for example, 'Later' matches 'later'.
    # Using re.sub method a quotation mark ' is removed, but not an apostrophe.
    # Using re.findall with "[a-z0-9']+" pattern receive a list with words, where all characters
    # except alphanumeric and apostrophe are ignored.
    # collections.Counter returns a dictionary with words and its number of occurrences.
    return Counter(re.findall("[a-z0-9']+", re.sub(r" '|' ", " ", phrase.lower())))
    # TODO: How does the following pattern work? - "[a-z0-9]+(?:'\w)?"