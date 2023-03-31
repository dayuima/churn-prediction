import streamlit as st
import pandas as pd
import numpy as np
import joblib
import tensorflow as tf


with open('full_pipeline.pkl', 'rb') as file_1:
  model_pipeline = joblib.load(file_1)

from tensorflow.keras.models import load_model
model_ann = load_model('churn_model.h5')


st.title("Customer Churn Prediction")

membership_category = st.selectbox('Membership Category',('No Membership', 'Basic Membership', 'Silver Membership', 'Premium Membership', 'Gold Membership', 'Platinum Membership'), index=1)
st.write(membership_category)

avg_transaction_value = st.number_input('Average Transaction Value :', min_value =  800.460000, max_value = 99914.050000, value = 800.460000)
st.write(avg_transaction_value)

points_in_wallet = st.number_input('Points In Wallet :', min_value =  0.000000, max_value = 2069.069761, value = 0.000000)
st.write(points_in_wallet)

feedback = st.selectbox('Feedback',('Poor Website', 'Poor Customer Service', 'Too many ads', 'Poor Product Quality', 'No reason specified', 'Products always in Stock', 'Reasonable Price', 'Quality Customer Care', 'User Friendly Website'), index=1)
st.write(feedback)


df_inf = pd.DataFrame({
    'membership_category':[membership_category],
    'avg_transaction_value':[avg_transaction_value],
    'points_in_wallet':[points_in_wallet],
    'feedback':[feedback],
})

model_ann1 = model_ann.predict(df_inf[['pregnancies','glucose','bloodpressure','skinthickness','insulin','bmi','diabetespedigreefunction','age']])

if st.button('Predict'): 
    final_result_ann = model_ann.predict(df_inf[['membership_category','avg_transaction_value','points_in_wallet','feedback']])
    st.write('Hasil Prediksi: ')
    if final_result_ann == 1:
        st.subheader('Churn')
    else:
        st.subheader('No Churn')





