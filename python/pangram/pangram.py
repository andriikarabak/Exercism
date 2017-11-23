def is_pangram(sentence):
    lowercase_sentence = sentence.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in alphabet:
        if not char in lowercase_sentence:
            return False
    return True

