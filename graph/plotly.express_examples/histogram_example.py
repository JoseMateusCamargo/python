import plotly.express as px

df = px.data.iris()
fig = px.histogram(df, x="sepal_length", width=800, height=500, title='Gráfico Histograma', nbins=20)

# In jupyter can use:
# fig.show()

fig.write_html('first_figure.html', auto_open=True)
