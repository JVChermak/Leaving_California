# Import dependencies
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import datetime
import numpy as np

# Read data
df_census = pd.read_csv('Resources/Census.csv')

# Filter data to just get information about California
ca_housing_df = df_census[df_census['State'] == 'California']

# Visually inspect relationship between Median Housing Cost and Year
x = ca_housing_df['Year']
y = ca_housing_df['Median Housing Cost (monthly) ($)']
plt.scatter(x, y)
plt.xlabel('Years')
plt.ylabel('Median Monthly Housing Cost (USD)')
plt.title('California Monthly Median Housing Costs')
plt.show()

# Set independent variable
X = ca_housing_df.Year.values.reshape(-1,1)

# Set dependent variable
y1 = ca_housing_df['Median Housing Cost (monthly) ($)']

# Create model and fit
model = LinearRegression()
model.fit(X,y1)

# Predict using the model
y_pred = model.predict(X)

# Visualize the regression line
plt.scatter(X,y1)
plt.plot(X, y_pred, color='red')
plt.xlabel('Years')
plt.ylabel('Median Monthly Housing Cost (USD)')
plt.title('California Monthly Median Housing Costs')
plt.savefig('img/median_housing1.png')
plt.show()

# Find the equation for the regression line
print(model.coef_)
print(model.intercept_)

# Predict the cost of housing in 2030
m1 = model.coef_
b1 = model.intercept_
print(f'The predicted monthly cost of housing in 2030 is ${m1*2030 + b1} based on 2010-2018 census data.')

# Try a linear regression with only 2013 to 2018 data
recent_ca_housing_df = ca_housing_df[ca_housing_df['Year'] >= 2013]
recent_ca_housing_df

# Set independent variable
X2 = recent_ca_housing_df['Year'].values.reshape(-1,1)

# Set dependent variable
y2 = recent_ca_housing_df['Median Housing Cost (monthly) ($)']

# Create model and fit
model = LinearRegression()
model.fit(X2,y2)

# Predict with model
y_pred2 = model.predict(X2)

# Visualize the regression line
plt.scatter(X2,y2)
plt.plot(X2, y_pred2, color='red')
plt.xlabel('Years')
plt.ylabel('Median Monthly Housing Cost (USD)')
plt.title('California Median Monthly Housing Cost (USD)')
plt.savefig('img/median_housing2.png')
plt.show()

# Find the equation for the regression line
print(model.coef_)
print(model.intercept_)

# Predict Median Housing Cost in 2030
m2 = model.coef_
b2 = model.intercept_
print(f'The predicted monthly cost of housing in 2030 is ${m2*2030 + b2} based on 2013-2018 census data.')

# Create Zillow CA DataFrame
zillow_ca_df = pd.read_csv('Resources/zillow_data.csv')

# Remove RegionID and SizeRank columns
zillow_ca_df.drop(columns=['RegionID', 'SizeRank'], inplace=True)

# Convert to tall DataFrame
zillow_ca_df = pd.melt(zillow_ca_df, id_vars=['RegionName'], var_name='Time', value_name='Typical_Home_Value')

# Convert Time to datetime
zillow_ca_df['Time'] = pd.to_datetime(zillow_ca_df['Time'], format='%Y-%m')

# Visually inspect Zillow data
plt.plot_date(zillow_ca_df.Time, zillow_ca_df.Typical_Home_Value)
plt.xlabel('Time')
plt.ylabel('Typical Home Value (USD)')
plt.title('California Typical Home Value from Zillow')
plt.show()

# Create Months column that represents the number of months since 1994-04
zillow_ca_df['Months'] = range(0,len(zillow_ca_df))

# Set independent variable
X3 = zillow_ca_df['Months'].values.reshape(-1,1)

# Set dependent variable
y3 = zillow_ca_df['Typical_Home_Value']

# Create model and fit
z_model = LinearRegression()
z_model.fit(X3,y3)

# Predict with Zillow model
y_predz = z_model.predict(X3)

# Visualize the regression line
plt.scatter(X3,y3)
plt.plot(X3, y_predz, color='red')
plt.xlabel('Time')
plt.ylabel('Typical Home Value (USD)')
plt.title('California Typical Home Value from Zillow')
plt.xlim(0,286)
plt.ylim(150000,600000)
plt.xticks(np.arange(0, 300, step=50))
plt.yticks(np.arange(0,600000, step=50000))
plt.savefig('img/median_home_value1.png')
plt.show()

# Find the equation for the regression line
print(z_model.coef_)
print(z_model.intercept_)

# Predict home value in 2030 by adding 120 months to 2020-01
m3 = z_model.coef_
b3 = z_model.intercept_
x = 285 + 120
print(f'The predicted median home value in 2030 is ${m3 * x + b3} based on April 1996 to January 2020 Zillow data.')

# Check Census Median Home Value data
X4 = ca_housing_df['Year'].values.reshape(-1,1)
y4 = ca_housing_df['Median Home Value ($)(1000X)']

# Create model and fit
model = LinearRegression()
model.fit(X4,y4)

# Predict with model
y_pred4 = model.predict(X4)

# Visualize the regression line
plt.scatter(X4,y4)
plt.plot(X4, y_pred4, color='red')
plt.xlabel('Years')
plt.ylabel('Median Home Value')
plt.title('California Median Home Value from Census')
plt.savefig('img/median_home_value2.png')
plt.show()

# Find the equation for the regression line
print(model.coef_)
print(model.intercept_)

# Predict Median Housing Cost in 2030
m4 = model.coef_
b4 = model.intercept_
print(f'The predicted median home value in 2030 is ${(m4*2030 + b4) * 1000} based on 2010-2018 census data.')