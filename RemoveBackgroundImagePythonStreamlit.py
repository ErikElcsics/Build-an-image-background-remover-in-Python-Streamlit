# Importing Required Modules
from rembg import remove
from PIL import Image
import streamlit as st
from io import BytesIO

# Title of the Streamlit app
st.title("Background Remover")

# Initialize session state for output_image if not already present
if 'output_image' not in st.session_state:
    st.session_state.output_image = None

# File uploader allows user to add their own image
uploaded_image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)

    if st.button("Remove Background"):
        with st.spinner('Removing Background...'):
            # Open the uploaded image
            pil_image = Image.open(uploaded_image)

            # Removing the background from the given Image
            st.session_state.output_image = remove(pil_image)

# Display the processed image and download button if output_image exists in session state
if st.session_state.output_image is not None:
    st.image(st.session_state.output_image, caption="Background Removed", use_container_width=True)

    # Convert the output image to bytes
    img_byte_arr = BytesIO()
    st.session_state.output_image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()

    # Provide a download button for the user to save the output image
    st.download_button(
        label="Download Image with Background Removed",
        data=img_byte_arr,
        file_name="background_removed.png",
        mime="image/png"
    )
