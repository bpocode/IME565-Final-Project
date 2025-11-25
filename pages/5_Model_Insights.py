import streamlit as st
import pandas as pd
st.set_page_config(page_title = "Model Insights", 
                   page_icon = "🔎")

# Page title
st.markdown(
    """
    <h2 style="text-align: center; color: #4a4a4a;">Model Insights 🔎</h2>
    """,
    unsafe_allow_html=True,
)

model = st.selectbox(
        'Select Model',
        options = ['ADA Boost', 'Decision Tree', 'Random Forest','Soft Voting'],
    )

model_dict = {'ADA Boost': 'ada','Decision Tree':'dt','Random Forest':'rf','Soft Voting':'vote'}

st.subheader("Prediction Performance and Insights")
tab1, tab2, tab3 = st.tabs(["Confusion Matrix", "Classification Report","Feature Importance"])
with tab1:
    st.write("### Confusion Matrix")
    st.image('confusion_mat_' + model_dict[model] + '.svg')
with tab2:
    st.write("### Classification Report")
    cr = pd.read_csv('class_report_' + model_dict[model] + '.csv')
    st.dataframe(cr)
with tab3:
    st.write("### Feature Importance")
    st.image('feature_imp_' + model_dict[model] + '.svg')

with st.sidebar:
    st.header("📊 Page Guide")
    
    st.markdown("""
    **Explore 3 Key Metrics:**
    
    1. **Confusion Matrix**  
       Prediction accuracy breakdown
    
    2. **Classification Report**  
       Precision, Recall, F1-Score
    
    3. **Feature Importance**  
       Most influential health factors
    """)
    
    st.divider()
    
    st.success("Compare models to find the best performer!")