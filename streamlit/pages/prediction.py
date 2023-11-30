import streamlit as st
import pandas as pd
import sklearn
from sklearn.externals import joblib
import plotly.graph_objects as go

# Set page config
st.set_page_config(page_title='Airbnb Price Prediction Project', layout='wide', initial_sidebar_state='expanded')

with open('streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

df = pd.read_csv("streamlit/data/modelling_section.csv")

# Load the models
model1 = joblib.load('streamlit/model/linear_regression_model.pkl')
model2 = joblib.load('streamlit/model/Randomforest.pkl')
model3 = joblib.load('streamlit/model/XGboost_model.pkl')

# Mapping for model selection
model_mapping = {
    "Linear Regression Model": model1,
    "Random Forest Model": model2,
    "XGBoost Model": model3
}

# Sidebar for model selection
st.sidebar.header("Model Selection")
selected_model = st.sidebar.selectbox("Choose the model for prediction", list(model_mapping.keys()))

# Get the active model based on selection
active_model = model_mapping[selected_model]

# Define a function to make predictions
def predict_price(model, features):
    prediction = model.predict([features])
    return prediction[0]

# Streamlit app for price prediction
st.title('Airbnb Price Prediction')

# Input fields for the features
accommodates = st.number_input('Accommodates (Number of Guests)', min_value=0)
license = st.selectbox('License (Yes or No)', ['Yes', 'No'])
bedrooms = st.number_input('Bedrooms', min_value=0)
bathroom_num = st.number_input('Bathrooms', min_value=0)
amenities = st.number_input('Amenities', min_value=0, max_value=100)

# Convert 'license' from Yes/No to 1/0
license_binary = 1 if license == 'Yes' else 0

default_values = [0] * (active_model.n_features_in_ - 5)  
input_features = [accommodates, license_binary, bedrooms, bathroom_num, amenities] + default_values


# Function to calculate feature contributions for linear regression
def calculate_contributions(lr_model, features):
    contributions = lr_model.named_steps['linear_regression'].coef_ * features
    return contributions

# Button to make prediction
if st.button('Predict Price'):
    price = predict_price(active_model, input_features)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(f"<h1 style='text-align: center; color: blue;'>💲{price:.2f}</h1>", unsafe_allow_html=True)


 






    
