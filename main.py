import streamlit as st
from PIL import Image, ImageDraw
import pytesseract
import os


pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR\tesseract.exe'



# Step 1: Upload number plate image button
st.title("Number Plate Recognition App")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")

if uploaded_file is not None:
    # Step 2: Display selected image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Step 3: Predict number plate and draw rectangle
    text = pytesseract.image_to_string(image)

    # draw = ImageDraw.Draw(image)
    # draw.rectangle([(10, 10), (100, 100)], outline="red", width=3)

    st.image(image, caption='Number Plate Detected.', use_column_width=True)

    # Display the recognized text
    st.write("Recognized Text:")
    st.write(text)
