<img src="https://i.ibb.co/M6nBBb0/mascote.png" align="right" width="130">

# Python

## Gráficos - visualização

Criando visualizações estáticas, animadas e interativas, usando [Matplotlib](https://matplotlib.org/)
/ [Plotly](https://plotly.com/graphing-libraries/).

#### _Let's Go Code!_

- **Seaborn**
    - Seaborn heatmap.
- **Plotly Express**
    - Dispersão animada.
    - Boxplot - Diagrama de caixa.
    - Histogram - Histograma.
    - Gráfico de Linha.
    - Gráfico de Dispersão.
    - Gráfico de Dispersão colorido.
    - Gráfico de Regressão Linear.
- **Matplotlib**
    - Visualização de um gráfico usando 6 linhas de código.
    - Desenhar gráfico de barra.
    - Desenhar gráfico de pizza.
    - Plotagem com variáveis categóricas.

_Extra_: **Word Clouds** (também conhecidas como wordle, word collage ou tag cloud) são representações visuais de
palavras que dão maior destaque às palavras que aparecem com mais frequência.

- [WordCLoud exemplo.](https://github.com/JoseMateusCamargo/python/blob/main/graph/wordcloud_example.py)

---

## Seaborn

[Seaborn](https://seaborn.pydata.org/index.html) é uma biblioteca de visualização de dados Python baseada em
matplotlib. Ele fornece uma interface de alto nível para desenhar gráficos estatísticos atraentes e informativos.

**Seaborn heatmap**

```python
import numpy as np
import seaborn as sns

np.random.seed(0)

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers")

# Documentation: https://seaborn.pydata.org/generated/seaborn.heatmap.html

# Annotate each cell with the numeric value using integer formatting: annot - fmt
# Use a different colormap: cmap
# Add lines between each cell: linewidth
ax = sns.heatmap(flights, annot=True, fmt="d", cmap="YlGnBu", linewidths=.5)
```

---

## Plotly Express

O módulo [plotly.express](https://plotly.com/python/plotly-express/) (geralmente importado como px) contém funções
que podem criar figuras inteiras de uma só vez e é chamado de Plotly Express ou PX. Plotly Express é uma parte
interna da biblioteca de plotagens e é o ponto de partida recomendado para a criação de figuras mais comuns.

```python
# In jupyter can use:
# fig.show()
```

**Dispersão animada**

```python
import plotly.express as px

df = px.data.gapminder()
fig = px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
                 size="pop", color="continent", hover_name="country", facet_col="continent",
                 log_x=True, size_max=45, range_x=[100, 100000], range_y=[25, 90])

fig.write_html('first_figure.html', auto_open=True)
```

**Boxplot - Diagrama de caixa**

```python
import plotly.express as px

df = px.data.iris()
fig = px.box(df, y="sepal_length", width=800, height=500, title='Gráfico Boxplot', x='species')

fig.write_html('first_figure.html', auto_open=True)
```

**Histogram - Histograma**

```python
import plotly.express as px

df = px.data.iris()
fig = px.histogram(df, x="sepal_length", width=800, height=500, title='Gráfico Histograma', nbins=20)

fig.write_html('first_figure.html', auto_open=True)
```

**Gráfico de Linha**

```python
import plotly.express as px

df = px.data.iris()
fig = px.line(df, y="sepal_length", width=800, height=500, title='Gráfico de Linha')

fig.write_html('first_figure.html', auto_open=True)
```

**Gráfico de Dispersão**

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", width=800, height=500, title='Gráfico de Dispersão')

fig.write_html('first_figure.html', auto_open=True)
```

**Gráfico de Dispersão colorido**

```python
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", width=800, height=500, title='Gráfico de Dispersão',
                 color='species', size='petal_length')

fig.write_html('first_figure.html', auto_open=True)
```

**Gráfico de Regressão Linear**

```python
import plotly.express as px

# Documentation: https://plotly.com/python/line-and-scatter/
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")

fig.write_html('first_figure.html', auto_open=True)
```

----

## Matplotlib

[Matplotlib](https://matplotlib.org) é uma biblioteca abrangente para criar visualizações estáticas, animadas e
interativas em Python. O Matplotlib torna as coisas fáceis fáceis e as difíceis possíveis.

**Visualização de um gráfico usando 6 linhas de código**

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]

title = 'Graphic'
plt.suptitle(title)
plt.plot(x, y)
```

**Desenhar gráfico de barra**

```python
import numpy as np
import matplotlib.pyplot as plt

plt.rcdefaults()

months = ('jan', 'fev', 'mar', 'abr', 'mai', 'jun')
y_pos = np.arange(len(months))  # Eixo y
performance = [2342, 34234, 2525, 2525, 20470, 5334]

# Documentation: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html

# plt.bar plot com barras verticais
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, months)

"""
# plt.barh plot com barras horizontais
plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, months)  # define os locais e os rótulos dos xticks
"""

plt.ylabel('Receita R$')
plt.title('Receita 1º semestre')

plt.show()
```

**Desenhar gráfico de pizza**

```python
import matplotlib.pyplot as plt

# -------------------- [1 Example]
values = [40, 10, 50]
labels = ['PHP', 'JavaScript', 'Python']

plt.figure(figsize=(10, 8))
plt.pie(values, labels=labels, autopct="%1d%%")
plt.title('Favorites languages')
plt.show()

# -------------------- [2 Example]
labels = 'Laranja', 'Banana', 'Melancia', 'Abacate'
sizes = [20, 30, 40, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Banana')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Proporção de aspecto igual garante o desenho como um círculo.
plt.show()
```

**Plotagem com variáveis categóricas**

```python
import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```