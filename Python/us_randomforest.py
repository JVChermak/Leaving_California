# Import dependencies
import pandas as pd
from path import Path
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Loading data
file_path = Path('Resources/US_data_combined.csv')
df_us_data = pd.read_csv(file_path)

# Drop columns with multiple NaN values
df_us_data.dropna(axis=1, inplace=True)

# Create array for the number of medium incomes needed for monthly housing cost
cost_to_income = []
for i in range(len(df_us_data)):
    cost_to_income.append(df_us_data['Median Housing Cost (monthly) ($)'][i] / (df_us_data['Median Income ($)(1000X)'][i] * 1000 / 12))
    i += 1

# Create "Cost_to_income_ratio" column
df_us_data['Cost_to_income_ratio'] = cost_to_income

# Create array for binary category
leave = []
for i in range(len(df_us_data)):
    if df_us_data['Cost_to_income_ratio'][i] > 0.28:
        leave.append(1)
    else:
        leave.append(0)
    i += 1

# Create binary column in df_us_data
df_us_data['Leave'] = leave

# Create States DataFrame with names of states
state_names_df = df_us_data[['Year', 'Region', 'NAME']]

# Remove Region, NAME and Cost_to_income_ratio columns to prepare for ML
clean_us_data_df = df_us_data.drop(columns=['Region', 'NAME', 'Cost_to_income_ratio'])

# Define the features set
X = clean_us_data_df.copy()
X = X.drop('Leave', axis=1)

# Define the target set
y = clean_us_data_df['Leave'].ravel()

# Split into Train and Test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=78)

# Create instance of StandardScaler
scaler = StandardScaler()
# Fit StandardScaler with training data
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)

# Create a Random Forest Classifier
rf_model = RandomForestClassifier(n_estimators=128, random_state=78)

# Fit the model
rf_model = rf_model.fit(X_train_scaled, y_train)

# Make predictions using test data
predictions = rf_model.predict(X_test_scaled)

# Calculating the confusion matrix.
cm = confusion_matrix(y_test, predictions)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])
# Calculating the accuracy score
acc_score = accuracy_score(y_test, predictions)

# Displaying results
print("Confusion Matrix")
print(cm_df)
print(f"Accuracy Score: {acc_score}")
print("Classification Report")
print(classification_report(y_test, predictions))

# Calculate feature importance in the Random Forest model.
importances = rf_model.feature_importances_

# Sort the features by their importance.
sorted(zip(rf_model.feature_importances_, X.columns), reverse=True)