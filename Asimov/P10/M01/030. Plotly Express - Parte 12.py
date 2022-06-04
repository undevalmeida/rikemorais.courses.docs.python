import plotly.express as px
df = px.data.gapminder()
fig = px.choropleth(df,
                    locations="iso_alpha",
                    color="lifeExp",
                    hover_name="country",
                    animation_frame="year",
                    range_color=[20, 80])

fig.update_layout(height=800)
fig.show()
