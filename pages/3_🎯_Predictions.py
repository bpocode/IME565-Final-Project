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
import streamlit as st
import pandas as pd

st.header("**Patient Demographic Analysis**")

# Load the heart disease dataset
df = pd.read_csv('heart.csv')

# This should come after the user has submitted the form
# Assuming you have these variables from the form submission
if st.session_state.get('form_submitted', False):
    
    # Get user inputs from session state
    age = st.session_state.get('age')
    sex = st.session_state.get('sex')
    chest_pain_type = st.session_state.get('chest_pain_type')
    resting_bp = st.session_state.get('resting_bp')
    cholesterol = st.session_state.get('cholesterol')
    fasting_bs = st.session_state.get('fasting_bs')
    resting_ecg = st.session_state.get('resting_ecg')
    max_hr = st.session_state.get('max_hr')
    exercise_angina = st.session_state.get('exercise_angina')
    oldpeak = st.session_state.get('oldpeak')
    st_slope = st.session_state.get('st_slope')
    
    with st.expander("Age Group Comparison"):
        # Create age groups
        age_bins = [0, 35, 45, 55, 65, 100]
        age_labels = ['Under 35', '35-44', '45-54', '55-64', '65+']
        df['age_group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels, right=False)
        user_age_group = pd.cut([age], bins=age_bins, labels=age_labels, right=False)[0]
        percentage = df['age_group'].value_counts(normalize=True).get(user_age_group, 0) * 100
        st.markdown(f"""
        **Age Group:** Your selection: **{user_age_group}**  
        Percentage of patients in this age group: **{percentage:.2f}%**
        """)
    
    with st.expander("Sex Comparison"):
        percentage = df['Sex'].value_counts(normalize=True).get(sex, 0) * 100
        sex_label = "Male" if sex == 'M' else "Female"
        st.markdown(f"""
        **Sex:** Your selection: **{sex_label}**  
        Percentage of patients with this sex: **{percentage:.2f}%**
        """)
    
    with st.expander("Chest Pain Type Comparison"):
        percentage = df['ChestPainType'].value_counts(normalize=True).get(chest_pain_type, 0) * 100
        chest_pain_names = {
            'ATA': 'Atypical Angina',
            'NAP': 'Non-Anginal Pain',
            'ASY': 'Asymptomatic',
            'TA': 'Typical Angina'
        }
        st.markdown(f"""
        **Chest Pain Type:** Your selection: **{chest_pain_names[chest_pain_type]}**  
        Percentage of patients with this type: **{percentage:.2f}%**
        """)
    
    with st.expander("Resting Blood Pressure Comparison"):
        # Create BP categories
        bp_bins = [0, 120, 130, 140, 200]
        bp_labels = ['Normal (<120)', 'Elevated (120-129)', 'High Stage 1 (130-139)', 'High Stage 2 (≥140)']
        df['bp_category'] = pd.cut(df['RestingBP'], bins=bp_bins, labels=bp_labels, right=False)
        user_bp_category = pd.cut([resting_bp], bins=bp_bins, labels=bp_labels, right=False)[0]
        percentage = df['bp_category'].value_counts(normalize=True).get(user_bp_category, 0) * 100
        st.markdown(f"""
        **Blood Pressure Category:** Your selection: **{user_bp_category}**  
        Percentage of patients in this category: **{percentage:.2f}%**
        """)
    
    with st.expander("Cholesterol Level Comparison"):
        # Create cholesterol categories
        chol_bins = [0, 200, 240, 650]
        chol_labels = ['Normal (<200)', 'Borderline (200-239)', 'High (≥240)']
        df['chol_category'] = pd.cut(df['Cholesterol'], bins=chol_bins, labels=chol_labels, right=False)
        user_chol_category = pd.cut([cholesterol], bins=chol_bins, labels=chol_labels, right=False)[0]
        percentage = df['chol_category'].value_counts(normalize=True).get(user_chol_category, 0) * 100
        st.markdown(f"""
        **Cholesterol Category:** Your selection: **{user_chol_category}**  
        Percentage of patients in this category: **{percentage:.2f}%**
        """)
    
    with st.expander("Fasting Blood Sugar Comparison"):
        percentage = df['FastingBS'].value_counts(normalize=True).get(int(fasting_bs), 0) * 100
        fbs_label = "Elevated (>120 mg/dL)" if fasting_bs >= 0.5 else "Normal (<120 mg/dL)"
        st.markdown(f"""
        **Fasting Blood Sugar:** Your selection: **{fbs_label}**  
        Percentage of patients with this level: **{percentage:.2f}%**
        """)
    
    with st.expander("Resting ECG Comparison"):
        percentage = df['RestingECG'].value_counts(normalize=True).get(resting_ecg, 0) * 100
        ecg_names = {
            'Normal': 'Normal',
            'ST': 'ST-T Wave Abnormality',
            'LVH': 'Left Ventricular Hypertrophy'
        }
        st.markdown(f"""
        **Resting ECG:** Your selection: **{ecg_names[resting_ecg]}**  
        Percentage of patients with this result: **{percentage:.2f}%**
        """)
    
    with st.expander("Maximum Heart Rate Comparison"):
        # Create heart rate categories
        hr_bins = [0, 100, 120, 140, 160, 220]
        hr_labels = ['Very Low (<100)', 'Low (100-119)', 'Normal (120-139)', 'High (140-159)', 'Very High (≥160)']
        df['hr_category'] = pd.cut(df['MaxHR'], bins=hr_bins, labels=hr_labels, right=False)
        user_hr_category = pd.cut([max_hr], bins=hr_bins, labels=hr_labels, right=False)[0]
        percentage = df['hr_category'].value_counts(normalize=True).get(user_hr_category, 0) * 100
        st.markdown(f"""
        **Max Heart Rate Category:** Your selection: **{user_hr_category}**  
        Percentage of patients in this category: **{percentage:.2f}%**
        """)
    
    with st.expander("Exercise Angina Comparison"):
        percentage = df['ExerciseAngina'].value_counts(normalize=True).get(exercise_angina, 0) * 100
        angina_label = "Yes" if exercise_angina == 'Y' else "No"
        st.markdown(f"""
        **Exercise-Induced Angina:** Your selection: **{angina_label}**  
        Percentage of patients with this condition: **{percentage:.2f}%**
        """)
    
    with st.expander("ST Slope Comparison"):
        percentage = df['ST_Slope'].value_counts(normalize=True).get(st_slope, 0) * 100
        st.markdown(f"""
        **ST Slope:** Your selection: **{st_slope}**  
        Percentage of patients with this slope: **{percentage:.2f}%**
        """)
    
    with st.expander("Oldpeak (ST Depression) Comparison"):
        # Create oldpeak categories
        oldpeak_bins = [-10, 0, 1, 2, 10]
        oldpeak_labels = ['None (0)', 'Mild (0-1)', 'Moderate (1-2)', 'Severe (>2)']
        df['oldpeak_category'] = pd.cut(df['Oldpeak'], bins=oldpeak_bins, labels=oldpeak_labels, right=False)
        user_oldpeak_category = pd.cut([oldpeak], bins=oldpeak_bins, labels=oldpeak_labels, right=False)[0]
        percentage = df['oldpeak_category'].value_counts(normalize=True).get(user_oldpeak_category, 0) * 100
        st.markdown(f"""
        **ST Depression Category:** Your selection: **{user_oldpeak_category}**  
        Percentage of patients in this category: **{percentage:.2f}%**
        """)

else:
    st.info("ℹ️ Please fill out the health assessment form and click **Submit** to see your demographic comparison.")

    
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