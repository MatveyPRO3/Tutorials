import plotly.express as px
import numpy as np
accuracy = int(input("Enter accuracy: "))
x = np.linspace(-10, 10, num=20 * accuracy)
fig = px.line(x=x, y=np.sin(x))
fig.show()
