import pickle
import streamlit as st
import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.tree import DecisionTreeClassifier

filename = 'decision_tree_model_covid.pkl'
with open(filename,'rb') as file:
    loaded_model = pickle.load(file)
GeneratorExit
st.title('Covid-19 Psychological Effects Prediction App')
st.subheader('Please enter your data : ')    

df = pd.read_csv('covid_preprocessed_data.csv')
columns_list = df.columns.to_list()

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns
    object_columns = df.select_dtypes(include=['object']).columns

    age_mapping = {'19-25': 22, 'Dec-18': 18, '33-40': 36.5, '60+': 65, '26-32': 29, '40-50': 45,
                   '50-60': 55}
    df['age'] = df['age'].map(age_mapping)
    print(df['age'])

    numerical_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    df_numerical = pd.DataFrame(numerical_transformer.fit_transform(df[numerical_columns]), columns=numerical_columns)
    df_categorical = pd.get_dummies(df[object_columns], columns=object_columns)
    
    df_preprocessed = pd.concat([df_numerical, df_categorical], axis=1)
    
    df_preprocessed = df_preprocessed.reindex(columns=columns_list, fill_value=0)

    prediction = loaded_model.predict(df_preprocessed)
    prediction_text = np.where(prediction == 1, 'Yes', 'No')
    st.subheader('Lifestyle Change:')
    st.write(prediction_text)
