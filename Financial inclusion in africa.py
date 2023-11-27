import streamlit as st
import pickle
import pandas as pd

with open('C:\\Users\Lenovo\Downloads\logistic_model.pkl', 'rb') as f:

    logistic_model = pickle.load(f) # deserialize using load()

with open('C:\\Users\\Lenovo\\Downloads\\label_encoder.pkl', 'rb') as f:

    label_encoder = pickle.load(f) # deserialize using load()

local_image_path = 'C:\\Users\\Lenovo\\Downloads\\overview-philippine-banking.jpg'
image = open(local_image_path, 'rb').read()

# Display the image using st.image
st.image(image, use_column_width=True)


st.title(" Financial inclusion in Africa ")
st.subheader("Accusation/Use of a bank account prediction ")
col1 , col2,col3,col4 = st.columns(4)
with col1 :
    choices = ['','Kenya', 'Rwanda', 'Tanzania', 'Uganda']

    # Create a dropdown menu using selectbox
    selected_choice = st.selectbox('country:', choices)
    try:
        country = label_encoder.transform([[country]]) if REGION else None
    except:
        country = -1
with col2 :

    # Your array of choices
    # Your array of choices
    choices = ['','2016','2017','2018']

    # Create a dropdown menu using selectbox
    year = st.selectbox('year:', choices)

with col3:
    choices = ['','Rural','Urban']
    location_type = st.selectbox('location_type:', choices)
    try:
        location_type = label_encoder.transform([[location_type]]) if location_type else None
    except:
        location_type = -1
with col4:
    choices = ['', 'Yes', 'No']
    cellphone_access = st.selectbox('Cellphone access:', choices)
    try:
        cellphone_access = label_encoder.transform([[cellphone_access]]) if cellphone_access else None
    except:
        cellphone_access = -1


with col1 :
    household_size = st.text_input ('Household size')
with col2 :
    age_of_respondent = st.text_input ('Age of respondent')
with col3 :
    gender_of_respondent = st.text_input ('Gender')
    try:
        gender_of_respondent = label_encoder.transform([[gender_of_respondent]]) if gender_of_respondent else None
    except:
        gender_of_respondent = -1
with col4 :
    relationship_with_head = st.text_input('Relationship with head')
    try:
        relationship_with_head = label_encoder.transform([[relationship_with_head]]) if relationship_with_head else None
    except:
        relationship_with_head = -1
with col1 :
    marital_status = st.text_input('Marital status')
    try:
        marital_status = label_encoder.transform([[marital_status]]) if marital_status else None
    except:
        marital_status = -1
with col2 :
    education_level = st.text_input('Education level')
    try:
        education_level = label_encoder.transform([[education_level]]) if education_level else None
    except:
        education_level = -1
with col3:
    job_type = st.text_input('Job type')
    try:
        job_type = label_encoder.transform([[job_type]]) if job_type else None
    except:
        job_type = -1

if(st.button('Submit')):
    list = [country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,relationship_with_head,marital_status,education_level,job_type]
    list = [int(item) if str(item).isdigit() else 0 for item in list]
    result = logistic_model.predict([list])
    if(result == '0'):
        st.success('this person has an account')
    else :
        st.warning('this person doesnt have an account')