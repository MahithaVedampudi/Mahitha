import streamlit as st
import joblit

#load the joblit model
model_nb = joblib.load('spam-ham')
ip = st.text_input('Enter your text')

op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])
