from gensim.parsing.preprocessing import remove_stopwords
import gensim
from gensim.parsing.preprocessing import STOPWORDS
from nltk.tokenize import word_tokenize

text = "Nick likes to play football, however he is not too fond of tennis."
# Documentation: https://radimrehurek.com/gensim/
filtered_sentence = remove_stopwords(text)

print(filtered_sentence)

# Adicionando e removendo palavras de parada na lista de palavras de parada de Gensim padrão.
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print(all_stopwords)

# Adicionando palavras de parada à lista de palavras de parada de Gensim padrão.
# Para adicionar um elemento, você deve aplicar a função union no conjunto e passar a ele o conjunto de novas palavras.
# O union método retornará um novo conjunto que contém suas palavras recém-adicionadas.
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play']))

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]

print(tokens_without_sw)

# Removendo palavras irrelevantes da lista de palavras irrelevantes padrão do Gensim
all_stopwords_gensim = STOPWORDS
sw_list = {"not"}
# Para remover palavras irrelevantes da lista de palavras Gensim, você deve chamar o difference().
all_stopwords_gensim = STOPWORDS.difference(sw_list)

text = "Nick likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)
tokens_without_sw = [word for word in text_tokens if not word in all_stopwords_gensim]

print(tokens_without_sw)
