from numpy import roll
from plotly.subplots import make_subplots
import plotly.graph_objs as go

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Bar(y=[1, 4, 5], x=[6, 5, 2], marker_color="green"), row=1, col=1)
fig.add_trace(go.Scatter(y=[8, 2, 4, 5], x=[6, 5, 2, 7], mode="markers"), row=1, col=2)

fig.update_layout(title_text="Scatter Plot", title_font_size=30)

fig.show()
