import pandas as pd
import numpy as np

from lightgbm import LGBMRegressor
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv(
    r"C:\Users\HP\Desktop\IMS_ML\data\retail_store_inventory.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# Filter one SKU
sku = "P0016"

product_df = (
    df[df["Product ID"] == sku]
    .copy()
)

# Aggregate stores into daily sales
daily = (
    product_df.groupby("Date")
    .agg({
        "Units Sold": "sum",
        "Weather Condition": "first",
        "Holiday/Promotion": "first",
        "Seasonality": "first",
        "Competitor Pricing": "mean"
    })
    .reset_index()
)

# Create lag features
daily["lag_1"] = daily["Units Sold"].shift(1)
daily["lag_7"] = daily["Units Sold"].shift(7)
daily["lag_30"] = daily["Units Sold"].shift(30)

# Rolling averages
daily["rolling_7"] = (
    daily["Units Sold"]
    .shift(1)
    .rolling(7)
    .mean()
)

daily["rolling_30"] = (
    daily["Units Sold"]
    .shift(1)
    .rolling(30)
    .mean()
)

# Date features
daily["dayofweek"] = daily["Date"].dt.dayofweek
daily["month"] = daily["Date"].dt.month

# Encode categorical columns
for col in [
    "Weather Condition",
    "Holiday/Promotion",
    "Seasonality"
]:
    encoder = LabelEncoder()
    daily[col] = encoder.fit_transform(
        daily[col].astype(str)
    )

# Remove NaNs from lag creation
daily = daily.dropna()

# Features
X = daily[
    [
        "lag_1",
        "lag_7",
        "lag_30",
        "rolling_7",
        "rolling_30",
        "dayofweek",
        "month",
        "Weather Condition",
        "Holiday/Promotion",
        "Seasonality",
        "Competitor Pricing"
    ]
]

y = daily["Units Sold"]

# Train/Test split
split_index = int(len(X) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

# Train model
model = LGBMRegressor(
    n_estimators=200,
    learning_rate=0.05,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# MAPE
mape = (
    mean_absolute_percentage_error(
        y_test,
        predictions
    )
    * 100
)

print("\nSKU:", sku)
print("Train size:", len(X_train))
print("Test size:", len(X_test))
print("LightGBM MAPE:", round(mape, 2), "%")