import pickle
import pandas as pd
import numpy as np
import streamlit as st

with open("Linear.pkl","rb") as file:
    loaded_model=pickle.load(file)
# Streamlit app
st.title("Student Performance Prediction")

# ['Hours_Studied','Attendance','Access_to_Resources_m','Motivation_Level_m']

hours_studied = st.number_input("Enter the Hour studied", min_value=0, max_value=25, value=2)
Attendance = st.number_input("Enter Attendance", min_value=0, max_value=365, value=10)
Access_to_Resources_m = st.selectbox("Access To Resources", ["High", "Medium","Low"])
Motivation_Level_m = st.selectbox("Motivation Level", ["High", "Medium","Low"])

input_data = {
    "Hours Studied": hours_studied,
    "Attendance": Attendance,
    "Access To Resources": Access_to_Resources_m,
    "Motivation Level": Motivation_Level_m,
}    

new_data = pd.DataFrame([input_data])

lmh={
    'Low':1,
    'Medium':2,
    'High':3
}    
new_data['Access To Resources'] =new_data['Access To Resources'].map(lmh)
new_data['Motivation Level'] =new_data['Motivation Level'].map(lmh)

df = pd.read_csv("Cleaned.csv")
columns_list = df.columns.to_list()

new_data = new_data.reindex(columns=columns_list, fill_value=0)

prediction = loaded_model.predict(new_data)

if st.button("Predict"):
    st.write("Predicted Score :",prediction[0])
    if prediction[0] < 50 :
        st.error("You are Successfully Ummfi")
    else:
        st.success("Raskapettu Monee")

