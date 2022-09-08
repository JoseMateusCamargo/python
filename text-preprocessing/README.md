<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="225">

# Text Preprocessing in Python

O pré-processamento é tradicionalmente um passo importante para tarefas de processamento de linguagem natural (NLP). Ele
transforma o texto em uma forma mais digerível para que os algoritmos de aprendizado de máquina possam ter um desempenho
melhor.

Em qualquer tarefa de aprendizado de máquina, limpar ou pré-processar os dados é tão importante quanto a construção do
modelo, se não mais. E quando se trata de dados não estruturados, como texto, esse processo é ainda mais importante.

Algumas das etapas comuns de pré-processamento/limpeza de texto são:

* Lower casing ✔
* Removal of Punctuations ✔
* Removal of Stopwords ✔
* Removal of Frequent words ✔
* Removal of Rare words
* Stemming ✔
* Lemmatization ✔
* Removal of emojis ✔
* Removal of emoticons
* Conversion of emoticons to words
* Conversion of emojis to words ✔
* Removal of URLs ✔
* Removal of HTML tags ✔
* Chat words conversion
* Spelling correction
* Removal of numbers ✔

É preciso escolher cuidadosamente as etapas de pré-processamento com baseem nosso caso de uso, pois isso também
desempenha um papel importante. Por exemplo, no caso de uso de análise de sentimento, não precisamos remover os emojis
ou emoticons, pois isso transmitirá algumas informações importantes sobre o sentimento. Da mesma forma, precisamos
decidir com base em nossos casos de uso.

---

#### Let's code

### Lower casing

````python
input_str = "The 5 biggest countries by population in 2017 are China, India, United States, Indonesia, and Brazil"
input_str = input_str.lower()
print(input_str)
# the 5 biggest countries by population in 2017 are china, india, united states, indonesia, and brazil.
````

### Removal of Punctuations

Removendo este conjunto de símbolos !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~`:

```python
import string

input_str = "This &is [an] example? {of} string. with.? punctuation!!!!"  # Sample string
PUNCT_TO_REMOVE = string.punctuation
result = input_str.translate(str.maketrans("", "", PUNCT_TO_REMOVE))
print(result)  # This is an example of string with punctuation
```

### Removal of stopwords

"Palavras de parada" são as palavras mais comuns em um idioma como "o", "a", "on", "é", "todos". Essas palavras não
carregam significados importantes e geralmente são removidas dos textos. É possível remover palavras de parada usando o
Natural Language Toolkit (NLTK), um conjunto de bibliotecas e programas para processamento simbólico e estatístico de
linguagem
natural. [<b>Clique aqui para saber mais.</b>](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/README.md)

```python
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

input_str = "Nick likes to play football, however he is not too fond of tennis."

STOPWORDS = set(stopwords.words('english'))


def remove_stopwords(text):
    """custom function to remove the stopwords"""
    return " ".join([word for word in str(text).split() if word not in STOPWORDS])


print(remove_stopwords(input_str))  # Nick likes play football, however fond tennis.

tokens = word_tokenize(input_str)
result = [token for token in tokens if token not in STOPWORDS]
print(result)  # ['Nick', 'likes', 'play', 'football', ',', 'however', 'fond', 'tennis', '.']
```

### Removal of Frequent words

Na etapa de pré-processamento anterior, removemos as palavras irrelevantes com base nas informações do idioma. Mas
digamos, se tivermos um corpus específico de domínio, também podemos ter algumas palavras frequentes que não são tão
importantes para nós. Portanto, este passo é remover as palavras frequentes no corpus fornecido. Se usarmos algo como
tfidf, isso será resolvido automaticamente. Vamos pegar as palavras mais comuns e removê-las na próxima etapa

```python
from collections import Counter

input_str = "The 5 biggest countries by population population in 2017 are China, India, United States, Indonesia, and Brazil 2017"
cnt = Counter()
MAX_NUMBER_OF_WORDS_TO_REMOVE = 2

