import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Documentation: https://www.nltk.org/
nltk.download('stopwords')

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]

print(tokens_without_sw)

# Lista de palavras sem palavras de parada.
filtered_sentence = " ".join(tokens_without_sw)
print(filtered_sentence)

# Adicionando ou removendo palavras de interrupção na lista de palavras de interrupção padrão do NLTK.
print(stopwords.words('english'))

# Adicionando palavras de parada à lista de palavras de parada NLTK padrão.
all_stopwords = stopwords.words('english')
all_stopwords.append('play')

text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)

# Você também pode adicionar uma lista de palavras à stopwords.words lista usando o método append.
sw_list = ['likes', 'play']
all_stopwords.extend(sw_list)

text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]

print(tokens_without_sw)

# Removendo palavras de parada da lista de palavras de parada NLTK padrão.
all_stopwords = stopwords.words('english')
all_stopwords.remove('to')  # A maneira mais simples de fazer isso é por meio do método remove().

text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
print(tokens_without_sw)
