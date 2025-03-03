import streamlit as st
import numpy as np
import pickle as pk
import pandas as pd


with open("Log_model.pkl","rb") as file:
    model=pk.load(file)
    
    
id=st.number_input("Enter your Id: ",min_value=1,)
diet=st.selectbox("Choose your diet",['low fat', 'no fat'])
pulse=st.number_input("Enter your pulse: ",min_value=80,max_value=150,value=120)
time=st.number_input("Enter minute: ",min_value=1,max_value=60)


input_data={
    "Id":id,
    "Diet":diet,
    "pulse":pulse,
    "Time":time
}
df=pd.DataFrame([input_data])

# df['diet'] = df['diet'].map({"low fat":0,'no fat':1})





df1 = pd.read_csv("cleaned_features.csv")
columns_list = [col for col in df1.columns if col != 'Unnamed: 0']

df = df.reindex(columns=columns_list, fill_value=0)


prediction=model.predict(df)
if st.button('predict'):
    st.write(prediction[0])