<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python Snippets

<p>
  Material com exemplos Python.<br/>
</p>

- ✔ [How to use (manual)](https://github.com/JoseMateusCamargo/python/tree/main/how-to-use#readme)
    - Generators, filter, map, list, argparse, dic...
- ✔ [Computer Vision](https://github.com/JoseMateusCamargo/python/tree/main/computer-vision#readme)
    - OpenCV, Face Detection, Object size measurement...
- ✔ [Manipulando arquivos CSV](https://github.com/JoseMateusCamargo/python/tree/main/csv-manipulating#readme)
    - Consolidar, ler, comparar, salvar...
- ✔ [Conexões com banco de dados](https://github.com/JoseMateusCamargo/python/tree/main/db-connection#readme)
    - Insert, select, update...
- ✔ [Flask (Web app)](https://github.com/JoseMateusCamargo/python/tree/main/flask#readme)
- ✔ [Streamlit (Web app)](https://github.com/JoseMateusCamargo/python/tree/main/streamlit#readme)
- ✔ **Geometria**
    - Distância Euclidiana e Manhattan.
- ✔ [Gráficos - visualização](https://github.com/JoseMateusCamargo/python/tree/main/graph#readme)
    - Matplotlib, Plotly Express e Seaborn.
    - [Turtle (_Gráfico tartaruga_)](https://github.com/JoseMateusCamargo/python/tree/main/turtle#readme)
- ✔ [Interview questions](https://github.com/JoseMateusCamargo/python/blob/master/interview-question/README.md)
- ✔ [**Neural Style Transfer**](https://github.com/JoseMateusCamargo/python/blob/main/neural-style-transfer/main.py)
    - Neural Style Transfer é um processo que usa redes neurais para aplicar o estilo artístico de uma imagem para
      outra.
- ✔ [**OCR** (Optical Character Recognition)](https://github.com/JoseMateusCamargo/python/tree/main/ocr#readme)
    - Reconhecimento de Textos em imagens: _Google's Tesseract-OCR_ e _EasyOCR_.
- ✔ [**Pandas**](https://github.com/JoseMateusCamargo/python/tree/main/pandas#readme)
    - drop, to_datetime, isin...
- [Algoritmos de pesquisa (_Search
  Algorithms_)](https://github.com/JoseMateusCamargo/python/blob/master/search-algorithm/README.md)
- Web Scraping.
    - Usando `BeautifulSoup`
- Stop Words.
- ✔ Text-to-speech.
- Comandos e dicas
    - Reduza o tamanho do arquivo executável criado pelo `PyInstaller` no `Conda`.
    - Instalando um modulo usando `pip` em uma versão específica do python.
    - Como atualizar um pacote _Python Jupter Notebook_ usando `pip`.

---

### Geometria ✔

**Distância Euclidiana**

Em matemática, distância euclidiana (ou distância métrica) é a distância entre dois pontos, que pode ser provada pela
aplicação repetida do teorema de Pitágoras. Aplicando essa fórmula como distância, o espaço euclidiano torna-se um
espaço métrico, ou seja, soma da raiz quadrada da diferença entre `x` e `y` em suas respectivas dimensões,
geograficamente seria a `hipotenusa` de uma
triângulo. [Métodos para calcular a distância Euclidiana.](https://github.com/JoseMateusCamargo/python/blob/master/geometric/euclidean_distance.py)

**Fórmula**: √((X<sub>1</sub> - X<sub>2</sub>)<sup>2</sup>) + (Y<sub>1</sub> - Y<sub>2</sub>)<sup>2</sup>)

<img src="https://media.geeksforgeeks.org/wp-content/uploads/20200201225751/unnamed4.png" width="225">

**Distância Manhattan**

É apenas a soma das diferenças entre x e y em cada dimensão, essa medida de distância também e conhecida como City
Block, geograficamente seriam a soma dos catedos

**Fórmula**: |X<sub>1</sub> - X<sub>2</sub>| + |Y<sub>1</sub> - Y<sub>2</sub>|

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/800px-Manhattan_distance.svg.png" width="225">

---

### Web Scraping

O **web scraping** (raspagem de rede, em tradução livre), também conhecido como extração de dados da web, é o nome dado
ao processo de coleta de dados estruturados da web de maneira automatizada.

Usando `BeautifulSoup`:

* [Weather data collection.](https://github.com/JoseMateusCamargo/python/blob/master/scraping/weather.py)
* [Extracting Data from table HTML, example 02.](https://github.com/JoseMateusCamargo/python/blob/master/scraping/scraping_data_01.py)
* [Extracting Data from table HTML, example 01.](https://github.com/JoseMateusCamargo/python/blob/master/scraping/extracting_data.py)

---

### Stop Words

O que são palavras de parada? 🤔 As palavras que geralmente são filtradas antes do processamento de uma linguagem
natural são chamadas de palavras de interrupção.

- [Stop Words click here.](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/README.md)

---

### Text-to-speech

A síntese da fala é a produção artificial da fala humana. Um sistema de computador usado para essa finalidade é chamado
de computador de fala ou sintetizador de fala e pode ser implementado em produtos de software ou hardware. Um sistema de
texto para fala (TTS) converte o texto do idioma normal em fala; outros sistemas renderizam representações linguísticas
simbólicas como transcrições fonéticas em fala. [Wikipedia](https://en.wikipedia.org/wiki/Speech_synthesis).

* [Voice Recognition and Speech Synthesis.](https://github.com/JoseMateusCamargo/python/tree/main/tss-text-to-speech#readme)

---

### PyWhatKit

<i>Automate WhatsApp Messages with Python Instantly!</i>

> [<b>PyWhatKit</b>](https://pypi.org/project/pywhatkit/) is a Python library with various helpful features. It's
> easy-to-use and does not require you to do any additional setup. Currently, it has about 300k+ downloads and counting.
> New updates are released frequently with new features and bug fixes.

#### Let's code

* [Convert image to ASCII art.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/pywhatkit_examples/img_to_ASCII.py)
* [Using WhatsApp Message.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/pywhatkit_examples/wzap_usage.py)
* [Convert text to <i>Hand Written</i> text.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/pywhatkit_examples/handwriting_save.py)

#### Features

* Sending Message to a WhatsApp Group or Contact.
* Sending Image to a WhatsApp Group or Contact.
* Converting an Image to ASCII Art.
* Converting a String to Handwriting.
* Playing YouTube Videos.
* Sending Mails with HTML Code.
* Install and Use.

---

### Tkinter — Python interface to Tcl/Tk

> O pacote [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter) ("TK Interface") é a interface
> Python padrão para o kit de ferramentas TCL / TK GUI. Tanto o Tk quanto
> o tkinter estão disponíveis na maioria das plataformas Unix, incluindo macOS, bem como em sistemas Windows.

* [Spelling correction with <b>textblob</b> (Simplified Text Processing).](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/tkinter-examples/tk_textblob_spelling_correction.py)
* [<b>Tkinter</b> Open File Dialog, <i>GUI interface</i>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/tkinter-examples/tk_openfile_example.py)

----

### Package Scripts

* [Extraindo arquivos `.zip` com <b>zipfile</b>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/zip_extrac.py)
* [Generate ASCII artistic images of a cow with a message. :hand_over_mouth:](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/art_in_console.py)
* [Displaying Windows 10 toast notifications.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/windows_notification.py)
* [How to display a calendar.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/the_calendar.py)
* [Instagram automation with 06 lines of code!.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/insta_post.py)
* [Convert `Html` to `PDF` using <b>pdfkit</b>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/html_to_pdf.py)
* [Creating a Simple Map with <b>Folium</b>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/maps_using_folium.py)
* [Geocode phone number.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/phone_carrier_geocoder.py)
* [Translator with <b>Google Translate</b> behind it.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/translator.py)
* [Using the most famous URL Shorteners.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/tinyurl_shorteners.py)
* [How to Generate Barcode.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/barcode_.py)
* [Access and parse data from Wikipedia.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/use_wikipedia.py)
* [Downloading YouTube Videos.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/youtube_download.py)

### Scripts

* [Criando uma schedule com `schedule`.]()
* [Returns the IP address of the host.](https://github.com/JoseMateusCamargo/python/blob/master/scripts/get_ip_address.py)
* [How to Use Progress Bars.](https://github.com/JoseMateusCamargo/python/blob/master/scripts/progress_bar.py)
* [Take a screenshot with <b>Selenium WebDriver</b>.](https://github.com/JoseMateusCamargo/python/blob/master/scripts/screenshot_selenium.py)
* [Print Emojis.](https://github.com/JoseMateusCamargo/python/blob/master/scripts/using_emoji.py)
* [How to print colored text using <b>Colorama</b>.](https://github.com/JoseMateusCamargo/python/blob/main/scripts/print_colored_text.py)

### [Dicas](https://github.com/JoseMateusCamargo/python/blob/main/tips-and-others/README.md)

- Renomeando arquivo.
- _List Comprehensions_, ler arquivo em um linha de codigo.
- _Factorial_, função para aplicar fatorial.
- _Anagram_, função para checar se string é anagrama.
- Retornando a memória utilizada por um objeto.
- _Odd or Even_, checando se um numero é impar ou par.
- Trabalhando com `split` e `join`.
- Formatar string com `f-string`.
- Atribuição de múltiplas variávies.
- Trocar valor de 02 variávies.
- Print _N_ vezes uma string.
- _Palindrome_, reverter string (palindrome).
- Formar `string` a partir dos elementos de uma `lista`.
- Armazenar elementos de uma `lista` diretamente em variávies.
- `swapcase()` o método retorna uma string onde todas as letras maiúsculas são minúsculas e vice-versa.
- [Operações basicas (média, mediana e quantil).](https://github.com/JoseMateusCamargo/python/blob/main/tips-and-others/mean_median_quantile.py)

---

## Comandos

**Reduza o tamanho do arquivo executável criado pelo `PyInstaller` no `Conda`**

Para alterar o environtment, use: `conda activate NOME_DO_ENVIRONMENT`

```shell
# 1. Criando uma nova (conda environtment)
conda create -n NAME_OF_NEW_ENV

# 2. Instalando pip 
conda install pip

# 3. Instalando outro pacote
pip install numpy scipy matplotlib

# 4. Listando pacotes instalados no (environment)
conda list
# or
pip list

# 5. Instalando PyInstaller
pip install pyinstaller

# 6. Agora podemos construir um arquivo executavel atraves de um script Python usando PyInstaller
pyinstaller example.py

# Para construir um unico arqvuio executavel, use a opção PyInstaller -F ou --onefile 
```

**Instalando um modulo usando `pip` em uma versão específica do python**

```shell
python_version -m pip install your_package
# or 
path/to/your/python_version -m pip install your_package

```

**Como atualizar um pacote _Python Jupter Notebook_ usando `pip`**

```shell
!pip list -o # lists outdated packages  
!pip list -u # lists up-to-date packages  
!pip install -U <name_lib> # up-to-date the package
```

### Direitos de uso (Use rights)

<p>
  Você tem todo o direito de usar esse material para seu próprio aprendizado.<br/>
  You can use this material for your own learning.
</p>
