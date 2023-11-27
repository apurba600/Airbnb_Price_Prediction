Airbnb Price Prediction And Reviews Sentiment Analysis

![DALL·E 2023-10-17 13 43 26 - Illustration of a digital interface showcasing an Airbnb listing in Toronto, displaying high ratings, photos of a chic urban loft, and a 'Book Now' bu](https://github.com/apurba600/Airbnb_Price_Prediction/assets/90535174/318a8331-50ac-43a0-8d52-32ae4eb86db0)




# Introduction

One main challenge faced by Airbnb hosts, especially newcomers to the platform, is the
difficulty in optimizing their listings. This includes determining the best area to invest in a
property for Airbnb hosting and gaining insights into pricing, occupancy rates, and other relevant
factors. These challenges can lead to suboptimal decision-making and potentially lower profits
for hosts.

# Project Overview

The project's goal is to develop a machine-learning model that provides price prediction, 
relationship of reviews with profitability and data-driven insights to Airbnb hosts. 

This model would consider various factors such as location, property type,
seasonal trends, and local demand to help hosts make informed decisions about their listings.
By leveraging this model, hosts can improve their investment decisions, enhance the quality of
their listings, and ultimately maximize their profitability. This project primarily benefits new and
experienced Airbnb hosts who are seeking a data-driven approach to optimize their properties
and increase their overall success in the Airbnb marketplace.

Machine learning offers various solutions to the challenges. Through the analysis of extensive
datasets, ML models allow hosts to make data-driven decisions by identifying key variables for
optimization, including location, property type, pricing strategies, and amenities. Utilizing
supervised techniques like linear regression, neural networks, and XGBoost, hosts can
construct predictive models to forecast occupancy rates and rental income, facilitating proactive
planning. 

By optimizing Airbnb listings through machine learning, it is anticipated to boost hosts
profitability, potentially amounting to thousands of dollars in additional earnings. Hosts can also
save dozens of hours each month, potentially adding up to thousands of hours in time saved
collectively, which they can spend with friends and family.Additionally, the project's focus on
improving the guest experience may lead to higher guest satisfaction and more positive reviews,
further benefiting hosts.

# Dependencies
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


# Dataset

We got the dataset from inside Airbnb and open data.

The dataset consists of 42,811 entries and 75 columns. Here are some key columns from the dataset:

- id: Unique identifier for each listing.
- listing_url: URL of the listing.
- name: Name of the listing.
- description: Description of the listing.
- neighborhood_overview: Overview of the neighborhood.
- host_id: Identifier for the host.
- host_name: Name of the host.
- host_since: The date the host joined Airbnb.
- host_response_time: Time taken by the host to respond to inquiries.
- review_scores_location: Review score based on location.
- instant_bookable: Whether the property can be booked instantly.
- reviews_per_month: Average number of reviews per month.
- bathroom_num: Number of bathrooms in the listing.

Some of the preliminary analyses we hypothesize will give a high correlation to Price are:

- bathroom
- location
- bedroom
- amenities
- reviews

# Exploratory Data Analysis (EDA)

We will start by importing the files and analyzing the data to understand the distribution and relationship among features. We will also remove duplicate and null values, describe and get info on the data, convert target values to proper data 

 # Airbnb Price Prediction Project Flowchart:

- Project Overview

- Introduction to the project's aim and significance.
Definition of the problem statement.
Data Collection

- Description of data sources.
Methods used for gathering Airbnb listings and review data.
Data Preprocessing

- Cleaning: Handling missing values and outliers.
- Feature Engineering: Extracting new insights, such as host tenure and amenities count.
- Encoding: Converting categorical data into a machine-readable format.
- Exploratory Data Analysis (EDA)

- Visualization: Creating graphs to understand data distributions and relationships.
Correlation Analysis: Identifying relationships between features and price.
Assumption Testing: Checking for linearity, normality, and homoscedasticity.
Model Building

# Feature Engineering

Price Column: Did a log transformation to get a better normal distribution

One hot encoding and Ordinal encoding on some of the categorical features

# Baseline Modeling and Evaluation:

Starting with Basic model

Built a simple linear regression model using all data features to predict Airbnb prices.
Evaluating Our First Model:

Measured how well our model predicts prices with R-squared (the higher, the better).
Used Mean Squared Error (MSE) to understand the average error in our price predictions.

# Advanced Modelling

After creating a baseline with simple linear regression, we explored more complex modeling techniques to capture the complex relationships in the data:

Random Forest: An ensemble method that aggregates the predictions of multiple decision trees to produce a more robust and accurate model. It's good at handling non-linear relationships.

XGBoost: A gradient-boosting framework that uses bootstrapping and boosting.

Neural Networks: Neural networks can capture complex patterns through their multiple layers and non-linear activation functions.

Ridge Regression: This linear regression variant introduces L2 regularization to penalize large coefficients, reducing model complexity and preventing overfitting.

Lasso Regression: Similar to Ridge, Lasso adds L1 regularization, which can reduce some coefficients to zero, effectively performing feature selection.

# Model Optimization

k-Fold Cross-Validation: This method provided a way to estimate the performance of our models. It involves partitioning the data into k subsets and training the model k times, each time using a different subset as the test set and the remaining as the training set.

GridSearchCV: We utilized GridSearchCV for searching over specified parameter values for our estimators. By training and evaluating the model for every combination of parameters, we were able to identify the most effective parameters.

# Model Evaluation

R-squared: To quantify the amount of variance in the listing prices that our models could explain.

Mean Squared Error (MSE): To measure the average squared difference between the estimated values and the actual value.

Mean Absolute Error (MAE): To provide a measure of prediction accuracy, how close the predictions are to the actual outcomes on average.

# Results

<img width="483" alt="Screenshot 2023-11-26 at 7 04 38 PM" src="https://github.com/apurba600/Airbnb_Price_Prediction/assets/90535174/fcae120d-8943-4979-85dc-577546a73556">

 
# Conclusion
In Conclusion, while the XG Boost model showed the highest R2 score on the test set among the various models evaluated, indicating strong predictive performance, its significant overfit (with a train R2 of 0.72) suggests it may not generalize fit as well to unseen data. The Random Forest model,on the other hand with train (R2 of 0.62) and test (R2 of 0.60) scores, showed the most reliable for predicting Airbnb prices, showing good generalization and a substantial improvement over the baseline Linear Regression model ( R2 of 0.40). The key predictors identified by the Random Forest model — room type, number of accommodations, license, and latitude — offer actionable insights for hosts looking to optimize their pricing strategies on the platform.

# Licensing, Acknowledgements
http://insideairbnb.com/get-the-data/ - The data was taken from this link
