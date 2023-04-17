# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 13:54:12 2023

@author: Engr. Okechulwu
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models

diabetes_model = pickle.load(open('C:/Users/WCLENG-9/Desktop/Multiple Disease Pediction System/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:/Users/WCLENG-9/Desktop/Multiple Disease Pediction System/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('C:/Users/WCLENG-9/Desktop/Multiple Disease Pediction System/parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('C:/Users/WCLENG-9/Desktop/Multiple Disease Pediction System/breast_cancer.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction',
                           'Breast Cancer Prediction'],
                          icons=['activity','heart','person','gender-female'],
                          default_index=0)


# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.slider('Number of Pregnancies', 0, 10, 0, 1)
        
    with col2:
        Glucose = st.slider('Glucose Level', 0, 200, 1, 1)
    
    with col3:
        BloodPressure = st.slider('Blood Pressure value', 0, 150, 1, 1)
    
    with col1:
        SkinThickness = st.slider('Skin Thickness value', 0, 70, 1, 1)
    
    with col2:
        Insulin = st.slider('Insulin Level', 0, 500, 1, 1)
    
    with col3:
        BMI = st.slider('BMI value', 0.0, 50.0, 1.0, 1.0)
    
    with col1:
        DiabetesPedigreeFunction = st.slider('Diabetes Pedigree Function value', 0.0, 1.0, 0.0, 0.01 )
    
    with col2:
        Age = st.slider('Age of the Person', 0, 100, 1, 1)
        
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider('Age of the Patient', 0, 100, 1, 1)
        
    with col2:
        sex = st.slider('Gender of Patient', 0, 1, 0, 1 )
        
    with col3:
        cp = st.slider('Chest Pain types', 0, 3, 0, 1)
        
    with col1:
        trestbps = st.slider('Resting Blood Pressure', 0, 200, 1, 1)
        
    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl', 0, 500, 1, 1)
        
    with col3:
        fbs = st.slider('Fasting Blood Sugar > 120 mg/dl', 0, 1, 0, 1)
        
    with col1:
        restecg = st.slider('Resting Electrocardiographic results', 0, 1, 0, 1)
        
    with col2:
        thalach = st.slider('Maximum Heart Rate achieved', 0, 200, 1, 1)
        
    with col3:
        exang = st.slider('Exercise Induced Angina', 0, 1, 0, 1)
        
    with col1:
        oldpeak = st.slider('ST depression induced by exercise', 0.0, 5.0, 0.0, 0.01)
        
    with col2:
        slope = st.slider('Slope of the peak exercise ST segment', 0, 3, 0, 1)
        
    with col3:
        ca = st.slider('Major vessels colored by flourosopy', 0, 4, 0, 1)
        
    with col1:
        thal = st.slider('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', 0, 3, 0, 1)
        
    
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'Heart Disease detected!'
        else:
          heart_diagnosis = 'Heart Disease not detected!'
        
    st.success(heart_diagnosis)
    
    
    
    
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.slider('MDVP:Fo(Hz)', 0.000, 400.000, 0.000)
        
    with col2:
        fhi = st.slider('MDVP:Fhi(Hz)', 0.000, 400.000, 0.000, 0.001)
        
    with col3:
        flo = st.slider('MDVP:Flo(Hz)', 0.000, 400.000, 0.000, 0.001)
        
    with col4:
        Jitter_percent = st.slider('MDVP:Jitter(%)', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col5:
        Jitter_Abs = st.slider('MDVP:Jitter(Abs)', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col1:
        RAP = st.slider('MDVP:RAP', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col2:
        PPQ = st.slider('MDVP:PPQ', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col3:
        DDP = st.slider('Jitter:DDP', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col4:
        Shimmer = st.slider('MDVP:Shimmer', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col5:
        Shimmer_dB = st.slider('MDVP:Shimmer(dB)', 0.000, 1.000, 0.000, 0.001)
        
    with col1:
        APQ3 = st.slider('Shimmer:APQ3', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col2:
        APQ5 = st.slider('Shimmer:APQ5', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col3:
        APQ = st.slider('MDVP:APQ', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col4:
        DDA = st.slider('Shimmer:DDA', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col5:
        NHR = st.slider('NHR', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col1:
        HNR = st.slider('HNR', 0.0000, 50.0000, 0.0000, 0.0001)
        
    with col2:
        RPDE = st.slider('RPDE', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col3:
        DFA = st.slider('DFA', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col4:
        spread1 = st.slider('spread1', -6.00000, 1.00000, -6.00000, 0.000001)
        
    with col5:
        spread2 = st.slider('spread2', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col1:
        D2 = st.slider('D2', 0.00000, 1.00000, 0.00000, 0.000001)
        
    with col2:
        PPE = st.slider('PPE', 0.00000, 1.00000, 0.00000, 0.000001)
        
        
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)




# Breast Cancer Prediction Page
if (selected == 'Breast Cancer Prediction'):
    
    st.title('Breast Cancer Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2 = st.columns(2)
    
    with col1:
        radius_mean = st.slider('Mean Radius', 0, 50, 0, 1)
        
    with col1:
        perimeter_mean = st.slider('Perimeter Mean', 0, 200, 1, 1)
    
    with col1:
        area_mean = st.slider('Area Mean', 0, 150, 1, 1)
    
    with col1:
        symmetry_mean = st.slider('Symmetry Mean', 0.00000, 1.00000, 0.00000, 0.000001)
    
    with col1:
        compactness_mean = st.slider('Compactness Mean', 0.00000, 1.00000, 0.00000, 0.000001)
    
    with col1:
        concave_points_mean = st.slider('Concave Points Mean', 0.0, 50.0, 1.0, 1.0)
        
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Test Result"):
        breast_cancer_prediction = breast_cancer_model.predict([[radius_mean, perimeter_mean, area_mean, symmetry_mean, compactness_mean, concave_points_mean]])                          
        
        if (breast_cancer_prediction[0] == 1):
          breast_cancer_diagnosis = "The Breast Cancer is Benign"
        else:
          breast_cancer_diagnosis = "The Breast Cancer is Malignant"
        
    st.success(breast_cancer_diagnosis)
        