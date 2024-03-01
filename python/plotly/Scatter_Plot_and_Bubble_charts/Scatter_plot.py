import plotly.express as px 
  
# using the iris dataset
df = px.data.iris() 
  
# plotting the scatter chart
fig = px.scatter(df, x="petal_width", y="petal_width") 
  
# showing the plot
fig.show()