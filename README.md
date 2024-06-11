# Project Title: Predictive Models for Resale Prices and Lead Classification
## Overview
### This project aims to develop and deploy two machine learning models:

A regression model for predicting the resale prices of flats in Singapore.
A classification model for evaluating and classifying leads in the copper industry.
The project includes creating user-friendly web applications for each model to assist users in making data-driven decisions.

## Table of Contents
Introduction
Datasets
Machine Learning Models
Web Application
Installation and Setup

## Introduction
### Resale Price Prediction
The objective of the resale price prediction model is to assist potential buyers and sellers in estimating the resale value of flats in Singapore. The model leverages historical data of resale flat transactions and utilizes advanced machine learning techniques to improve prediction accuracy. This includes addressing issues such as data skewness and noise, which can affect manual predictions.

### Lead Classification
In the copper industry, lead management is crucial for business success. The lead classification model aims to evaluate and classify leads based on their likelihood of converting into customers. By analyzing historical sales data, the model identifies patterns and helps prioritize leads, improving the efficiency of the sales process.


## Data Preprocessing: 
Handling missing values, encoding categorical features, and scaling numerical features.
## Feature Engineering: 
Creating new features such as the age of the flat and interaction terms.
## Model Selection: 
Experimenting with different regression algorithms (e.g., Linear Regression, Random Forest, XGBoost) and selecting the best-performing model.
## Model Evaluation: 
Using metrics such as Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared to evaluate model performance.
## Lead Classification Model
The lead classification model uses classification techniques to predict the likelihood of a lead converting into a customer. Key steps include:

## Data Cleaning:
Removing data points with STATUS values other than WON or LOST.
## Feature Selection: 
Identifying the most relevant features for predicting lead conversion.
## Model Selection:
Experimenting with different classification algorithms (e.g., Logistic Regression, Decision Trees, Random Forest) and selecting the best-performing model.
## Model Evaluation: 
Using metrics such as Accuracy, Precision, Recall, and F1-Score to evaluate model performance.
## Web Application
The web application provides a user-friendly interface for interacting with the machine learning models. Key features include:


## Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Flask,Python
Machine Learning: scikit-learn, pandas, numpy
