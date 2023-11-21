import csv

filename = 'earthquake.csv'
mags,titles,lons,lats=[],[],[],[]


with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    row = next(csvreader)
    for row in csvreader:
        mag=row[4]
        title=row[0]
        lon=row[2]
        lat=row[1]
        mags.append(mag)
        titles.append(title)
        lons.append(lon)
        lats.append(lat)


import pandas as pd   
data=pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()
#绘制散点图
import plotly.express as px

import plotly.graph_objects as go

fig = go.Figure()

# Add scatter plot
fig.add_scattergeo(
    lat=lats,
    lon=lons,
    text=titles,
    mode='markers',
    marker=dict(
        size=1,
        sizemode='diameter',
        sizeref=0.5,
        #color=mags,
        colorscale='Viridis',
        reversescale=True,
        colorbar=dict(title='Magnitude'),
    ),
)

# Add world map layer
fig.update_geos(
    visible=True,
    resolution=110,
    showcountries=True,
    countrycolor='gray',
    showland=True,
    landcolor='lightgray',
    showocean=True,
    oceancolor='lightblue',
    showlakes=True,
    lakecolor='lightblue',
    showrivers=True,
    rivercolor='lightblue',
)

# Set layout
fig.update_layout(
    title="Global Earthquake Scatter Plot",
    width=800,
    height=800,
)

# Save the plot as HTML file and display it
fig.write_html('global_earthquake.html')
fig.show()

