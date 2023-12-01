import streamlit as st

st.set_page_config(
    page_title="Color Pop",
    page_icon="random"
)

st.markdown(
    """
    <style>
    .st-emotion-cache-mcjgwn {padding-top:5px; margin-top:5px;}
    </style>
    """,
    unsafe_allow_html=True
)

with st.sidebar:
        st.image('./assets/icon.jpg')
        st.title("Color Pop")
        st.subheader("Human segmentation application making color-pop effect easy to use!")

st.write("# Welcome to Color Pop! :camera_with_flash:")
st.text("")
st.markdown(
    """

    ##### Color Pop is an image editing tool that edits your images in such a way that all the objects apart from humans are gray-scaled. 
     
    This tool is built upon UNet trained on a small number of images. The final effect on images will like the image on the left 👈
    
    **Navigate through the project from the sidebar** to see how was it built and select "App" to try it! :carousel_horse:
"""
)