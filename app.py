import streamlit as st
import pandas as pd
import numpy as np


st.title("Hello I am Jyoti")


st.write("hello world")
df=pd.DataFrame({
    "first column":[1,2,3],
    "second column":[10,20,30]
})
st.write('here is the dtaframe')
st.write(df)
chart__data=pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.line_chart(chart__data)