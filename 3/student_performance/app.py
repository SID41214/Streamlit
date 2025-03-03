import pickle
import numpy as np
import pandas as pd
import streamlit as st
# from sklearn.preprocessing import LabelEncoder

st.title("Student Score")

hours=st.number_input("Enter Study Hour", min_value=0, max_value=24, value=1)
attendance=st.number_input("Enter total attendance", min_value=0, max_value=100, value=70)
acesstoresource=st.selectbox("Access_to_Resources", ["LOW", "Medium","HIGH" ])
Motivation_Level=st.selectbox("Motivation_Level", ["LOW", "Medium","HIGH" ])




input_data={
    
    "Hours":hours,
    "Attendance":attendance,
    "Access_to_Resources":acesstoresource,
    "Motivation_Level":Motivation_Level
    
}


new_data = pd.DataFrame([input_data])

lmh={
    'Low':1,
    'Medium':2,
    'High':3
}


new_data['Access_Resource_map']=new_data['Access_to_Resources'].map(lmh)

new_data['Motivation_Level_map']=new_data['Motivation_Level'].map(lmh)

new_data.drop(["Access_to_Resources","Motivation_Level"],axis=1,inplace=True)

df = pd.read_csv("cleaned_features.csv")
columns_list = [col for col in df.columns if col != 'Unnamed: 0']

new_data = new_data.reindex(columns=columns_list, fill_value=0)


with open('linear.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
    

prediction = loaded_model.predict(new_data)

if st.button('Predict'):
    if prediction[0] > 50:
        st.balloons()
    st.write('The predicted score is:', prediction[0])

