import streamlit as st

st.set_page_config(page_title="Introduction", page_icon=":dart:")

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

st.markdown("# Introduction :dart:")

st.write(
    """Color Pop Effects gives your photos a dramatic look by converting it to black and white while keeping selected areas colorful. """
)
st.text("")
c1,c2 = st.columns(2)
with c1:
    st.image('./assets/normal.jpg', caption="Sample Image")
with c2:
    st.image('./assets/pop.jpg',caption="Human object colored and rest of the background is in gray-scale")
    
st.text("")

st.write(
    """
    Color Pop effect has been gaining popularity within the digital image industry, especially after COVID pandemic. Due to the COVID-19 pandemic, the global Photo Editing Software market size is estimated to be worth **932** million USD in 2021 and is forecast to a readjusted size of USD **1307.9** million by 2028 with a CAGR of 4.9% during the forecast period 2022-2028. The market in North America is expected to grow considerably during the forecast period. The high adoption of advanced technology and the presence of large players in this region are likely to create ample growth opportunities for the market. Given the potential of this industry, developing state of the art image editing applications will potentially gain attention of even more companies and generate handsome revenue.
    """
)

st.write("""
    To appreciate the beauty of this technology, let's gain some understanding about the principle behind this application, that is Image segmentation. Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images. Segmentation are of mulitple types depending upon the context of application. If image segmentation is used to mark roads, pavements, then it is termed as lane segmentation. If it is used to distinguish between different objects of same kind, for example, marking multiple humans in a picture is termed as instance segmentation. As the name suggests, marking each instance of a single type of object in an image.
         """)

st.text("")
st.image('./assets/segmentation.jpg',caption="Semenatic Segmentation")

st.write("""
    Progress in a image segmentation technology bears fruit not only in digital image processing domain, but in other domains as well. For instance, the deep learning model Unet that is used in this project is widely used in organ instance segmentation. Other semantic segmentation models are used across applications. In autonomous vehicles, segmentation is essential for detecting and identifying objects on the road, such as pedestrians, vehicles, and road signs, enabling safer navigation for autonomous vehicles. Segmentation can be used to classify different types of land cover in satellite images, providing valuable information for environmental monitoring, urban planning, and agriculture. : Segmentation is crucial for recognizing and tracking objects in real-time, enhancing the augmented reality experience by overlaying digital information onto the real world.
         """)

st.write("""
         You might be thinking that why should you care about the advancement of image segmentation in domains other than digital imaging. Consider an example of self driven cars, which is one of the biggest domain where image segmenatation is heavily used. Autonomous cars market is expected to generate a revenue of USD 15.55 Billion by 2030, Globally, at 31.19% CAGR. This is not only generating huge revenue, but accelerating the steps to reduce the fossil feul consumptions, and finally leaving an everlasting impact on the carbon emmissions. Decreased carbon emissions will play a major role in reducing the levels of abrupt changes in temperature and rise in sea levels.
         """)

st.write("""
         Color pop will surely be a game changer in  the digital imaging market given the rate with which the industry is growing and the speed with which image editing tools are gaining traction in social media. Developing accessible and lightweight applications like this is a decent step towards this evolution. Apart from that, image segmentation can contribute to various aspects of business, including marketing, customer experience, product development, and quality control. The ability to extract meaningful information from visual data can result in better decision-making and potentially increased revenue for businesses across different sectors.
         """)