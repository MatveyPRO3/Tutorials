import numpy as np
import plotly.graph_objects as go 
  
  
# Creating the X, Y value that will
# change the values of Z as a function
feature_x = np.arange(0, 50, 2) 
feature_y = np.arange(0, 50, 3) 
  
# Creating 2-D grid of features 
[X, Y] = np.meshgrid(feature_x, feature_y) 
  
Z = np.cos(X / 2) + np.sin(Y / 4) 
  
# plotting the figure
fig = go.Figure(data =
    go.Contour(x = feature_x, y = feature_y, z = Z)) 
  
fig.show()