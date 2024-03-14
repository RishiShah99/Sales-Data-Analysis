# Author: Rishi Shah
# Date: 2024-03-13

# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Print the first 5 rows of the dataframe
print(df.head())

# Print the last 5 rows of the dataframe
print(df.tail())

# Print the shape of the dataframe
print(df.shape)

# # Data Cleaning: Handling missing values, outliers, and discrepancies in the data
# Check for missing values
print(df.isnull().sum())
# All of the zeroes are in the second addressline, state, and territories, so we can keep them as is.

# Check for outliers
print(df.describe())

# Remove outliers
df = df[df['SALES'] < 10000]

# Check for outliers after removing them
print(df.describe())

# Data Analysis: Exploring the data and identifying patterns
# Plot the distribution of sales
plt.hist(df['SALES'], bins=20)
plt.xlabel('Sales')
plt.ylabel('Frequency')
plt.title('Distribution of Sales')
plt.show()

# Plot the distribution of sales by product line
df['PRODUCTLINE'].value_counts().plot(kind='bar')
plt.xlabel('Product Line')
plt.ylabel('Frequency')
plt.title('Distribution of Sales by Product Line')
plt.show()

# Plot the distribution of sales by country
df['COUNTRY'].value_counts().plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.title('Distribution of Sales by Country')
plt.show()

# Plot the total sales by product line
df.groupby('PRODUCTLINE')['SALES'].sum().plot(kind='bar')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product Line')
plt.show()

# # Plot the total sales by country
df.groupby('COUNTRY')['SALES'].sum().plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Total Sales')
plt.title('Total Sales by Country')
plt.show()

# Data Interpretation: Drawing conclusions and making recommendations
# Conclusion 1: The highest sales are from the Classic Cars product line
# Recommendation 1: Focus on promoting and expanding the Classic Cars product line to increase sales

# Conclusion 2: The highest sales are from the USA
# Recommendation 2: Consider expanding operations and marketing efforts in the USA to capitalize on the high sales

# Conclusion 3: The lowest sales are from the Trucks and Buses product line
# Recommendation 3: Evaluate the market demand and potential for growth in the Trucks and Buses product line
