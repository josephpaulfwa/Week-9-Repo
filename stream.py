import streamlit as st
import pandas as pd

st.title("Hi, I'm Joe!")
st.header("This is my first Streamlit app.")
st.subheader("Welcome to my Streamlit app.")
st.write("This is a simple app to demonstrate Streamlit capabilities.")
st.markdown("Hi ** How**`R` *u*")

df = pd.DataFrame({
    'Name': ["JOHN", "MIKE", "KING", "MIKE"],
    'Column 2': [60, 20, 30, 40]
})

st.dataframe(df)

st.divider()

st.image("itachi.jpg", caption="Itachi Uchiha")