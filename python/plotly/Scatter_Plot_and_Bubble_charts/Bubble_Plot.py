import plotly.express as px 
  
# using the iris dataset
df = px.data.iris() 
  
# plotting the bubble chart
fig = px.scatter(df, x="species", y="petal_width", 
                 size="petal_length", color="petal_width") 
  
# showing the plot
fig.show()