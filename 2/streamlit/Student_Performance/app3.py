import pickle
import pandas as pd
import numpy as np
import streamlit as st

with open('Linear.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# streamlit app
st.title('Student Performance Prediction')

# ['Hours_Studied','Attendance','Access_to_Resources_m','Motivation_Level_m']

Hours_Studied=st.number_input("Enter the houre of studies",min_value=0,max_value=24,value=5)
Attendance=st.number_input('Attendance',min_value=0,max_value=365,value=60)
Access_to_Resources_m=st.selectbox('Access_to_Resources_m',['High','Medium','Low'])
Motivation_Level_m=st.selectbox('Motivation_Level',['High','Medium','Low'])


#Prepare the input data as a dictionary
input_data = {
    'Enter the houre of studies':Hours_Studied,
    'Attendance':Attendance,
    'Access_to_Resources':Access_to_Resources_m,
    'Motivation_Level':Motivation_Level_m,
}

#convert input data to dataframe
new_data=pd.DataFrame([input_data])

lmh={
    'Low':1,
    "Medium":2,
    'High':3
}

new_data['Access_to_Resources']=new_data['Access_to_Resources'].map(lmh)
new_data['Motivation_Level']=new_data['Motivation_Level'].map(lmh)

# Load the saved features list
df = pd.read_csv("cleaned.csv")
columns_list = df.columns.to_list()

# Reindex to match the original column order
new_data = new_data.reindex(columns=columns_list, fill_value=0)

# Make predictions
prediction = loaded_model.predict(new_data)

# Output the prediction
if st.button('Predict'):
    st.write('Predicted Score :',prediction[0])