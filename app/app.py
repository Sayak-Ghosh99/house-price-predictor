import joblib
import pandas as pd
import os

# Define paths
base_path = os.path.join(os.path.dirname(__file__), "..", "notebooks")
model_path = os.path.join(base_path, "linear_regression_model.pkl")
features_path = os.path.join(base_path, "model_features.pkl")

# Load model and feature list
model = joblib.load(model_path)
model_features = joblib.load(features_path)

# 🎯 Collect raw simplified input from user
print("📊 House Price Prediction Tool")
print("Please enter values for the following features:\n")

raw_input = {
    "Overall Qual": float(input("Overall Quality (1-10): ")),
    "Gr Liv Area": float(input("Above ground living area (sq ft): ")),
    "Garage Cars": float(input("Garage car capacity: ")),
    "Total Bsmt SF": float(input("Total basement area (sq ft): ")),
    "Year Built": int(input("Year Built: ")),
    "Neighborhood": input("Neighborhood (e.g., NAmes, CollgCr, etc.): "),
    "Bldg Type": input("Building Type (e.g., 1Fam, Twnhs, etc.): "),
    "House Style": input("House Style (e.g., 1Story, 2Story, etc.): "),
}

# 🧠 Convert to DataFrame
df_input = pd.DataFrame([raw_input])

# 🪄 One-hot encode the input like training
df_encoded = pd.get_dummies(df_input)

# 🧩 Align with model features
for col in model_features:
    if col not in df_encoded.columns:
        df_encoded[col] = 0

df_encoded = df_encoded[model_features]  # Ensure correct column order

# 🔮 Make prediction
prediction = model.predict(df_encoded)[0]
print(f"\n💰 Estimated House Price: ₹{round(prediction, 2)}")
