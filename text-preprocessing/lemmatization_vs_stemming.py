import pandas as pd
import nltk
import spacy

df_palavras = pd.DataFrame(
    ['programação', 'programa', 'carreira', 'carreiras', 'vida', 'vidente', 'tempestade', 'temperamento'],
    columns=['palavras'])

print(df_palavras)

# Stemmer
'''
Na stemming vamos analisar cada palavra individualmente e reduzi-la à sua raiz ou, como é chamado na técnica, 
ao seu stem. Uma característica dessa técnica é que ela pode reduzir a palavra a uma outra gramaticalmente incorreta, 
porém ainda com valor para nossa análise.
'''
nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()

df_palavras['nltk_stemmer'] = [stemmer.stem(palavra) for palavra in df_palavras['palavras']]
print(df_palavras)

# Spacy lemmatization
'''
Na lemmatization a técnica é reduzir a palavra à sua raiz, retirando todas as inflexões e chegando ao lemma. 
Rresultará em uma palavra que realmente existe na gramática. Outro ponto importante é que, 
nessa técnica, a classe gramatical da palavra será levada em consideração para fazer a redução.
'''
# !python -m spacy download pt
nlp = spacy.load('pt_core_news_sm')
df_palavras['spacy_lemma'] = df_palavras['palavras'].apply(lambda x: " ".join([y.lemma_ for y in nlp(str(x))]))
print(df_palavras)
