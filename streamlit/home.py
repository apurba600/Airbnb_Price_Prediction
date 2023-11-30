import streamlit as st
import pandas as pd
import numpy as np
import plost
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


st.sidebar.subheader('Map')
map_price_filter = st.sidebar.selectbox('Prices by', ('<=50$', '51-150$', '151-250$', '>250$'))


# Row A
st.markdown('### Airbnb Key Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Listings", "19932" , "123")
col2.metric("Average Price/Day", "130$", "-2%")
col3.metric("Occupancy Rate", "83%", "-6%")

# Read data
airbnb_df = pd.read_csv("data/finaldf.csv")
raw_data = pd.read_csv("data/raw_data.csv")


def categorize_price(price):
    if price <= 50:
        return '<=50$'
    elif 51 <= price <= 150:
        return '51-150$'
    elif 150 < price <= 250:
        return '151-250$'
    else:
        return '>250$'



airbnb_df['price_category'] = airbnb_df['price'].apply(categorize_price)

filtered_df = airbnb_df[airbnb_df['price_category'] == map_price_filter]


prices = airbnb_df['price']

# Create the bins for the histogram
bins = np.linspace(prices.min(), prices.max(), 30)

# Create the histogram
fig = go.Figure(data=[go.Histogram(x=prices, xbins=dict(start=prices.min(), end=prices.max(), size=(prices.max()-prices.min())/30), 
                                   marker_color='#636EFA', hoverinfo='x+y')])

# Update the layout for a nicer appearance
fig.update_layout(
    title="Distribution of Airbnb Prices",
    xaxis=dict(title='Price'),
    yaxis=dict(title='Number of Listings'),
    bargap=0.1, 
    hovermode='x',  
    template='plotly_white',  
    height=500,  
)

# Add hover template
fig.update_traces(hovertemplate='Price: %{x}<br>Count: %{y}')

# Display the plot in Streamlit
st.markdown('### Visualization')
st.plotly_chart(fig, use_container_width=True)


#Mapbox Access Token
mapbox_token = "pk.eyJ1IjoiYXB1cmJhNjAiLCJhIjoiY2xwaXA2djl3MDFmMzJscXhrdWNuOW9zNiJ9.Bqw-7vFw66_QpWpvjc3s7w"


# Set the Mapbox token
go.layout.mapbox.AccessToken = mapbox_token

# Generate a list of colors based on 'host_is_superhost' (red for 1, blue for 0)
colors = ['#FF5733' if is_superhost == 1 else '#636EFA' for is_superhost in filtered_df['host_is_superhost']]

# Create the map using the filtered DataFrame
fig = go.Figure(go.Scattermapbox(
    lat=filtered_df['latitude'],
    lon=filtered_df['longitude'],
    mode='markers',
    marker=go.scattermapbox.Marker(
        size=7,
        color=colors,
        opacity=0.7
    ),
    text=['Superhost' if is_superhost == 1 else 'Regular Host' for is_superhost in filtered_df['host_is_superhost']],
    hoverinfo='text'
))

# Customizing the layout
fig.update_layout(
    mapbox_style="dark",  # Assuming dark mode is preferred
    mapbox=dict(
        accesstoken=mapbox_token,
        bearing=0,
        center=go.layout.mapbox.Center(
            lat=43.7,
            lon=-79.4
        ),
        pitch=0,
        zoom=10
    ),
    title="Airbnb Locations in Toronto by Price Range",
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Displaying the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Mapping for 'host_response_time'
response_time_mapping = {
    4: 'within an hour',
    3: 'within few hours',
    2: 'within a day',
    1: 'within few days'
}
# Convert 'host_response_time' to string and map it
airbnb_df['host_response_time'] = airbnb_df['host_response_time'].map(response_time_mapping)

# Convert 'instant_bookable' to 'Yes'/'No'
airbnb_df['instant_bookable'] = airbnb_df['instant_bookable'].replace({True: 'Yes', False: 'No'})

# Create two columns for the layout in Streamlit
c1, c2 = st.columns((7, 3))

# Creating bar charts for each categorical column and displaying them side by side
for i, column in enumerate(['host_response_time', 'instant_bookable']):
    # Prepare data for plotting
    plot_df = airbnb_df[column].value_counts().reset_index()
    plot_df.columns = ['category', 'count']  # Renaming columns appropriately

    # Create a bar chart using plotly.graph_objects
    fig = go.Figure(data=[
        go.Bar(x=plot_df['category'], y=plot_df['count'], marker_color='#636EFA')
    ])

    # Update the layout of the chart
    fig.update_layout(
        title=f"Distribution of {column}",
        xaxis_title=column,
        yaxis_title="Count",
        template='plotly_white'
    )

    # Display the chart in the appropriate column in Streamlit
    if i == 0:
        with c1:
            st.plotly_chart(fig, use_container_width=True)
    else:
        with c2:
            st.plotly_chart(fig, use_container_width=True)




license_counts = airbnb_df['license'].value_counts()


c4, c5 = st.columns((7, 3))
with c5:
    # Create the donut chart
    fig = go.Figure(data=[go.Pie(labels=['No License (0)', 'License (1)'],
                                values=license_counts,
                                hole=.3)])  # The hole parameter creates the donut chart

    # Update the layout of the chart
    fig.update_layout(
        title_text='Distribution of Licenses',
        annotations=[dict(text='License', x=0.5, y=0.5, font_size=20, showarrow=False)],
        showlegend=True
    )

    # Set the color of the donut slices
    fig.update_traces(marker=dict(colors=['#636EFA', '#EF553B'], line=dict(color='#FFFFFF', width=2)))

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)


    # Amenity columns and their respective percentages
    amenity_columns = [
        'Pool', 'Wifi', 'Air conditioning', 'kitchen',
        'Parking', 'Private entrance',
        'Hot tub', 'Heating', 'Washer', 'Dryer'
    ]
    amenity_percentages = [19.98, 92, 93, 82, 80, 10, 92, 86, 90]


with c4:

    # Create a bar chart using plotly.graph_objects
    fig = go.Figure([go.Bar(
        x=amenity_percentages,
        y=amenity_columns,
        orientation='h',  # Horizontal bar chart
        marker_color='#636EFA'
    )])

    # Update the layout of the chart
    fig.update_layout(
        title="Amenities Availability in Airbnb Listings (%)",
        xaxis_title="Percentage",
        yaxis_title="Amenities",
        template='plotly_white'
    )

    # Display the plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)
