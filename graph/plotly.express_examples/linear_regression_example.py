import plotly.express as px

# Documentation: https://plotly.com/python/line-and-scatter/
df = px.data.tips()
fig = px.scatter(df, x="total_bill", y="tip", trendline="ols")

# In jupyter can use:
# fig.show()

fig.write_html('first_figure.html', auto_open=True)