for word in input_str.split():
    cnt[word] += 1

# Top 10
print(cnt.most_common(10))

FREQWORDS = set([w for (w, wc) in cnt.most_common(MAX_NUMBER_OF_WORDS_TO_REMOVE)])


def remove_freq_words(text):
    """custom function to remove the frequent words"""
    return " ".join([word for word in str(text).split() if word not in FREQWORDS])


print(remove_freq_words(input_str))
# The 5 biggest countries by in are China, India, United States, Indonesia, and Brazil
```

### Stemming

Stemming é o processo de redução de palavras flexionadas (ou às vezes derivadas) ao seu radical, base ou
raiz ([Wikipedia](https://en.wikipedia.org/wiki/Stemming))

Por exemplo, se houver duas palavras no corpus `walks` e `walking`, então o stemming originará o sufixo para
fazê-los `walk`. Mas digamos em outro exemplo, temos duas palavras `console` e `consoling`, o lematizador irá remover o
sufixo e torná-las `consol` que não é uma palavra apropriada em inglês.

Existem vários tipos de algoritmos de stemming disponíveis e um dos mais famosos é o porter stemmer que é amplamente
utilizado. Podemos usar o pacote `nltk` para o mesmo.

```python
from nltk.stem.porter import PorterStemmer

input_str = "The 5 biggest countries by population population in 2017 are China, India, United States, Indonesia, and Brazil 2017"

stemmer = PorterStemmer()


def stem_words(text):
    return " ".join([stemmer.stem(word) for word in text.split()])


print(stem_words(input_str))
# the 5 biggest countri by popul popul in 2017 are china, india, unit states, indonesia, and brazil 2017
```

Podemos ver que o trabalho ocorreu nas palavras _countries_, _population_ e _United_, tiveram seu final cortado devido a
derivação.

Além disso, este stemmer de porteiro é para o idioma inglês. Se estivermos trabalhando com outras linguagens, podemos
usar o Snowball Stemmer. Os idiomas suportados para o snowball stemmer são:

```python
from nltk.stem.snowball import SnowballStemmer

print(SnowballStemmer.languages)

('arabic', 'danish', 'dutch', 'english', 'finnish', 'french', 'german', 'hungarian', 'italian', 'norwegian', 'porter',
 'portuguese', 'romanian', 'russian', 'spanish', 'swedish')
```

### Lemmatization

Lemmatization é semelhante à Stemming ao reduzir as palavras flexionadas ao radical da palavra, mas difere na maneira
como garante que a palavra raiz (também chamada de lemma) pertence ao idioma. Como resultado, este é geralmente mais
lento do que o processo de stemming. Portanto, dependendo do requisito de velocidade, podemos optar por usar stemming ou
lemmatization.

Vamos usar o `WordNetLemmatizer` em `nltk` para _lematizar_ nossas frases.

```python
from nltk.stem import WordNetLemmatizer

input_str = "The 5 biggest countries by population populations in 2017 are China, India, United States, Indonesia, and Brazil 2017"

lemmatizer = WordNetLemmatizer()


def lemmatize_words(text):
    return " ".join([lemmatizer.lemmatize(word) for word in text.split()])


print(lemmatize_words(input_str))
# The 5 biggest country by population population in 2017 are China, India, United States, Indonesia, and Brazil 2017
```

Podemos ver que o trabalho ocorreu nas palavras _population_ e _populations_.

Há mais uma coisa na lematização. Vamos tentar lematizar a `running` agora.

```python
lemmatizer.lemmatize("running")  # running
```

Ele retornou executando como tal sem convertê-lo para a execução do formulário raiz. Isso porque o processo de
lematização depende da `POS tag` para chegar ao lema correto. Agora vamos lematizar novamente fornecendo a `POS tag`
para a palavra.

```python
lemmatizer.lemmatize("running", "v")  # v para verbo
```

Agora estamos executando o formulário raiz. Portanto, também precisamos fornecer a `POS tag` da palavra junto com a
palavra para `lemmatizer` em nltk. Dependendo do `POS`, o `lemmatizer` pode retornar resultados diferentes. Por exemplo:

```python
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

