<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Flask

[Flask](https://flask.palletsprojects.com/en/2.0.x/) é uma estrutura leve de aplicativo da
web [WSGI](https://wsgi.readthedocs.io/en/latest/), foi projetado para
tornar os primeiros passos rápidos e fáceis, com a capacidade de escalar para aplicativos complexos, começou como um
invólucro simples em torno de [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) e
[Jinja](https://jinja.palletsprojects.com/en/3.0.x/) e se tornou uma das estruturas de aplicativos da web Python mais
populares.

#### _Let's Code!_

- Hello World.
- [Video Streaming com OpenCV & Flask.](https://github.com/JoseMateusCamargo/python/blob/master/flask-examples/opencv_streaming_web/app.py)
    - Transmissão de vídeos ao vivo de câmeras IP ou webcam com visão computacional.
- _Configuração para deploy_.

---

**Hello World**

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_():
    return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)
```

---

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