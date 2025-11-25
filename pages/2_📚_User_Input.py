import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Input Page", page_icon = "📚")

# Title and description
st.markdown(
    """
    <h2 style="text-align: center; color: #69503c;">User Input 📚</h2>
    <p style="text-align: center; font-size: 18px; color: #1c2d8f;">
    Fill out the form below with your details.
    </p>
    """,
    unsafe_allow_html = True
)

with st.form("user_inputs_form"):
    
    # Personal Information Section
    st.markdown("### 👤 Personal Information")
    
    age = st.number_input(
        'Age',
        value = st.session_state.get('age', 40),
        min_value = 0, max_value = 100, step = 1,
        help = "Enter your age in years (typical range: 28-77)"
    )
    
    sex = st.selectbox(
        'Sex',
        options = ['M', 'F'],
        index = 0 if st.session_state.get('sex', 'M') == 'M' else 1,
        help = "M = Male, F = Female"
    )
    
    st.divider()
    
    # Cardiovascular Symptoms Section
    st.markdown("### 💓 Cardiovascular Symptoms")
    
    chest_pain_type = st.selectbox(
        'Chest Pain Type',
        options = ['ATA', 'NAP', 'ASY', 'TA'],
        index = ['ATA', 'NAP', 'ASY', 'TA'].index(st.session_state.get('chest_pain_type', 'ATA')),
        help = """
        - **ATA**: Atypical Angina (mild chest discomfort)
        - **NAP**: Non-Anginal Pain (chest pain not related to heart)
        - **ASY**: Asymptomatic (no chest pain)
        - **TA**: Typical Angina (classic heart-related chest pain)
        """
    )
    
    exercise_angina = st.selectbox(
        'Exercise-Induced Angina',
        options = ['N', 'Y'],
        index = 0 if st.session_state.get('exercise_angina', 'N') == 'N' else 1,
        help = "Do you experience chest pain during physical activity? Y = Yes, N = No"
    )
    
    st.divider()
    
    # Clinical Measurements Section
    st.markdown("### 🩺 Clinical Measurements")
    
    resting_bp = st.number_input(
        'Resting Blood Pressure (mm Hg)',
        value = st.session_state.get('resting_bp', 120),
        min_value = 0, max_value = 200, step = 1,
        help = "Normal: 90-120 mm Hg | High: >130 mm Hg"
    )
    
    cholesterol = st.number_input(
        'Cholesterol (mg/dL)',
        value = st.session_state.get('cholesterol', 200),
        min_value = 0, max_value = 650, step = 1,
        help = "Normal: <200 mg/dL | Borderline: 200-239 | High: ≥240 mg/dL"
    )
    
    fasting_bs = st.number_input(
        'Fasting Blood Sugar',
        value = st.session_state.get('fasting_bs', 0.0),
        min_value = 0.0, max_value = 1.0, step = 0.01,
        help = "0 = Normal (<120 mg/dL) | 1 = Elevated (>120 mg/dL)"
    )
    
    max_hr = st.number_input(
        'Maximum Heart Rate (bpm)',
        value = st.session_state.get('max_hr', 150),
        min_value = 60, max_value = 220, step = 1,
        help = "Highest heart rate achieved during exercise (typical range: 60-202 bpm)"
    )
    
    oldpeak = st.number_input(
        'Oldpeak (ST Depression)',
        value = st.session_state.get('oldpeak', 1.0),
        min_value = -10.0, max_value = 10.0, step = 0.1,
        help = "ST depression induced by exercise (0 = normal, higher values indicate more depression)"
    )
    
    st_slope = st.selectbox(
        'ST Slope',
        options = ['Up', 'Flat', 'Down'],
        index = ['Up', 'Flat', 'Down'].index(st.session_state.get('st_slope', 'Up')),
        help = """
        Slope of peak exercise ST segment:
        - **Up**: Upsloping (healthier)
        - **Flat**: Flat (moderate concern)
        - **Down**: Downsloping (higher concern)
        """
    )
    
    st.divider()
    
    # ECG Results Section
    st.markdown("### 📊 ECG Results")
    
    resting_ecg = st.selectbox(
        'Resting ECG',
        options = ['Normal', 'ST', 'LVH'],
        index = ['Normal', 'ST', 'LVH'].index(st.session_state.get('resting_ecg', 'Normal')),
        help = """
        - **Normal**: Normal ECG
        - **ST**: ST-T wave abnormality (T wave inversions and/or ST elevation/depression)
        - **LVH**: Left Ventricular Hypertrophy (enlarged heart muscle)
        """
    )
    
    st.divider()
    
    submit_button = st.form_submit_button("Submit", use_container_width=True, type="primary")

if submit_button:
    st.session_state['age'] = age
    st.session_state['sex'] = sex
    st.session_state['chest_pain_type'] = chest_pain_type
    st.session_state['resting_bp'] = resting_bp
    st.session_state['cholesterol'] = cholesterol
    st.session_state['fasting_bs'] = fasting_bs
    st.session_state['resting_ecg'] = resting_ecg
    st.session_state['max_hr'] = max_hr
    st.session_state['exercise_angina'] = exercise_angina
    st.session_state['oldpeak'] = oldpeak
    st.session_state['st_slope'] = st_slope
    st.session_state['form_submitted'] = True
    
    st.success("✅ Form submitted successfully! Proceed to the Predictions page.")

with st.sidebar:
    st.header("📋 Complete Your Assessment")
    
    st.markdown("""
    **Ready to get your prediction?**
    
    Fill out all the fields in the form with your health information, then click **Submit** and go to the **Predictions** page.
    """)
    
    st.divider()

    st.info("💡 **Tip:** Have your recent medical records handy for accurate results")
    
    st.warning("⚠️ This is not medical advice—consult your healthcare provider")