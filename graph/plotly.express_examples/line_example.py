import plotly.express as px

df = px.data.iris()
fig = px.line(df, y="sepal_length", width=800, height=500, title='Gráfico de Linha')

# In jupyter can use:
# fig.show()

fig.write_html('first_figure.html', auto_open=True)
