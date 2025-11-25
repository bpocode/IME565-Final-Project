import streamlit as st
import pandas as pd
import pickle
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title = "Predictions", 
                   page_icon = "🎯")

# Page title
st.markdown(
    """
    <h2 style="text-align: center; color: #4a4a4a;">Heart Disease Prediction 🎯</h2>
    """,
    unsafe_allow_html=True,
)

# # Ensure session state keys are initialized
if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False

# Check if the form has been submitted
if st.session_state['form_submitted'] == False:
    st.warning("Please fill out the form on the 'User Input' page before viewing predictions.")
    st.stop()

# Load the trained model and dataset
with open('model_ada_heart.pickle', 'rb') as model_file:
    ada_model = pickle.load(model_file)

with open('model_dt_heart.pickle', 'rb') as model_file:
    dt_model = pickle.load(model_file)

with open('model_rf_heart.pickle', 'rb') as model_file:
    rf_model = pickle.load(model_file)

with open('model_vote_heart.pickle', 'rb') as model_file:
    vote_model = pickle.load(model_file)

age = st.session_state['age']
sex = st.session_state['sex'] 
chest_pain_type = st.session_state['chest_pain_type'] 
resting_bp = st.session_state['resting_bp'] 
cholesterol = st.session_state['cholesterol']
fasting_bs = st.session_state['fasting_bs'] 
resting_ecg = st.session_state['resting_ecg'] 
max_hr = st.session_state['max_hr'] 
exercise_angina = st.session_state['exercise_angina']
oldpeak = st.session_state['oldpeak']
st_slope = st.session_state['st_slope'] 

sex_m = 0
if sex == 'M':
    sex_m = 1

ChestPainType_ATA, ChestPainType_NAP, ChestPainType_TA = 0,0,0
if chest_pain_type == 'ATA':
    ChestPainType_ATA = 1
elif chest_pain_type == 'NAP':
    ChestPainType_NAP = 1
elif chest_pain_type == 'TA':
    ChestPainType_TA = 1

RestingECG_Normal, RestingECG_ST = 0,0
if resting_ecg == 'Normal':
    RestingECG_Normal = 1
elif resting_ecg == 'ST':
    RestingECG_ST = 1

ExerciseAngina_Y = 0
if ExerciseAngina_Y == 'Y':
    ExerciseAngina_Y = 1

ST_Slope_Flat, ST_Slope_Up = 0,0
if st_slope == 'Flat':
    ST_Slope_Flat = 1
if st_slope == 'Up':
    ST_Slope_Up = 1

model = st.selectbox(
        'Select Model',
        options = ['ADA Boost', 'Decision Tree', 'Random Forest','Soft Voting'],
    )

model_dict = {'ADA Boost': ada_model,'Decision Tree':dt_model,'Random Forest':rf_model,'Soft Voting':vote_model}

selected_model = model_dict[model]

if st.button('Predict'):
    prediction = selected_model.predict([[age,resting_bp,cholesterol,fasting_bs,max_hr,oldpeak,sex_m,ChestPainType_ATA,
                   ChestPainType_NAP,ChestPainType_TA,RestingECG_Normal,RestingECG_ST,ExerciseAngina_Y,ST_Slope_Flat,ST_Slope_Up]])

    if prediction == 0:
        st.success('You do not have heart failure!')
        st.balloons()

    if prediction == 1:
        st.warning('You may be at risk for heart failure. Please see next page for recommendations.')
# ['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak',
#        'Sex_M', 'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA',
#        'RestingECG_Normal', 'RestingECG_ST', 'ExerciseAngina_Y',
#        'ST_Slope_Flat', 'ST_Slope_Up'],

with st.sidebar:
    st.header("⚙️ Guide")
    
    st.markdown("""
    **Steps:**
    1. Fill form
    2. Choose model
    3. Get Yes/No prediction
    
    **What You Get:**
    - Heart disease prediction
    - Health recommendations
    """)
    
    st.divider()
    
    st.warning("⚠️ Not medical advice")
    st.info("💬 Chat with Health Assistant after!")