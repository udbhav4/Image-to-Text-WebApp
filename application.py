import pytesseract
import streamlit as st
from PIL import Image
import cv2

st.title("IMAGE TO TEXT CONVERTER")
i= st.sidebar.file_uploader("Choose an image:")  #'sidebar' moves our browzer to the left side of the website page.

if i is not None:    #Need to write 'if' since streamlit works in loops and until it receives the image we have uploaded, it will show an error saying no image found.
  st.image(i, caption= 'YOUR IMAGE') #displaying image.
  img= Image.open(i) #reading image so as to be able to use it.
  if st.button('DETECT'):    #this if creates the button 'DETECT' and shows the required output only if that button is pressed.
    op= pytesseract.image_to_string(img)
    st.text("THE CONVERTED TEXT IS: ")
    st.write(op)
