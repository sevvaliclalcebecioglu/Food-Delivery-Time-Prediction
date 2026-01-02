# 🍔 Food Delivery Time Prediction

This project focuses on predicting food delivery times using Machine Learning techniques.  
The goal is to estimate the delivery duration based on distance, traffic, weather, courier experience, and other operational factors.

You can **test the working demo online** here:  
👉 https://huggingface.co/spaces/sevvaliclal/FoodDeliveryTimePrediction

---

## 📌 Project Overview

Food delivery platforms need accurate delivery time estimates to improve customer trust and operational efficiency.  
In this project, multiple regression models were trained and compared to predict the delivery time in minutes.

---

## 📊 Dataset Description

The dataset contains 1000 records with the following features:

- **Order_ID**: Unique identifier for each order  
- **Distance_km**: Distance between restaurant and delivery location  
- **Weather**: Weather conditions (Clear, Rainy, Foggy, etc.)  
- **Traffic_Level**: Traffic density (Low, Medium, High)  
- **Time_of_Day**: Morning, Afternoon, Evening, Night  
- **Vehicle_Type**: Bike, Scooter, or Car  
- **Preparation_Time_min**: Food preparation time  
- **Courier_Experience_yrs**: Courier experience in years  
- **Delivery_Time_min**: Target variable (delivery time in minutes)

---

## ⚙️ Machine Learning Pipeline

1. Data loading  
2. Data preprocessing (One-Hot Encoding)  
3. Train-test split  
4. Model training  
5. Model evaluation  
6. Best model selection  
7. Model saving for deployment

---

## 🤖 Models Used

- **Linear Regression** (Baseline model)  
- **Random Forest Regressor**  
- **Gradient Boosting Regressor**

---

## 📈 Model Performance

| Model               | R² Score | RMSE |
|--------------------|----------|------|
| **Linear Regression**  | **0.826** | **8.82** |
| Gradient Boosting  | 0.786    | 9.79 |
| Random Forest      | 0.767    | 10.21 |

✅ **Linear Regression achieved the best performance and was selected as the final model.**

---

## 💾 Saved Artifacts

| File | Purpose |
|------|---------|
| `best_model.pkl` | Trained Machine Learning model |
| `columns.pkl` | One-Hot encoded feature columns (used at inference time) |

These files are used for deployment and real-time prediction.

