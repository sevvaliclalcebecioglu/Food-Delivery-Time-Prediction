import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("data/best_model.pkl")
columns = joblib.load("data/columns.pkl")

st.title("🍔 Food Delivery Time Prediction")

st.write("Enter delivery details to predict delivery time (minutes)")

# User inputs
distance = st.number_input("Distance (km)", 0.0, 50.0, 5.0)
prep_time = st.number_input("Preparation Time (min)", 0, 120, 15)
experience = st.number_input("Courier Experience (years)", 0, 20, 2)

weather = st.selectbox("Weather", ["Clear", "Rainy", "Foggy", "Windy"])
traffic = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
time_of_day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
vehicle = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])

# Create input DataFrame
input_data = pd.DataFrame([{
    "Distance_km": distance,
    "Preparation_Time_min": prep_time,
    "Courier_Experience_yrs": experience,
    "Weather": weather,
    "Traffic_Level": traffic,
    "Time_of_Day": time_of_day,
    "Vehicle_Type": vehicle
}])

# One-hot encoding
input_data = pd.get_dummies(input_data)

# Align columns
input_data = input_data.reindex(columns=columns, fill_value=0)

if st.button("Predict Delivery Time"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated Delivery Time: {prediction:.2f} minutes")
