import plotly.graph_objects as go

animais = ['Girafas', 'Macacos', 'Tigres']

fig = go.Figure(
    data=[
        go.Bar(x=animais, y=[3, 120, 6], name='Zoo SP'),
        go.Bar(x=animais, y=[1, 40, 2], name='Zoo RJ')
    ]
)

fig.show()
