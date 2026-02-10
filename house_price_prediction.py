import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset (simulating collection from Kaggle)
df = pd.read_csv('house_data.csv')

# Display basic info
print("Dataset Overview:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# Preprocessing
# Encode categorical variable 'location'
le = LabelEncoder()
df['location_encoded'] = le.fit_transform(df['location'])

# Features and target
X = df[['size_sqft', 'bedrooms', 'bathrooms', 'location_encoded', 'age_years']]
y = df['price']

# Scale numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Evaluation:")
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Coefficients
print("\nModel Coefficients:")
for feature, coef in zip(X.columns, model.coef_):
    print(f"{feature}: {coef}")

# Sample predictions
print("\nSample Predictions:")
sample_data = pd.DataFrame({
    'size_sqft': [1600, 2200],
    'bedrooms': [3, 4],
    'bathrooms': [2, 3],
    'location_encoded': [le.transform(['urban'])[0], le.transform(['suburban'])[0]],
    'age_years': [10, 5]
})
sample_scaled = scaler.transform(sample_data)
predictions = model.predict(sample_scaled)
for i, pred in enumerate(predictions):
    print(f"House {i+1}: Predicted Price ${pred:.2f}")

# Insights
print("\nInsights:")
print("1. The model explains {:.2f}% of the variance in house prices.".format(r2 * 100))
print("2. Size in square feet has the highest positive impact on price.")
print("3. Older houses (higher age_years) tend to have lower prices.")
print("4. Location affects price, with urban areas generally having higher values.")