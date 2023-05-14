import re
import string  # library that contains punctuation
import nltk
from bs4 import BeautifulSoup
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import contractions
import spacy
from word2number import w2n

# load spacy model, can be "en_core_web_sm" as well
nlp = spacy.load('pt_core_news_sm')

text = "vida estamos online amore carreira carreiras três copos de café () $ ### ... _! geese crazy Im  me here not rocks entry don't <br></b> three cups of coffee"
print()


# ------------------- [] Remove extra whitespaces from text
def remove_whitespace():
    result = text.strip()
    return print('Remover espaços: ', " ".join(result.split()))


# -------------------- [] Remove punctuation: ‘!”#$%&'()*+,-./:;?@[\]^_`{|}~’
def remove_punctuation():
    result = "".join([i for i in text if i not in string.punctuation])
    return print('Remover pontuação: ', result)


# -------------------- [] Remove punctuation using re: ‘!”#$%&'()*+,-./:;?@[\]^_`{|}~’
def remove_punctuation_using_re():
    result = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', text.encode().decode('utf-8'))
    return print('Remover pontuação com RE: ', result)


# --------------------- [] Expand shortened words, e.g. don't to do not
def expand_contractions():
    result = contractions.fix(text)
    return print('Expand shortened words: ', result)


def treatment_for_numbers():
    doc = nlp(text)
    result = [w2n.word_to_num(token.text) if token.pos_ == 'NUM' else token for token in doc]
    return print(result)


# -------------------- [2] Tokenization Function
def tokenization():
    return nltk.word_tokenize(text)


# -------------------- [3] Stopwords Function
# print(f'Stop words present: {stopwords[0:10]}')
# Output: Stop words present: ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're"]
stopwords = nltk.corpus.stopwords.words('english')


def remove_stopwords():
    text_tokenized = tokenization()
    result = " ".join([token for token in text_tokenized if token not in stopwords[0:10]])
    return print(result)


# -------------------- [4] Stemming Function
def stemming_porter_stemmer():
    porter_stemmer = PorterStemmer()
    text_tokenized = tokenization()
    result = " ".join([porter_stemmer.stem(word) for word in text_tokenized])
    return print('Stemming using PorterStemmer: ', result)


''' Output example:
crazy-> crazi
geese-> gees
'''


# -------------------- [5] Lemmatization Function
def lemmatizer_word_net_lemmatizer():
    lemmatizer_ = WordNetLemmatizer()
    text_tokenized = tokenization()
    result = " ".join([lemmatizer_.lemmatize(word) for word in text_tokenized])
    return print('Lemmatizer using WordNetLemmatizer: ', result)


''' Output example:
geese-> goose
'''


# -------------------- [5] Lemmatization using spacy
def lemmatizer_spacy():
    doc = nlp(text)
    # Lemmatizing each token
    result = " ".join([word.lemma_ if word.lemma_ != "-PRON-" else word.lower_ for word in doc])
    return print('Lemmatizer using Spacy: ', result)


''' Output example:
geese-> goose
'''

strip_html_tags()
remove_whitespace()
remove_punctuation()
remove_punctuation_using_re()
expand_contractions()
remove_stopwords()
stemming_porter_stemmer()
lemmatizer_word_net_lemmatizer()
lemmatizer_spacy()
