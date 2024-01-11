from PyDictionary import PyDictionary

def get_word_definition(word):
    dictionary = PyDictionary()
    definition = dictionary.meaning(word)
    return definition
