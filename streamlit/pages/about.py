import streamlit as st

# Set page config
st.set_page_config(page_title='Airbnb Price Prediction Project', layout='wide', initial_sidebar_state='expanded')

with open('streamlit/style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.image('streamlit/pages/airbnb.jpg', width=700)    

# Main Title
st.title('Airbnb Price Prediction Project')

# Introduction
st.markdown('''
### Introduction
One main challenge faced by Airbnb hosts, especially newcomers to the platform, is the difficulty in optimizing their listings. This includes determining the best area to invest in a property for Airbnb hosting and gaining insights into pricing, occupancy rates, and other relevant factors. These challenges can lead to suboptimal decision-making and potentially lower profits for hosts.
''')

# Project Overview
st.markdown('''
### Project Overview
The project's goal is to develop a machine-learning model that provides price prediction, relationship of reviews with profitability and data-driven insights to Airbnb hosts.
''')


# Dependencies
st.markdown('''
### Dependencies
Python Libraries (refer to requirements.txt):
- pandas
- numpy
- matplotlib
- seaborn
- plotly
- statsmodels
- scipy
- scikit-learn
- tensorflow
- Xgboost
- re
''')

# Exploratory Data Analysis (EDA)
st.markdown('''
### Exploratory Data Analysis (EDA)
We will start by importing the files and analyzing the data to understand the distribution and relationship among features. We will also remove duplicate and null values, describe and get info on the data, convert target values to proper data types.
''')

# Airbnb Price Prediction Project Flowchart
st.markdown('''
### Airbnb Price Prediction Project Flowchart:
**Project Overview**  
- Introduction to the project's aim and significance.  
- Definition of the problem statement.  

**Data Collection**  
- Description of data sources.  
- Methods used for gathering Airbnb listings and review data.  

**Data Preprocessing**  
- Cleaning: Handling missing values and outliers.  
- Feature Engineering: Extracting new insights, such as host tenure and amenities count.  
- Encoding: Converting categorical data into a machine-readable format.  

**Exploratory Data Analysis (EDA)**  
- Visualization: Creating graphs to understand data distributions and relationships.  
- Correlation Analysis: Identifying relationships between features and price.  
- Assumption Testing: Checking for linearity, normality, and homoscedasticity.  
''')

# Model Building
st.markdown('''
### Model Building
**Feature Engineering**  
- Price Column: Did a log transformation to get a better normal distribution.  
- One hot encoding and Ordinal encoding on some of the categorical features.  

**Baseline Modeling and Evaluation**  
- Starting with a Basic model.  
- Built a simple linear regression model using all data features to predict Airbnb prices.  

**Evaluating Our First Model**  
- Measured how well our model predicts prices with R-squared (the higher, the better).  
- Used Mean Squared Error (MSE) to understand the average error in our price predictions.  
''')

# Advanced Modelling
st.markdown('''
### Advanced Modelling
After creating a baseline with simple linear regression, we explored more complex modeling techniques to capture the complex relationships in the data:  
- **Random Forest**: An ensemble method that aggregates the predictions of multiple decision trees.  
- **XGBoost**: A gradient-boosting framework that uses bootstrapping and boosting.  
- **Neural Networks**: Can capture complex patterns through multiple layers and non-linear activation functions.  
- **Ridge Regression**: Introduces L2 regularization to penalize large coefficients.  
- **Lasso Regression**: Similar to Ridge, Lasso adds L1 regularization, which can reduce some coefficients to zero.  
''')

# Model Optimization
st.markdown('''
### Model Optimization
- **k-Fold Cross-Validation**: Provides a way to estimate the performance of our models.  
- **GridSearchCV**: Utilized for searching over specified parameter values for our estimators.  
''')

# Model Evaluation
st.markdown('''
### Model Evaluation
- **R-squared**: Quantifies the amount of variance in the listing prices that our models could explain.  
- **Mean Squared Error (MSE)**: Measures the average squared difference between the estimated values and the actual value.  
- **Mean Absolute Error (MAE)**: Provides a measure of prediction accuracy.  
''')

st.image('/Users/apurba60/Desktop/streamlit/pages/result.jpg', width=700) 

st.markdown('''
### Conclusion
In Conclusion, while the XG Boost model showed the highest R2 score on the test set among the various models evaluated, indicating strong predictive performance, 
its significant overfit (with a train R2 of 0.72) suggests it may not generalize fit as well to unseen data. The Random Forest model,on the other hand with train (R2 of 0.62) and test (R2 of 0.60) scores, 
showed the most reliable for predicting Airbnb prices, showing good generalization and a substantial improvement over the baseline Linear Regression model ( R2 of 0.40). The key predictors identified by the Random Forest model — room type, number of accommodations, license, and latitude — offer actionable insights for hosts looking to optimize their pricing strategies on the platform. 
''')

st.markdown('''
### Acknowledgement
http://insideairbnb.com/get-the-data/ - The data was taken from this link
''')

