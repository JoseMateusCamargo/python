<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python Snippets

<p>
  Material simples com exemplos em Python.<br/>
  Simple material with Python examples.
</p>

- ✔ [How to use (manual)](https://github.com/JoseMateusCamargo/python/tree/main/how-to-use#readme)
    - Usando **generators**.
    - Usando função `filter` com lambda.
    - Usando função `map`.
    - _Métodos_ usado em uma `lista`.
    - Como passar uma lista como um _argumento_ usando `argparse`.
    - Dominando **dicionários**.
- ✔ [Computer Vision.](https://github.com/JoseMateusCamargo/python/tree/main/computer-vision#readme)
- ✔ [Manipulando arquivos CSV.](https://github.com/JoseMateusCamargo/python/blob/main/csv-manipulating/README.md)
- ✔ [Conexões com banco de dados.](https://github.com/JoseMateusCamargo/python/blob/main/db-connection/README.md)
    - Insert, select, update ...
- Flask. ✔
- [Streamlit.](https://github.com/JoseMateusCamargo/python/tree/main/stream-lit#readme)
- Geometria. ✔
    - Distância Euclidiana
    - Distância Manhattan
- Gráficos e visualização.
- [Some interview questions.](https://github.com/JoseMateusCamargo/python/blob/master/interview-question/README.md)
- Neural Style Transfer.
- Trabalhando com Pandas ✔
- [Algoritmos de pesquisa (Search Algorithms)](https://github.com/JoseMateusCamargo/python/blob/master/search-algorithm/README.md)
- Scraping (BeautifulSoup)
- Stop Words
- Text-to-speech
- Comandos e dicas
    - Reduza o tamanho do arquivo executável criado pelo `PyInstaller` no `Conda`.
    - Instalando um modulo usando `pip` em uma versão específica do python.
    - Como atualizar um pacote _Python Jupter Notebook_ usando `pip`.

---

### DataBase Connection (insert, select, update ...)

* [Conexão MySQL usando `mysql.connector`.](https://github.com/JoseMateusCamargo/python/blob/main/db-connection/mysql.connector_connection.py)
* [Inserindo dados `DataFrame` em MySQL usando `mysql.connector`.](https://github.com/JoseMateusCamargo/python/blob/main/db-connection/pymysql_dataframe_connection.py)
* [Conexão MySQL usando `pymysql`.](https://github.com/JoseMateusCamargo/python/blob/main/db-connection/pymysql_connection.py)
* [Conexão SQLite usando `sqldf`.](https://github.com/JoseMateusCamargo/python/blob/main/db-connection/sqldf_connection.py)

### Trabalhando com Pandas

* [Selecionando linhas usando valor da coluna(s).](https://github.com/JoseMateusCamargo/python/blob/master/pandas/get_list_all_duplicate_row.py)
* [Remover ou selecionar linhas duplicadas na DataFrame.](https://github.com/JoseMateusCamargo/python/blob/master/pandas/how_to_drop_duplicate_rows.py)
* [Selecionar linhas com base em vários valores de coluna.](https://github.com/JoseMateusCamargo/python/blob/master/pandas/select_rows_by_conditions_multiples_column.py)
* [Excluir linhas com base em vários valores de coluna.](https://github.com/JoseMateusCamargo/python/blob/master/pandas/drop_rows_based_on_column_values.py)
* [Trabalhando com **datas**.](https://github.com/JoseMateusCamargo/python/blob/master/pandas/work_with_dates.py)

---

### Gráficos - visualização

Desenvolvendo visualizações estáticas, animadas e interativas, com `Matplotlib`, `Plotly` e `Seaborn`.

* [Visualização de dados em Python](https://github.com/JoseMateusCamargo/python/blob/master/graph/README.md)

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

### Scraping (BeautifulSoup)

* [Weather data collection.](https://github.com/JoseMateusCamargo/python/blob/master/scraping/weather.py)
* [Extracting Data from table HTML, example 02.](https://github.com/JoseMateusCamargo/python/blob/master/scraping/scraping_data_01.py)
* [Extracting Data from table HTML, example 01.](https://github.com/JoseMateusCamargo/python/blob/master/scraping/extracting_data.py)

---

### Stop Words

> O que são palavras de parada? 🤔 As palavras que geralmente são filtradas antes do processamento de uma linguagem
> natural são chamadas de palavras de interrupção.
> [Stop Words click here.](https://github.com/JoseMateusCamargo/python/blob/master/stop-words/README.md)

---

### Text-to-speech

A síntese da fala é a produção artificial da fala humana. Um sistema de computador usado para essa finalidade é chamado
de computador de fala ou sintetizador de fala e pode ser implementado em produtos de software ou hardware. Um sistema de
texto para fala (TTS) converte o texto do idioma normal em fala; outros sistemas renderizam representações linguísticas
simbólicas como transcrições fonéticas em fala. [Wikipedia](https://en.wikipedia.org/wiki/Speech_synthesis).

* [Voice Recognition and Speech Synthesis.](https://github.com/JoseMateusCamargo/python/tree/master/tss-text-to-speech#readme)

---

### Flask ✔

[Flask]() é uma estrutura leve de aplicativo da web [WSGI](https://wsgi.readthedocs.io/en/latest/), foi projetado para
tornar os primeiros passos rápidos e fáceis, com a capacidade de escalar para aplicativos complexos, começou como um
invólucro simples em torno de [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) e
[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) e se tornou uma das estruturas de aplicativos da web Python mais
populares.

* [Hello World usando <b>Flask</b>.](https://github.com/JoseMateusCamargo/python/blob/master/flask-examples/hello_world.py)
* [Video Streaming com OpenCV & Flask.](https://github.com/JoseMateusCamargo/python/blob/master/flask-examples/opencv_streaming_web/app.py)
    * Transmissão de vídeos ao vivo de câmeras IP ou webcam com visão computacional

**Configuração para deploy**

Uma das alternativas é instalar o pacote **python-dotenv**, `pip install python-dotenv` e criar um arquivo **.flaskenv**
na parta raiz do projeto, e adicionar:

``` commandline
FLASK_APP=app.py (ou o nome da sua aplicação)
FLASK_ENV=development (ou production)
```

**Truque**!! 😉 (caso tenhamos problema na criação do arquivo **.flaskenv** | _Erro : "You must type a file name"_)

Crie um novo arquivo e chame de `.flaskenv.` então salve automaticamente será removida a terminação `'.'`, extranho mas
funciona 😅

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

### Build Optical Character Recognition (OCR)

> Dentro da área da Visão Computacional existe a sub-área de Reconhecimento Ótico de Caracteres (ou OCR – Optical
> Character Recognition) que basicamente visa transformar imagens em textos. Em outras palavras, o OCR pode ser descrito
> como a conversão de imagens contendo texto digitado, escrito a mão ou impresso, em caracteres que uma máquina é capaz
> de entender.
>

* [Recognize and “read” the text with <b>Google's Tesseract-OCR</b>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/ocr-examples/tesseract_example.py)
* [Text detection from images using <b>EasyOCR</b>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/ocr-examples/easyocr_example.py)

---

### Tkinter — Python interface to Tcl/Tk

> O pacote [tkinter](https://docs.python.org/3/library/tkinter.html#module-tkinter) ("TK Interface") é a interface
> Python padrão para o kit de ferramentas TCL / TK GUI. Tanto o Tk quanto
> o tkinter estão disponíveis na maioria das plataformas Unix, incluindo macOS, bem como em sistemas Windows.

* [Spelling correction with <b>textblob</b> (Simplified Text Processing).](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/tkinter-examples/tk_textblob_spelling_correction.py)
* [<b>Tkinter</b> Open File Dialog, <i>GUI interface</i>.](https://github.com/JoseMateusCamargo/python/blob/master/package-scripts/tkinter-examples/tk_openfile_example.py)

----

### Turtle — Turtle graphics

* [Start example using loop.](https://github.com/JoseMateusCamargo/python/blob/master/turtle_examples/turtle_star_loop.py)
* [Start example.](https://github.com/JoseMateusCamargo/python/blob/master/turtle_examples/turtle_star.py)

---

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