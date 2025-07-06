import pandas as pd
import numpy as np
import joblib
import tensorflow as tf
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import MinMaxScaler

# Load dataset
df = pd.read_csv("data/cleaned_data.csv")
X = df.drop(columns=["target"])
y = df["target"]

# Load trained models
rf_model = joblib.load("models/random_forest_model.pkl")
lstm_model = tf.keras.models.load_model("models/lstm_model.h5")

# Normalize data
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Evaluate Random Forest
rf_preds = rf_model.predict(X)
rf_mse = mean_squared_error(y, rf_preds)
rf_r2 = r2_score(y, rf_preds)

# Evaluate LSTM
lstm_preds = lstm_model.predict(X_scaled)
lstm_mse = mean_squared_error(y, lstm_preds)
lstm_r2 = r2_score(y, lstm_preds)

# Display Results
print("Random Forest -> MSE:", rf_mse, "R² Score:", rf_r2)
print("LSTM Model -> MSE:", lstm_mse, "R² Score:", lstm_r2)
