import streamlit as st
import pickle
import time

st.title("Tweet Sentiment Analysis Model")

model = pickle.load(open('twitter_sentiment.pkl','rb'))

tweet = st.text_input("Enter your tweet")

submit = st.button('Predict')

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()

    st.write('Prediction time taken:',round(end-start,2),'seconds')
    print(prediction[0])
    st.write('Prediction Sentiment:',prediction[0])

