import streamlit as st
from PIL import Image

st.title("AAA")
st.header("About Me")
image=Image.open(r"C:\Users\pjh60\Desktop\作业\PJH.png")
st.image(image,caption="My Picture",width=250)
# st.image("https://upload.wikimedia.org/wikipedia/commons/8/8d/Google_logo_%282010-2013%29.svg", width=150)

st.text("1。")
st.text("2。")
st.text("3。")

st.success("Welcome to my first Streamlit app!")