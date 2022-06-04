import plotly

import plotly.graph_objs as go
fig = go.Figure(
    data=[go.Bar(x=[1, 2, 3], y=[2, 1, 3])],
    layout=go.Layout(
        title=go.layout.Title(text='Bar Chart')
    )
)

fig.show()
