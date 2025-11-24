import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Input Page", page_icon = "📚")

# Title and description
st.markdown(
    """
    <h2 style="text-align: center; color: #69503c;">Heart Failure Predictor - Please Enter your information below</h2>
    <p style="text-align: center; font-size: 18px; color: #1c2d8f;">
    Fill out the form below with your details.
    </p>
    """,
    unsafe_allow_html = True
)

with st.form("user_inputs_form"):
    age = st.number_input(
        'Age',
        value = st.session_state.get('age', 40),  # Load saved or default
        min_value = 0, max_value = 100, step = 1
    )

    sex = st.selectbox(
        'sex',
        options = ['M', 'F'],
        index = 0 if st.session_state.get('sex', 'M') == 'M' else 1
    )

    chest_pain_type = st.selectbox(
        'Chest Pain Type',
        options = ['ATA', 'NAP', 'ASY', 'TA'],
        index = 0 if st.session_state.get('chest_pain_type', 'ATA') == 'ATA' else 1
    )

    resting_bp = st.number_input(
            'Resting Blood Pressure',
            value = st.session_state.get('resting_bp', 120),  # Load saved or default
            min_value = 0, max_value = 200, step = 1
        )

    cholesterol = st.number_input(
            'Cholesterol',
            value = st.session_state.get('cholesterol', 200),  # Load saved or default
            min_value = 0, max_value = 650, step = 1
        )

    fasting_bs = st.number_input(
            'Fasting Blood Sugar',
            value = st.session_state.get('fasting_bs', 0.5),  # Load saved or default
            min_value = 0.0, max_value = 1.0, step = 0.01
        )

    resting_ecg = st.selectbox(
        'Resting ECG',
        options = ['Normal', 'ST', 'LVH'],
        index = 0 if st.session_state.get('resting_ecg', 'Normal') == 'Normal' else 1
    )

    max_hr = st.number_input(
            'Max Heart Rate',
            value = st.session_state.get('max_hr', 200),  # Load saved or default
            min_value = 0, max_value = 650, step = 1
    )

    exercise_angina = st.selectbox(
        'Exercise Angina?',
        options = ['Y', 'N'],
        index = 0 if st.session_state.get('exercise_angina', 'Y') == 'Y' else 1
    )

    oldpeak = st.number_input(
            'Oldpeak',
            value = st.session_state.get('oldpeak', 1.0),  # Load saved or default
            min_value = -10.0, max_value = 10.0, step = 0.1
    )

    st_slope = st.selectbox(
        'ST Slope',
        options = ['Up', 'Flat', 'Down'],
        index = 0 if st.session_state.get('st_slope', 'Up') == 'Up' else 1
    )

    submit_button = st.form_submit_button("Submit")

if submit_button:
    st.session_state['age'] = age
    st.session_state['sex'] = sex
    st.session_state['chest_pain_type'] = chest_pain_type
    st.session_state['resting_bp'] = resting_bp
    st.session_state['cholesterol'] = cholesterol
    st.session_state['fasting_bs'] = fasting_bs
    st.session_state['resting_ecg'] = resting_bp
    st.session_state['max_hr'] = max_hr
    st.session_state['exercise_angina'] = exercise_angina
    st.session_state['oldpeak'] = oldpeak
    st.session_state['st_slope'] = st_slope
    st.session_state['form_submitted'] = True