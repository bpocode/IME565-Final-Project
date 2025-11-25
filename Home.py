import streamlit as st
st.set_page_config(
    page_title = "👋 Home",
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
#AI used to center image
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("heart.gif", caption="Predict whether or not you have heart failure")

# Caption
st.markdown(
    """
    <h2 style = "text-align: center; color: #69503c;">Utilize our advanced Machine Learning application to predict heart failure risk.</h2>
    """,
    unsafe_allow_html = True,
)

st.write("---")

with st.expander("What can you do with this app?"):
    st.markdown("""
    📝 **Fill Out a Health Assessment:** Provide a form where users can enter their own health metrics.

    ⭐ **Predict Risk of Heart Failure:** Use machine learning models to classify heart failure prediction.
        
    💬 **Chat With a Health Assistant:** Receive personalized, data-driven lifestyle recommendations.
    
    🔧 **Interactive Features:** Explore data with fully interactive charts and summaries!
    """)

st.sidebar.markdown("### 🔍 Navigate the App")

st.sidebar.markdown("""
- **Home:** Learn what the Heart Failure Predictor does and how to use it.

- **Understanding Models:** Explore the machine learning models used for risk prediction.

- **User Input:** Fill out your health information for personalized analysis.

- **Predictions:** Generate heart failure risk predictions based on your data.

- **Health Assistant Chatbot:** Get personalized guidance based on your inputs.

- **Model Insights:** View performance metrics, feature importance, and medical interpretations.
""")

st.sidebar.info("Select a page above to begin your heart failure risk analysis!")


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


