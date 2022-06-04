import plotly.graph_objects as go
import numpy as np

fig = go.Figure(data=go.Heatmap(
    z=[[1, None, 30, 50, 1], [20, 1, 60, 80, 1], [30, 60, 1, -10, 20]],
    x=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
    y=['Morning', 'Afternoon', 'Evening'],
))

fig.show()
