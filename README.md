# 🌦 Weather-Trend Forecasting: A Machine Learning Approach

## 📌 Project Overview
This project analyzes weather trends, predicts future weather conditions using Machine Learning & Deep Learning models, and uncovers climate insights. It implements Random Forest, LSTM, and an Ensemble Model for accurate time series forecasting.

### Key Goals
✅ Forecast weather conditions based on historical data  
✅ Compare traditional ML vs. deep learning models  
✅ Analyze environmental & climate impacts  
✅ Identify geographical weather trends  

## 📊 1. Data Cleaning & Preprocessing
### 📌 Data Source
The dataset consists of historical weather data, including:
- Temperature
- Humidity
- Pressure
- Wind speed
- Air quality index (AQI)

### 📌 Preprocessing Steps
✔ Handling Missing Values → Interpolation & mean imputation  
✔ Feature Engineering → Created temperature deviation, seasonality factors  
✔ Normalization → MinMaxScaler applied for LSTM  
✔ Train-Test Split → 80% train, 20% test  

## 🔍 2. Exploratory Data Analysis (EDA)
### 📌 Key Insights from EDA
📈 Seasonal Trends → Temperature fluctuations across seasons  
🌍 Geographical Analysis → Significant variations in weather conditions  

### 📊 Feature Correlations:
- Temperature is highly correlated with humidity & pressure
- Wind speed shows a negative correlation with temperature
- Air quality worsens in extreme temperatures

### 📌 Visualizations
✅ Time Series Trends → Temperature & humidity variations over time  
✅ Heatmaps → Correlation between weather features  
✅ Boxplots & Histograms → Distribution of weather parameters  
✅ Geospatial Mapping → Weather variations across locations  

## 🤖 3. Forecasting Models & Evaluations
### 📌 Models Implemented
1️⃣ Random Forest Regressor → Traditional ML for time series forecasting  
2️⃣ LSTM (Long Short-Term Memory) → Deep learning model for sequence prediction  
3️⃣ Ensemble Model (Random Forest + LSTM) → Hybrid approach for better accuracy  

### 📌 Model Performance Metrics
| Model                    | R² Score | Accuracy (%) |
|--------------------------|----------|--------------|
| Random Forest            | 0.9995   | 85.6%        |
| LSTM (Before Inverse Scaling) | -        | 73.11%       |
| LSTM (After Inverse Scaling) | -        | 95%          |
| Ensemble Model           | 0.9998   | 93.5%        |

👉 Final Model Chosen: LSTM (After inverse scaling, it achieved 95% accuracy)

## 📈 4. Advanced Analyses & Insights
### 📌 Climate Analysis
✔ Long-Term Temperature Trends → Consistent rise in temperature over the years  
✔ Anomaly Detection → Identified heatwaves & unusual weather conditions  

### 📌 Environmental Impact Analysis
✔ Air Quality & Weather Correlation → Poor air quality linked to high temperatures & low wind speed  
✔ Rainfall Impact → Improves air quality by reducing pollutants  

### 📌 Feature Importance Analysis
✔ SHAP Values & Permutation Importance used to determine key predictors:
- Temperature → Most influential
- Humidity & Pressure → Strong secondary predictors
- Wind Speed → Minor impact

### 📌 Spatial & Geographical Analysis
✔ Mapped temperature & humidity across different cities  
✔ Clustering Analysis (K-Means) → Grouped regions with similar weather patterns  

## 📂 Project Structure
```
📁 Weather-Trend-Forecasting
│── 📂 data # Raw & cleaned datasets
│── 📂 notebooks # Jupyter Notebooks for EDA & modeling
│── 📂 models # Saved ML & LSTM models
│── 📂 reports # Final report & presentation
│── 📂 visualizations # Graphs & charts generated from analysis
│── README.md # Project documentation (this file)
│── requirements.txt # Dependencies & libraries used
```

## 🚀 How to Run the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/padala-lahari07/Data-Meteo.git
   cd Weather-Trend-Forecasting
   ```
2. Set up the environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook:
   ```sh
   jupyter notebook
   ```

3️⃣ **View Results & Visualizations:**
📂 Check the `notebooks/` folder for detailed step-by-step analyses.

## 📌 Deliverables
✅ GitHub Repository: [https://github.com/PATHAN-0716/Weather-Trend-Forecasting](https://github.com/padala-lahari07/Data-Meteo) 
🔹 PM Accelerator Mission: Displayed in the report/dashboard

## 📧 Contact & Contributions
👨‍💻 Developed by: Padala Lakshmi Sai Lahari  
📩 Reach out for questions or collaboration!
