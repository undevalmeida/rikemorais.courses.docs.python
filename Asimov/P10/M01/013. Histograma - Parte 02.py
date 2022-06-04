import plotly.graph_objects as go
import numpy as np

# Distribuição com x
x = np.random.randn(500)

# Distribuição com z
z = np.random.randn(500) + 1

# Organização dos Dados
fig = go.Figure()
fig.add_trace(go.Histogram(x=x))
fig.add_trace(go.Histogram(x=z))
fig.update_layout(barmode='overlay')
fig.update_traces(opacity=0.75)

fig.show()
