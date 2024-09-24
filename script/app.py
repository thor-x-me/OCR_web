import cv2
import uuid
import numpy as np
from PIL import Image
import streamlit as st
from GeminiVision import getResponseFromImage

# Title of the app
st.title("OCR Application")

# Create file uploader for image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

# Create a text input box
user_input = st.text_input("Enter some text")

# Check if a file has been uploaded
if uploaded_file is not None and user_input:
    # Open the image file using PIL
    img = Image.open(uploaded_file)

    # Converting to openCV compatible file and saving in images folder
    cv_image = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    file_name = f"{uuid.uuid4()}.jpg"
    file_path = "../images/" + file_name
    cv2.imwrite(file_path, cv_image)

    # Getting the response
    response = getResponseFromImage(file_path, user_input)

    # Display the response
    st.write(response)

    # Display the image on the Streamlit app
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    # Display some additional details about the image
    st.write(f"Image size: {img.size}")
    st.write(f"Image mode: {img.mode}")


