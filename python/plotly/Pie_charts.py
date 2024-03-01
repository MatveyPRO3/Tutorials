import plotly.express as px 
  
# using the tips dataset
df = px.data.tips() 
  
# plotting the pie chart
fig = px.pie(df, values="total_bill", names="day") 
  
# showing the plot
fig.show()