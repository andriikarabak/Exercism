def is_isogram(word):
    for char in word:
        if word.lower().count(char) > 1 and char != '-' and char != ' ':
            return False
    return True

