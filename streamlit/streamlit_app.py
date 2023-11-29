import streamlit as st
import pandas as pd
import plost
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
st.sidebar.header('Airbnb Price Prediction')

st.sidebar.subheader('Map')
map_price_filter = st.sidebar.selectbox('Prices by', ('<50$', '50-150$', '150-250$', '>250$'))

st.sidebar.subheader('Donut chart parameter')
donut_theta = st.sidebar.selectbox('Select data', ('q2', 'q3'))

st.sidebar.subheader('Line chart parameters')
plot_data = st.sidebar.multiselect('Select data', ['temp_min', 'temp_max'], ['temp_min', 'temp_max'])
plot_height = st.sidebar.slider('Specify plot height', 200, 500, 250)


# Custom HTML for the top navigation bar
top_nav = """
<div class="top-nav">
    Airbnb Data Science Project
    <a href="YOUR_GITHUB_LINK" target="_blank">Go to GitHub</a>
</div>
"""

st.markdown(top_nav, unsafe_allow_html=True)



# Row A
st.markdown('### Airbnb Key Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# Row B
airbnb_df = pd.read_csv("streamlit/data/finaldf.csv")

def categorize_price(price):
    if price < 50:
        return '<50$'
    elif 50 <= price <= 150:
        return '50-150$'
    elif 150 < price <= 250:
        return '150-250$'
    else:
        return '>250$'

airbnb_df['price_category'] = airbnb_df['price'].apply(categorize_price)

filtered_df = airbnb_df[airbnb_df['price_category'] == map_price_filter]



fig = px.histogram(airbnb_df['price'], nbins=30, title="Airbnb Price Distribution",
                   labels={"value": "Price"}, color_discrete_sequence=['#636EFA'])

# Adding more descriptive labels
fig.update_layout(
    xaxis_title="Price",
    yaxis_title="Number of Listings",
    title={
        'text': "Distribution of Airbnb Prices",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="x"
)

# Adding hover data
fig.update_traces(hovertemplate='Price: %{x}<br>Count: %{y}')

# Displaying the plot in Streamlit
st.markdown('### Price Distribution Histogram')
st.plotly_chart(fig, use_container_width=True)


## Your Mapbox Access Token - Replace 'YOUR_MAPBOX_TOKEN' with your actual token
mapbox_token = "pk.eyJ1IjoiYXB1cmJhNjAiLCJhIjoiY2xwaXA2djl3MDFmMzJscXhrdWNuOW9zNiJ9.Bqw-7vFw66_QpWpvjc3s7w"

# Assuming 'airbnb_df' is your DataFrame and it has 'latitude' and 'longitude' columns
# Replace 'airbnb_df' with your actual DataFrame variable name

# Set the Mapbox token in the Plotly Express configuration
# Set the Mapbox token
px.set_mapbox_access_token(mapbox_token)

# Create the map using the filtered DataFrame
fig = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude",
                        zoom=10, center={"lat": 43.7, "lon": -79.4},
                        color_discrete_sequence=["blue"])

# Customizing the layout
fig.update_layout(
    mapbox_style="light",
    title="Airbnb Locations in Toronto by Price Range",
    margin={"r":0,"t":0,"l":0,"b":0}
)

# Displaying the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)


# Assuming 'df' is your DataFrame and 'categorical_columns' are the columns you're interested in
categorical_columns = ['host_response_time', 'instant_bookable']

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

# Create two columns for the layout
c1, c2 = st.columns((7, 3))

# Creating bar charts for each categorical column and displaying them side by side
for i, column in enumerate(categorical_columns):
    plot_df = airbnb_df[column].value_counts().reset_index()
    plot_df.columns = [column, 'count']  # Renaming columns appropriately

    fig = px.bar(plot_df, x=column, y='count',
                 labels={'count': 'Count'},
                 title=f"Distribution of {column}")
    fig.update_layout(xaxis_title=column, yaxis_title="Count")

    if i == 0:
        with c1:
            st.plotly_chart(fig, use_container_width=True)
    else:
        with c2:
            st.plotly_chart(fig, use_container_width=True)
