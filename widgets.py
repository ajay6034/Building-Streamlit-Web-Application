import streamlit as st
import pandas as pd


st.title("Streamlit Text Input")

name=st.text_input("enter the name")

age= st.slider("Select your age:", 0,100,29)
# st.write(f"your age is: {age}")

options=["python","java","c","scala"]
choice= st.selectbox("choose your option:", options)
st.write(f"you selected {choice}.")

# create a simple data frame
data= pd.DataFrame({
    'Name':["ajay","sada","sivaram"],
    'age':[29,22,27]
})
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

## Creating Upload Button
upload=st.file_uploader("choose a file",type='csv')
if upload is not None:
    df=pd.read_csv(upload)
    st.write(df)



if name:
    st.write(f'Hello {name}, your age is: {age}')

