import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow

with open('full_pipeline.pkl', 'rb') as file_1:
  model_pipeline = joblib.load(file_1)

from tensorflow.keras.models import load_model
model_ann = load_model('churn_model.h5')


st.title("Customer Churn Prediction")

membership_category = st.selectbox('Membership Category',('No Membership', 'Basic Membership', 'Silver Membership', 'Premium Membership', 'Gold Membership', 'Platinum Membership'), index=1)


avg_transaction_value = st.number_input('Average Transaction Value :', min_value =  800.460000, max_value = 99914.050000, value = 800.460000)


points_in_wallet = st.number_input('Points In Wallet :', min_value =  0.000000, max_value = 2069.069761, value = 0.000000)


feedback = st.selectbox('Feedback',('Poor Website', 'Poor Customer Service', 'Too many ads', 'Poor Product Quality', 'No reason specified', 'Products always in Stock', 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website'), index=1)

df_inf = pd.DataFrame({
    'membership_category':[membership_category],
    'avg_transaction_value':[avg_transaction_value],
    'points_in_wallet':[points_in_wallet],
    'feedback':[feedback]
})

if st.button('Predict'):
    data_inf_transform = model_pipeline.transform(df_inf)
    y_pred_inf = model_ann.predict(data_inf_transform)
    y_pred_inf = np.where(y_pred_inf >= 0.5, 1, 0)
    churn_status = np.where(y_pred_inf == 0, "No", "Yes")
    
    if churn_status == "No":
        st.success(f"The customer is predicted to not churn.")
    else:
        st.error(f"The customer is predicted to churn.")
