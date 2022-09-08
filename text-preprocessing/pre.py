from spellchecker import SpellChecker

spell = SpellChecker(language='pt')

"""
english = SpellChecker()  # the default is English (language='en')
spanish = SpellChecker(language='es')  # use the Spanish Dictionary
russian = SpellChecker(language='ru')  # use the Russian Dictionary
"""


def correct_spellings(text):
    corrected_text = []
    misspelled_words = spell.unknown(text.split())
    for word in text.split():
        if word in misspelled_words:
            corrected_text.append(spell.correction(word))
        else:
            corrected_text.append(word)
    return " ".join(corrected_text)


text = "casro messagem cachoro"
print(correct_spellings(text))
