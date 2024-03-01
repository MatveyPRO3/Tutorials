import plotly.express as px 
  
# using the iris dataset
df = px.data.iris() 
  
# plotting the histogram
fig = px.histogram(df, x="sepal_length", y="petal_width") 
  
# showing the plot
fig.show()