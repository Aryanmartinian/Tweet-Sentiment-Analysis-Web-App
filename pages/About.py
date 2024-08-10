#st.markdown('This application is all about tweet sentiment analysis of airlines.We can analyse reviews of the passengers using this streamlit application')
import streamlit as st
st.subheader('About Tweet Sentiment Analysis of Airlines')
st.markdown("""Welcome to the Tweet Sentiment Analysis of Airlines web application! 
            This tool is designed to provide valuable insights into public sentiment about airlines by analyzing tweets. 
            It leverages the power of machine learning and data visualization to offer both sentiment predictions and comprehensive data analysis.""")

st.subheader("Purpose")
st.markdown("""The primary goal of this application is to help users understand the general sentiment towards various airlines as expressed on Twitter. 
            By examining both historical and current tweets, users can gain insights into how airlines are perceived by the public, identify emerging trends, 
            and make informed decisions based on data-driven analysis.""")

st.subheader('Libraries and Tools Used')
st.markdown("1. **Streamlit** - The web framework for building a responsive and interactive user interface.\n" 
             "2. **Pandas** - Used for data manipulation and preprocessing, including loading and transforming datasets.\n "
             "3. **Matplotlib & Plotly** - Create static and interactive visualizations, enhancing data exploration.\n"
             "4. **NumPy** - Facilitate numerical operations and efficient data handling for model training and analysis.\n"
             "5. **Scikit-learn** -  Provide machine learning capabilities, including model training, evaluation, and feature extraction.\n"
             "6. **spaCy** - Perform advanced natural language processing tasks like tokenization and part-of-speech tagging.\n")

