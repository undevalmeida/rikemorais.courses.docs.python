import plotly.graph_objects as go

labels = ['Oxigene', 'Hidrogene', 'Carbono', 'Nitrogen']
values = [4500, 2500, 1053, 500]

fig = go.Figure(data=go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0]))

fig.update_traces(hoverinfo="label+percent",
                  textinfo="value+percent",
                  textfont_size=12,
                  )
fig.show()
