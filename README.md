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
