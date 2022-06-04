import plotly.graph_objects as go

# Lista de Cores
colors = ["lightslategray"] * 5
colors[1] = "blue"

fig = go.Figure(data=[go.Bar(
    x=['Item A', 'Item B', 'Item C',
       'Item D', 'Item E'],
    y=[20, 14, 23, 25, 22],
    marker_color=colors
)])

fig.show()
