<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="225">

# Stop Words

#### Palavra vazia (Stop word)

O que são palavras de parada? 🤔 As palavras que geralmente são filtradas antes do processamento de uma linguagem
natural são chamadas de palavras de interrupção. Na verdade, essas são as palavras mais comuns em qualquer idioma (como
artigos, preposições, pronomes, conjunções, etc.) e não acrescentam muitas informações ao texto.

#### Let's Go Code!

Para remover palavras de strings existem várias bibliotecas de processamento de linguagem natural, como NLTK, SpaCy,
Gensim, TextBlob, etc. ou, ainda podemos usar um script personalizado.

### Utilizando a biblioteca NLTK

[NLTK](https://www.nltk.org/) é uma plataforma líder para a construção de programas Python para trabalhar com dados de
linguagem humana. Ele fornece interfaces fáceis de usar para mais de 50 corpora e recursos lexicais, como WordNet, junto
com um pacote> de bibliotecas de processamento de texto para classificação, tokenização, lematização, marcação, análise
e raciocínio> semântico, wrappers para bibliotecas de PNL de força industrial...

* [Stop Words com NLTK.](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/nltk_stop_words.py)

### Utilizando a biblioteca Gensim

[Gensim](https://pypi.org/project/gensim/) é uma biblioteca Python para modelagem de tópicos, indexação de documentos e
recuperação de similaridade com> grandes corpora. O público-alvo é a comunidade de processamento de linguagem natural (
PNL) e recuperação de informações (RI).

* [Stop Words com Gensim.](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/gensim_stop_words.py)

### Utilizando a biblioteca SpaCy

[spaCy](https://spacy.io/) é uma biblioteca para processamento avançado de linguagem natural em Python e Cython. É
construído com base nas pesquisas mais recentes e foi projetado desde o primeiro dia para ser usado em produtos reais.

Requirements:

```shell
pip install -U spacy  
python -m spacy download en
```

* [Stop Words com spaCy.](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/spacy_stop_words.py)

### Utilizando um script personalizado

Agora com um script personalizado.

* [Stop Words script.](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/manual_script_stop_words.py)

### Direitos de uso (Use rights)

<p>
  Você tem todo o direito de usar esse material para seu próprio aprendizado.<br/>
  You can use this material for your own learning.
</p>