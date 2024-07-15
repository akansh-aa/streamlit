import streamlit as st
import pandas as pd
st.title("streamlit text writer")
name=st.text_input("Enter your name")
if name:
    st.write(f"Hello, {name}")

age=st.slider("select your age",0,100,25)
st.write(f"Your age is,{age}")

options=["Python","Java","C","C++"]
choice=st.selectbox("Choose youre favourite language", options)
st.write(f"You choose", {choice})

data={
    "Name":["John","Alas","Tim","Neil"],
    "Age":[30,23,26,24],
    "City":["MP",'UP',"Delhi","UK"]

}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


file=st.file_uploader("Choose a cvs file",type="csv")
if file is not None:
    df=pd.read_csv(file)
    st.write(df)