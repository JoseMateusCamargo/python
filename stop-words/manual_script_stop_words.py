stopwords_br = [line.strip() for line in open('stopwords_br.txt', encoding="utf-8")]
print(stopwords_br)


def remove_stopwords(sentence):
    tokens = sentence.split(" ")
    tokens_filtered = [word for word in tokens if not word in stopwords_br]
    return " ".join(tokens_filtered)


text = "A vantagem de ter péssima memória é divertir-se muitas vezes com as mesmas coisas boas como se fosse a primeira vez. ..."
filtered_text = remove_stopwords(text)
print(filtered_text)

# Para adicionar uma palavra à lista de palavras de parada usando o método append.
stopwords_br.append("vantagem")
filtered_text = remove_stopwords(text)
print(filtered_text)

# Para remover uma palavra do conjunto de palavras você pode passar a palavra a ser removida
# para o método remove do conjunto.
stopwords_br.remove("vantagem")
filtered_text = remove_stopwords(text)
print(filtered_text)
