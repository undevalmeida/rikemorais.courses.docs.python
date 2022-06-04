import plotly.graph_objects as go

fig = go.Figure(
    data=[
        go.Bar(x=[1, 2, 3], y=[1, 3, 2]),
        go.Scatter(y=[8, 3, 2], mode="lines")
    ]
)

fig.update_layout(title_text="Bar and Scatter Plot",
                  title_font_size=30,
                  height=700)
fig.show()
