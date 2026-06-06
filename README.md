# 🚗 Car Price Prediction

A Machine Learning web application that predicts the resale value of used cars based on vehicle details such as company, model, manufacturing year, fuel type, and kilometers driven.


🔗 Live App:
https://srinjoyraychaudhuri-car-price-prediction-system-app-aari3n.streamlit.app/

## Features

* Data cleaning and preprocessing
* One-Hot Encoding for categorical features
* Linear Regression model
* Interactive Streamlit interface
* Dynamic filtering of car models based on selected company

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Seaborn

## Project Structure

```text
CAR_PREDICTION/
├── app.py
├── car_price_prediction.ipynb
├── cars.csv
├── Cleaned_Car_data.csv
├── LinearRegressionModel.pkl
├── requirements.txt
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Model

* Algorithm: Linear Regression
* Evaluation Metric: R² Score

## Author

Srinjoy Ray Chaudhuri