word = 'openings'

print("Word is : ", word)
print("Resultado para verbo: ", lemmatizer.lemmatize(word, 'v'))  # Resultado para verbo:  open
print("Resultado para substantivo: ", lemmatizer.lemmatize(word, 'n'))  # Resultado para substantivo:  opening
```

Para finalizar podemos usar a seguinte funcão para Lemmatization da nossa base de dados:

```python
import nltk
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

word = 'openings drivers stripes'

wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}


def lemmatize_words(text):
    pos_tagged_text = nltk.pos_tag(text.split())
    return " ".join(
        [lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])


print(lemmatize_words(word))  # opening driver stripe
```

### Removal of Emojis

Com cada vez mais uso de plataformas de mídia social, há uma explosão no uso de emojis em nosso dia a dia também.
Provavelmente, talvez precisemos remover esses emojis para algumas de nossas análises
textuais. [F](https://stackoverflow.com/a/49146722/330558)

```python
import re


def remove_emoji(string):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)


print(remove_emoji("game is on 🔥🔥, Hilarious😂"))  # game is on , Hilarious

```

### Conversion of Emoji to Words

😀 is an emoji

```python
import emoji as e

text = "I am a coder 😎"
con = e.demojize(text)
print(con)  # I am a coder :smiling_face_with_sunglasses:
```

### Removal of URLs

```python
import re

text = "Please refer to link http://lnkd.in/ecnt5yC for the paper"


# ------------------- [1] Function
def remove_urls_1(text):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    return url_pattern.sub(r'', text)  # Please refer to link  for the paper


# ------------------- [2] Function
def remove_urls_2(text):
    return re.sub(r'https?://\S+|www\.\S+', '', text, flags=re.MULTILINE)  # Please refer to link  for the paper
```

### Removal of HTML Tags

Podemos acabar tendo strings html como parte do nosso texto.

Primeiro, vamos tentar remover as tags HTML usandoexpressões regulares.

```python
import re


def remove_html(text):
    html_pattern = re.compile('<.*?>')
    return html_pattern.sub(r'', text)
```

Também podemos usar o pacote BeautifulSoup para obter o texto do documento HTML de uma maneira mais elegante.

```python
from bs4 import BeautifulSoup


# ------------------- [1] Function
def strip_html_tags_1(text):
    return BeautifulSoup(text, "lxml").text


# ------------------- [2] Function
def strip_html_tags_2(text):
    soup = BeautifulSoup(text, "html.parser")
    result = soup.get_text(separator=" ")
    return print('Remover tags html: ', result)
```

### Spelling Correction

Uma outra etapa importante de pré-processamento de texto é a correção ortográfica. Erros de digitação são comuns em
dados de texto e talvez queiramos corrigir esses erros de ortografia antes de fazermos nossa análise. Vamos usar o
pacote python [pyspellchecker](https://pypi.org/project/pyspellchecker/) para nossa correção ortográfica.

`!pip install pyspellchecker`

```python
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
print(correct_spellings(text))  # carro mensagem cachorro
````

### Remove numbers

Remova os números se eles não forem relevantes para suas análises. Normalmente, expressões regulares são usadas para
remover números.

```python
import re

input_str = "Box A contains 3 red and 5 white balls, while Box B contains 4 red and 2 blue balls."
result = re.sub(r'\d+', '', input_str)
print(result)  # Box A contains red and white balls, while Box B contains red and blue balls.
```

### Remove whitespaces

Para remover espaços iniciais e finais, você pode usar a função strip()

```python
input_str = "\t a string example\t"
input_str = input_str.strip()
print(input_str)
# `a string example`
```

---

### Tokenization

Tokenização é o processo de dividir o texto fornecido em pedaços menores chamados tokens. Palavras, números, sinais de
pontuação e outros podem ser considerados como tokens.
