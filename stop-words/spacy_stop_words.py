# pip install -U spacy
# python -m spacy download en

import spacy
from nltk.tokenize import word_tokenize

sp = spacy.load('en_core_web_sm')

all_stopwords = sp.Defaults.stop_words

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)

# Adicionando e removendo palavras de parada na lista de palavras de parada padrão SpaCy.
print(len(all_stopwords))
print(all_stopwords)

# Adicionando palavras de parada à lista de palavras de parada do SpaCy padrão..
# Você pode adicionar uma nova palavra ao conjunto da mesma forma que adicionaria qualquer novo item a um conjunto.
all_stopwords.add("tennis")

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)

# Você também pode adicionar várias palavras à lista de palavras de parada SpaCy.
all_stopwords |= {"likes", "tennis", }

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)

# Removendo palavras de parada da lista de palavras de parada do SpaCy padrão
# Para remover uma palavra do conjunto de palavras você pode passar a palavra a ser removida
# para o método remove do conjunto.
all_stopwords.remove('not')

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)
