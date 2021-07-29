import pytesseract
import streamlit as st
from PIL import Image
pytesseract.pytesseract.tesseract_cmd= '/app/.apt/usr/bin/tesseract'

st.title("IMAGE TO TEXT CONVERTER")
i= st.sidebar.file_uploader("Choose an image:")

if i is not None:
  st.image(i, caption= 'YOUR IMAGE')
  img= Image.open(i)
  if st.button('DETECT'):
    op= pytesseract.image_to_string(img)
    st.text("THE CONVERTED TEXT IS: ")
    st.write(op)
