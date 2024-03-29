<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Turtle graphics

O [Turtle](https://docs.python.org/3/library/turtle.html#module-turtle) (“Tartaruga” em inglês) é um módulo do Python
para desenhar utilizando a lógica de programação. É uma extensão da linguagem de programação chamada Logo, a qual foi
criada em 1967.

A ideia principal do Turtle é que temos uma Tartaruga em um canvas (tela para desenho), onde utilizamos comandos
estruturados em uma determinada lógica para criarmos o nosso desenho.

#### _Let's Code!_

- Gráfico estrela.
- Gráfico estrela usando `array` de cores.

---

**Gráfico estrela**

```python
from turtle import *

color('red', 'yellow')
begin_fill()

while True:
    forward(200)
    left(170)

    if abs(pos()) < 1:
        break

end_fill()
done()
```

**Gráfico estrela usando array de cores**

```python
import turtle

colors = ['yellow', 'red', 'blue', 'green', 'magenta', 'cyan', 'orange']

t = turtle.Turtle()
t.begin_fill()

screen = turtle.Screen()
screen.bgcolor('white')
t.speed(30)

for i in range(120):
    t.color(colors[i % 6])
    t.forward(i * 4)
    t.left(150)
    t.width(2)

t.end_fill()
turtle.exitonclick()
```

## Fim
