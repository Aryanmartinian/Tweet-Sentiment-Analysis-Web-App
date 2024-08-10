# Main file--
# from PIL import Image
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
#from PIL import Image

st.title('Tweet Sentiment Analysis')
#image= Image.open("Twitter sentiment analysis.png")
#st.image(image, caption='Sunrise by the mountains')
#img_contact_form = Image.open("images/Twitter sentiment analysis.png")
#with st.container():
 #   image_column,text_column = st.columns((1,2))
  #  with image_column:
   #     st.image(img_contact_form)"""
        


st.sidebar.title(" Tweet Sentiment Analysis Of Airlines")
st.sidebar.markdown("We can analyse passengers review from this application.")
data=pd.read_csv('data/tweet-checkpoint (1).csv')

if st.checkbox("Show Data"):
    st.write(data.head(50))

st.sidebar.subheader('Tweets Analyser')
tweets = st.sidebar.radio('Sentiment Type',('positive','negative','neutral'))
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
st.write(data.query('airline_sentiment==@tweets')[['text']].sample(1).iat[0,0])
# a select box has different key numbers- if you want to make another select box that has different key number.
select = st.sidebar.selectbox('Visualisation of Tweets',['Histogram','Pie Chart'],key=1)
sentiment =data['airline_sentiment'].value_counts()
sentiment=pd.DataFrame({'Sentiment':sentiment.index,'Tweets':sentiment.values})
st.markdown("###  Sentiment count")
if select=="Histogram":
    fig = px.bar(sentiment,x='Sentiment',y='Tweets',color='Tweets',height=500)
    st.plotly_chart(fig)
else:
    fig = px.pie(sentiment,values='Tweets',names='Sentiment')
    st.plotly_chart(fig)
#Now we will make a slider which will tell us the time and location of the tweets-->
st.sidebar.markdown('Time & Location of tweets')
hr = st.sidebar.slider("Hour of the day",0,23)
data['Date'] = pd.to_datetime(data['tweet_created'])
hr_data = data[data['Date'].dt.hour==hr]
if not st.sidebar.checkbox("Hide",True,key='2'):
    st.markdown("### Location of the tweets based on the hour of the day")
    st.markdown("%i tweets during %i:00 and %i:00" %(len(hr_data),hr,(hr+1)%24))
    st.map(hr_data)


st.sidebar.markdown("Airline tweets by sentiment")
choice = st.sidebar.multiselect("Airlines",('US Airways','United','American','Southwest','Delta','Virgin America'),key='0')
if len(choice)>0:
    air_data=data[data.airline.isin(choice)]
    fig1 = px.histogram(air_data,x='airline',y='airline_sentiment',histfunc='count',color='airline_sentiment',labels={'airline_sentiment'})
    st.plotly_chart(fig1)