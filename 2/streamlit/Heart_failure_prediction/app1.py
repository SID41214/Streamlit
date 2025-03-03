import pickle
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# streamlit app
st.title('Heart Disease prediction')

# input fields for user
age=st.number_input("Age",min_value=0,max_value=120,value=45)
sex=st.selectbox("sex",['M','F'])
chest_pain=st.selectbox("Chest Pain Type",['ATA','ASY','TA'])
resting_bp=st.number_input('Resting Blood Pressure',min_value=0,max_value=200,value=130)
cholesterol=st.number_input('cholesterol',min_value=0,max_value=500,value=230)
fasting_bs=st.selectbox('fasting blood suger',['0','1'])
resting_ecg=st.selectbox('resting ECG',['normal','ST','LVH'])
max_hr=st.number_input('max heart rate',min_value=60,max_value=220,value=170)
exercise_angina=st.selectbox('exercise angina',["N","Y"])
oldpeak=st.number_input('oldpeak',min_value=0.0,max_value=6.0,value=2.5)
st_slope=st.selectbox('ST slope',["up","flat","down"])

#Prepare the input data as a dictionary
input_data = {
    'Age':age,
    'Sex':sex,
    'ChestPainType':chest_pain,
    'RestingBP':resting_bp,
    'Cholestrol':cholesterol,
    'FastinngBS':fasting_bs,
    'RestingECG':resting_ecg,
    'MaxHR':max_hr,
    'ExerciseAngina':exercise_angina,
    'OldPeak':oldpeak,
    'ST_Slope':st_slope
}

#convert input data to dataframe
new_data=pd.DataFrame([input_data])

# load saved LabelEncoder
sex_encoder=LabelEncoder()
sex_encoder.classes_=np.array(['F','M'])

chest_pain_encoder=LabelEncoder()
chest_pain_encoder.classes_=np.array(['ATA','NAP','ASY','TA'])

resting_ecg_encoder=LabelEncoder()
resting_ecg_encoder.classes_=np.array(['normal','ST','LVH'])

exercise_angina_encoder=LabelEncoder()
exercise_angina_encoder.classes_=np.array(['N','Y'])

st_slope_encoder=LabelEncoder()
st_slope_encoder.classes_=np.array(["up","flat","down"])

# Apply label encoding to categorical columns
new_data['Encoder_sex']=sex_encoder.transform(new_data['Sex'])
new_data["Encoder_ChestPainType"] = chest_pain_encoder.transform(new_data["ChestPainType"])
new_data["Encoder_RestingECG"] = resting_ecg_encoder.transform(new_data["RestingECG"])
new_data["Encoder_ExerciseAngina"] = exercise_angina_encoder.transform(new_data["ExerciseAngina"])
new_data["Encoder_ST_Slope"] = st_slope_encoder.transform(new_data["ST_Slope"])

# Drop original columns as they are already encoded
new_data.drop(["Sex", "ChestPainType", "RestingECG", "ExerciseAngina", "ST_Slope"], axis=1, inplace=True)

# Load the saved features list
df = pd.read_csv("features.csv")
columns_list = [col for col in df.columns if col != 'Unnamed: 0']

# Reindex to match the original column order
new_data = new_data.reindex(columns=columns_list, fill_value=0)

# Load the saved scaler
with open('scaler.pkl', 'rb') as scaler_file:
    loaded_scaler = pickle.load(scaler_file)

# Scale the new data
scaled_data = pd.DataFrame(loaded_scaler.transform(new_data), columns=columns_list)

# Load the RandomForest model
with open('Random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Make predictions               
prediction = loaded_model.predict(scaled_data)

# Output the prediction
if prediction[0] == 1:
    st.error("Prediction: Heart Disease Present")
else:
    st.success("Prediction: No Heart Disease",)
    st.snow()
