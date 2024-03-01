import plotly.express as px
import numpy as np
import math

equation = "(sqrt(cos(x))*cos(75x)+sqrt(abs(x))-.7)*(4-x*x)^.2"


def heart_func(x):
    return ((4 - x * x) ** 0.2) * (math.sqrt(math.cos(x)) * math.cos(75 * x) + math.sqrt(abs(x)) - 0.7)


x = np.linspace(-1.570, 1.570, 10000)
y = [heart_func(i) for i in x]


fig = px.line(x=x, y=y)
fig.show()
