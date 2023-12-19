import streamlit as st
from PIL import Image
import numpy as np
import cv2
from imageOps import image_info, grey, resize, get_image_download_link



st.markdown('<h2>My Image App</h2>', unsafe_allow_html=True)

# uploading image in side bar
uploaded_file = st.sidebar.file_uploader("Choose an image...", type="jpg")

# if image is uploaded  then show image
if uploaded_file is not None:
    # print(type(uploaded_file))
    # print(uploaded_file)
    image = Image.open(uploaded_file)
    image = np.array(image)
    # print(type(image))
    # print(image)
    st.sidebar.image(image, caption='Uploaded Image.', use_column_width=True)
else:
    st.write("Please upload an image file")

# creating a list of operations can be done with opencv
options = ["Show Image Information", "Grey Image", "Resize Image"]
# putting the options in selectbox sidebar
choice = st.sidebar.selectbox("Choose Operation", options)
# print(choice)
if uploaded_file is not None:
    if choice == "Show Image Information":
        # calling the function from imageOps.py
        size, width, height, channels = image_info(image)
        col1, col2, col3, col4 = st.columns(4)

        col1.write(f"Size of Image: {size}")
        col2.write(f"Width of Image: {width}" )
        col3.write(f"Height of Image: {height}" )
        col4.write(f"Channels of Image: {channels}")
        st.image(image, caption='Uploaded Image.', use_column_width=True)
    elif choice == "Grey Image":
        # calling the function from imageOps.py
        grey_img = grey(image)
        st.image(grey_img, caption='Grey Image.', use_column_width=True)
        st.markdown(get_image_download_link(grey_img), unsafe_allow_html=True)

    elif choice == "Resize Image":
        # calling the function from imageOps.py
        width = st.slider("Width", 100, 1000)
        height = st.slider("Height", 100, 1000)
        resized_img = resize(image, width, height)
        st.image(resized_img, caption='Resized Image.', use_column_width=True)
        st.markdown(get_image_download_link(resized_img), unsafe_allow_html=True)
