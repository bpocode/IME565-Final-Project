import streamlit as st
st.set_page_config(
    page_title = "Home",
    page_icon = "👋",
    # layout = "wide"
)

# Centered Title using HTML and Markdown
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Heart Failure Predictor ❤️</h2>
    """,
    unsafe_allow_html = True,
)

# Insert an image
st.image('heart.png', width = 'stretch', 
         caption = "Predict whether or not you have heart failure")


# Initialize session state keys
if 'age' not in st.session_state:
    st.session_state['age'] = 50
if 'sex' not in st.session_state:
    st.session_state['sex'] = 'M'
if 'chest_pain_type' not in st.session_state:
    st.session_state['chest_pain_type'] = 'ATA'
if 'resting_bp' not in st.session_state:
    st.session_state['resting_bp'] = 130
if 'cholesterol' not in st.session_state:
    st.session_state['cholesterol'] = 200
if 'fasting_bs' not in st.session_state:
    st.session_state['fasting_bs'] = 0.25
if 'resting_ecg' not in st.session_state:
    st.session_state['resting_ecg'] = 'Normal'
if 'max_hr' not in st.session_state:
    st.session_state['max_hr'] = 140
if 'exercise_angina' not in st.session_state:
    st.session_state['exercise_angina'] = 'N'
if 'oldpeak' not in st.session_state:
    st.session_state['oldpeak'] = 1.0
if 'st_slope' not in st.session_state:
    st.session_state['st_slope'] = 'Up'
if 'form_submitted' not in st.session_state:
    st.session_state['form_submitted'] = False # Track if form is submitted


