import plotly.express as px 
  
# data to be pltted
df = px.data.tips() 
  
# plotting the figure
fig = px.line_3d(df, x="sex", y="day", 
                 z="time", color="sex") 
  
fig.show()