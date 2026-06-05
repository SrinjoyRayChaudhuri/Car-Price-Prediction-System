import streamlit as st
import pickle
import pandas as pd

# Load model and dataset
model = pickle.load(open('LinearRegressionModel.pkl', 'rb'))
car = pd.read_csv('Cleaned_Car_data.csv')

# Page Configuration
st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="centered"
)

# Title
st.title("🚗 Car Price Prediction")
st.markdown("Predict the resale value of a used car using Machine Learning.")

st.markdown("---")

# Company Selection
companies = sorted(car['company'].unique())

company = st.selectbox(
    "Select Company",
    companies
)

# Model Selection (Filtered by Company)
filtered_models = sorted(
    car[car['company'] == company]['name'].unique()
)

car_model = st.selectbox(
    "Select Car Model",
    filtered_models
)

# Filter dataset according to selected model
selected_car = car[car['name'] == car_model]

# Year Selection (Filtered by Model)
filtered_years = sorted(
    selected_car['year'].unique(),
    reverse=True
)

year = st.selectbox(
    "Select Manufacturing Year",
    filtered_years
)

# Fuel Type Selection (Filtered by Model)
filtered_fuels = sorted(
    selected_car['fuel_type'].unique()
)

fuel_type = st.selectbox(
    "Select Fuel Type",
    filtered_fuels
)

# Kilometers Driven
kms_driven = st.number_input(
    "Kilometers Driven",
    min_value=0,
    max_value=500000,
    value=0,
    step=1000
)

st.markdown("")

# Prediction Button
if st.button("Predict Price"):

    try:
        input_df = pd.DataFrame(
            [[car_model, company, year, kms_driven, fuel_type]],
            columns=[
                'name',
                'company',
                'year',
                'kms_driven',
                'fuel_type'
            ]
        )

        prediction = model.predict(input_df)[0]

        if prediction < 0:
            prediction = 0

        st.success(
            f"Estimated Car Price: ₹ {prediction:,.0f}"
        )

    except Exception as e:
        st.error(f"Prediction Error: {e}")

st.markdown("---")
st.caption("Built with Python, Pandas, Scikit-Learn and Streamlit")

#   & "C:\Users\Srinjoy RayChaudhuri\anaconda3\python.exe" -m streamlit run app.py