import streamlit as st
from PIL import Image
from io import BytesIO
import time
image_formats = ["jpg", "jpeg", "png", "avif", "blp", "bmp", "dds", "dib", "eps", "gif", "icns", "ico", "im", "tiff", "webp"]
images = st.file_uploader("Upload your images here.", type=image_formats, accept_multiple_files=True)
option = st.selectbox("Select the file format you want to convert your image into",
                      ("jpg", "jpeg", "webp", "png"),
                      index=None,
                      placeholder="Select desired file format..."
                      )

if st.button("🚀 convert now!"):
    with st.spinner("Processing..."):            
        for image in images:
            im = Image.open(image)
            buffer = BytesIO()
            im.save(buffer, format=option)
            img_bytes = buffer.getvalue()        
            st.image(img_bytes)
            st.download_button(
                label=f"download {option}",
                data=img_bytes,
                file_name=f"converted.{option}" 
            )
    st.success("Done! ✅")