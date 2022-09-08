import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_length", y="sepal_width", width=800, height=500, title='Gráfico de Dispersão',
                 color='species', size='petal_length')

# In jupyter can use:
# fig.show()

fig.write_html('first_figure.html', auto_open=True)
