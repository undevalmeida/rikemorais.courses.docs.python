import plotly.graph_objects as go
import numpy as np

N = 70

x = 70 * np.random.rand(N)
y = 55 * np.random.rand(N)
z = 40 * np.random.rand(N)

fig = go.Figure(data=go.Mesh3d(
    x=x,
    y=y,
    z=z,
    opacity=0.5
))

fig.show()
