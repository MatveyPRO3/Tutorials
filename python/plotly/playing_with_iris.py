import plotly.express as px

df = px.data.iris()

fig = px.line(df, x="sepal_width",y = "petal_width")
fig.show()