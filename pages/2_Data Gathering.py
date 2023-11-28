import streamlit as st

st.set_page_config(page_title="Data Gathering", page_icon=":knife_fork_plate:")

# st.markdown(
#         """
#         <style>
#             [data-testid="stSidebarNav"]::before {
#                 content: "Color Pop";
#                 margin-left: 20px;
#                 margin-top: 20px;
#                 font-size: 30px;
#                 position: relative;
#                 top: 50px;
#                 bottom: 50px;
#             }
#         </style>
#         """,
#         unsafe_allow_html=True,
#     )

with st.sidebar:
        st.image('./assets/icon.jpg')
        st.title("Color Pop")
        st.subheader("Human segmentation application making color-pop effect easy to use!")

st.markdown("# Data Gathering :knife_fork_plate:")

st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)