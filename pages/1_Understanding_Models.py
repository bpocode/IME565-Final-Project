import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Understanding Models", page_icon = "🧠")

# Title and description #AI used for HTML
st.markdown(
    """
    <h2 style="text-align: center; color: #69503c;">Understanding Models 🧠</h2>
    </p>
    """,
    unsafe_allow_html = True
)


st.markdown(
    """
    Compare the available machine learning models for predicting heart failure risk and choose the best one for your needs.
    """
)

st.markdown("## About the Models")

# ---- MODEL ACCORDIONS ----
with st.expander("Decision Tree"):
    st.markdown("""
    - A simple, interpretable model that splits data into branches based on features.
    - Works well with small datasets and is easy to visualize.
    - **Why use it?** When interpretability and simplicity are more important than accuracy.
    """)

with st.expander("Random Forest"):
    st.markdown("""
    - Combines multiple decision trees to improve accuracy and reduce overfitting.
    - Handles large datasets effectively and provides feature importance.
    - **Why use it?** When you need a balance of accuracy and generalization.
    """)

with st.expander("AdaBoost"):
    st.markdown("""
    - A boosting technique that builds models iteratively, focusing on difficult-to-predict samples.
    - Improves performance for imbalanced datasets.
    - **Why use it?** When your data has significant class imbalances or needs better handling of misclassifications.
    """)

with st.expander("Soft Voting Classifier"):
    st.markdown("""
    - Combines predictions from multiple models (Decision Tree, Random Forest, AdaBoost) by averaging their probabilities.
    - Often achieves better performance than any single model.
    - **Why use it?** When you want the strengths of multiple models and can trade interpretability for accuracy.
    """)

# ---- CHOOSING THE RIGHT MODEL ----
st.markdown("## Choosing the Right Model")

st.markdown(
    """
    - **Decision Tree** → Use for fast, interpretable results.  
    - **Random Forest** → Best for strong accuracy and generalization.  
    - **AdaBoost** → Ideal for imbalanced data or when misclassification is costly.  
    - **Soft Voting Classifier** → Maximizes overall performance by combining multiple models.  
    """
)

st.caption("Explore the models and select the one that aligns with your project goals!")

with st.sidebar:
    st.header("📚 Quick Guide")
    
    st.markdown("""
    **Models Available:**
    - 🌳 Decision Tree → Interpretable
    - 🌲 Random Forest → Accurate  
    - 🚀 AdaBoost → Imbalanced data
    - 🗳️ Soft Voting → Best overall
    
    **Learn about:** strengths, limitations, and when to use each model
    """)
    
    st.info("💡 Choose based on accuracy vs. interpretability")