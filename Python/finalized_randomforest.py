# Initial imports.
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Read data
df_us_data = pd.read_csv('Resources/US_data_combined.csv')
df_us_data

# Drop columns with multiple NaN values
df_us_data.dropna(axis=1, inplace=True)
df_us_data

# List columns for calculations
cols = df_us_data.columns.to_list()
print(cols)

# Create array for binary category: if Median Home Value exceeds 3 times the Median Income, time to leave
leave = []
for i in range(len(df_us_data)):
    if df_us_data['Median Home Value ($)(1000X)'][i] > 3 * df_us_data['Median Income ($)(1000X)'][i]:
        leave.append(1)
    else:
        leave.append(0)
    i += 1     
leave

# Create binary column in df_us_data
df_us_data['Leave'] = leave
df_us_data

# Create States DataFrame with names of states
state_names_df = df_us_data[['Year', 'Region', 'NAME']]
state_names_df.head()

# Remove Region and NAME columns to prepare for ML
clean_us_data_df = df_us_data.drop(columns=['Region', 'NAME'])
clean_us_data_df

# Check datatypes for all columns in preparation of ML
clean_us_data_df.dtypes

# Preprocess the data
# Define the features set
X = clean_us_data_df.copy()
X = X.drop('Leave', axis=1)
X.head()

# Define the target set
y = clean_us_data_df['Leave'].ravel()
y[:5]

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
predictions

# Evaluate the Model
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
importances

# Sort the features by their importance.
important_features = sorted(zip(rf_model.feature_importances_, X.columns), reverse=True)
print("Features in order of importance")
print(important_features)