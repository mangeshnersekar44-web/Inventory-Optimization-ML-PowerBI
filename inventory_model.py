# ============================================
# 1. Import Libraries
# ============================================

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import warnings
warnings.filterwarnings("ignore")


# ============================================
# 2. Load Dataset
# ============================================

df = pd.read_csv("inventory_data.csv")

print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)

df.head()


# ============================================
# 3. Data Cleaning
# ============================================

# Convert date columns
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True)
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Drop unnecessary columns
df = df.drop([
    'Row ID',
    'Order ID',
    'Customer ID',
    'Customer Name',
    'Postal Code'
], axis=1)

df.head()


# ============================================
# 4. Feature Engineering
# ============================================

# Extract time features
df['year'] = df['Order Date'].dt.year
df['month'] = df['Order Date'].dt.month
df['day'] = df['Order Date'].dt.day
df['dayofweek'] = df['Order Date'].dt.dayofweek

# Shipping delay
df['shipping_days'] = (df['Ship Date'] - df['Order Date']).dt.days


# ============================================
# 5. Exploratory Data Analysis
# ============================================

# Sales Distribution
plt.figure(figsize=(7,4))
sns.histplot(df['Sales'], bins=40, kde=True)
plt.title("Sales Distribution")
plt.show()


# Sales by Category
plt.figure(figsize=(7,4))
sns.barplot(x='Category', y='Sales', data=df)
plt.title("Sales by Category")
plt.show()


# Sales by Region
plt.figure(figsize=(7,4))
sns.barplot(x='Region', y='Sales', data=df)
plt.title("Sales by Region")
plt.show()


# ============================================
# 6. Correlation Heatmap
# ============================================

plt.figure(figsize=(8,5))

cols = ['Sales','year','month','day','dayofweek','shipping_days']

sns.heatmap(df[cols].corr(), annot=True, cmap="coolwarm")

plt.title("Sales Correlation Heatmap")
plt.show()


# ============================================
# 7. Convert Categorical Variables
# ============================================

df_encoded = pd.get_dummies(
    df,
    columns=[
        'Ship Mode',
        'Segment',
        'Country',
        'City',
        'State',
        'Region',
        'Category',
        'Sub-Category'
    ],
    drop_first=True
)


# ============================================
# 8. Define Features & Target
# ============================================

X = df_encoded.drop(
    ['Sales','Order Date','Ship Date','Product ID','Product Name'],
    axis=1
)

y = df_encoded['Sales']


# ============================================
# 9. Train Test Split
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)


# ============================================
# 10. Train Machine Learning Model
# ============================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


# ============================================
# 11. Prediction
# ============================================

predictions = model.predict(X_test)


# ============================================
# 12. Model Evaluation
# ============================================

mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("\nModel Performance")
print("-------------------")
print("MAE :", mae)
print("RMSE:", rmse)
print("R2  :", r2)


# ============================================
# 13. Feature Importance
# ============================================

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

top_features = importance.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(8,5))
top_features.plot(kind='barh')
plt.title("Top Features Affecting Sales")
plt.show()


# ============================================
# 14. Inventory Optimization
# ============================================

# Average product demand
avg_sales = df.groupby('Product Name')['Sales'].mean()

lead_time = 5

reorder_point = avg_sales * lead_time

reorder_df = pd.DataFrame({
    'Product Name': avg_sales.index,
    'Average Sales': avg_sales.values,
    'Reorder Point': reorder_point.values
})

print("\nSample Reorder Points:")
print(reorder_df.head())


# ============================================
# 15. Save Results
# ============================================

reorder_df.to_csv("inventory_reorder_points.csv", index=False)

print("\nProject Completed Successfully!")