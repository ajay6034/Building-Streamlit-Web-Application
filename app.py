import streamlit as st
import pandas as pd
import numpy as np

##Title of the application
st.title("Hello Streamlit")

## DIsplay simple Text
st.write("This is a simple text")

## create a simple data frame
df= pd.DataFrame({
    'first column':[1,2,3],
    'second column':[4,5,6]
})

## Display the data frame
st.write("Hello this is the Data Frame")
st.write(df)

## create a line chart
chart_data=pd.DataFrame(
    np.random.rand(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)