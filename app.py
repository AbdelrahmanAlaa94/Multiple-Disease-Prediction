import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open('E:/College/Training/NTI/multiple-disease-prediction-streamlit-app-main/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('E:/College/Training/NTI/multiple-disease-prediction-streamlit-app-main/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('E:/College/Training/NTI/multiple-disease-prediction-streamlit-app-main/saved_models/parkinsons_data_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        Age = st.text_input('Age')
    with col2:
        Gender = st.text_input('Gender')
    with col3:
        BMI = st.text_input('BMI')
    with col4:
        Smoking = st.text_input('Smoking')
    with col5:
        AlcoholConsumption = st.text_input('Alcohol Consumption')
    
    with col1:
        PhysicalActivity = st.text_input('Physical Activity')
    with col2:
        FamilyHistoryParkinsons = st.text_input('Family History of Parkinson’s')
    with col3:
        TraumaticBrainInjury = st.text_input('Traumatic Brain Injury')
    with col4:
        Hypertension = st.text_input('Hypertension')
    with col5:
        Diabetes = st.text_input('Diabetes')

    with col1:
        Depression = st.text_input('Depression')
    with col2:
        Stroke = st.text_input('Stroke')
    with col3:
        SystolicBP = st.text_input('Systolic BP')
    with col4:
        DiastolicBP = st.text_input('Diastolic BP')
    with col5:
        CholesterolTotal = st.text_input('Total Cholesterol')

    with col1:
        CholesterolLDL = st.text_input('LDL Cholesterol')
    with col2:
        CholesterolHDL = st.text_input('HDL Cholesterol')
    with col3:
        CholesterolTriglycerides = st.text_input('Triglycerides')
    with col4:
        UPDRS = st.text_input('UPDRS Score')
    with col5:
        MoCA = st.text_input('MoCA Score')

    with col1:
        Tremor = st.text_input('Tremor')
    with col2:
        Rigidity = st.text_input('Rigidity')
    with col3:
        Bradykinesia = st.text_input('Bradykinesia')
    with col4:
        PosturalInstability = st.text_input('Postural Instability')
    with col5:
        SpeechProblems = st.text_input('Speech Problems')

    with col1:
        SleepDisorders = st.text_input('Sleep Disorders')
    with col2:
        Constipation = st.text_input('Constipation')

    # Code for Prediction
    parkinsons_diagnosis = ''

    # Creating a button for Prediction
    if st.button("Parkinson's Test Result"):

        # Make sure all inputs are assigned before using them
        user_input = [
            Age, Gender, BMI, Smoking, AlcoholConsumption, PhysicalActivity,
            FamilyHistoryParkinsons, TraumaticBrainInjury, Hypertension, Diabetes,
            Depression, Stroke, SystolicBP, DiastolicBP, CholesterolTotal,
            CholesterolLDL, CholesterolHDL, CholesterolTriglycerides, UPDRS, MoCA,
            Tremor, Rigidity, Bradykinesia, PosturalInstability, SpeechProblems,
            SleepDisorders, Constipation
        ]

        # Convert inputs to float (Make sure they are not empty)
        try:
            user_input = [float(x) if x else 0 for x in user_input]
            parkinsons_prediction = parkinsons_model.predict([user_input])

            if parkinsons_prediction[0] == 1:
                parkinsons_diagnosis = "The person has Parkinson's disease"
            else:
                parkinsons_diagnosis = "The person does not have Parkinson's disease"
        except ValueError:
            st.error("Please enter valid numerical values for all inputs.")

    st.success(parkinsons_diagnosis)