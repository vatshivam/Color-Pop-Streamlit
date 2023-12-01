import streamlit as st

st.set_page_config(page_title="Conclusion", page_icon=":feather:")

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

st.markdown("# Conclusion :feather:")

st.write("""
Digital Image processing products such as Color Pop are gaining traction in industry. So an organization should be encouraged to develop solutions like these given that open source deep learning technology is getting even more accessible. Even though there are pretrained models present in the industry, building your own that is trained on a custom dataset is not a cakewalk. Various complexities are involved to build such a solution. For instance, the size of the dataset, the accuracy of the masks, data augmentation techniques or the computational power avaiable in hand intertwine with each other to decide the quiality of solution. 
"""
)

st.write("""
Out of the these factors, amount of data and the computational power plays a critical role. This project, due to the limited computational resources only runs a limited number of iterations of training on a very small dataset. The dataset after augmentation had around 3000 data points to train on which is not enought to build a state pf the art machine. Due to this fact, the current model works poorly on unseen data and has an accuracy of even less than 50%. Given this fact, the model is no way near to be used at a industry level. However, one shouldn't ignore similar opensource technology that can serve the purpose of color pop effect in a similar fashion. 
""")


st.write("""
One such technology is Image Matting. Image matting involves separating the foreground object from the background and capturing the soft transitions or semi-transparent regions at the object's boundary. Image matting is commonly used in tasks like image editing, where precise separation of foreground and background is needed, especially when the edges are not well-defined. This process can be extrapolated to obtain image boundaries, similar to what we saw in image segmentation. [MODNet](https://github.com/ZHKKKe/MODNet) is a state of the art image matting solution that could be considered as an alternate for color-pop. Given a scenario where an organization do not have the computational and scitific resoruces to develop their own model, open source solution like this could be used to obtain color pop effect.         
""")
st.text("")

c1,c2,c3=st.columns([0.2,0.97,0.1])
with c2:
    st.image("./assets/matting_vs_seg.png",caption="Image matting vs Image Segmentation")

st.write("""
All these obstacles shouldn't slow down or discourage organizations from developing such products. Many big players such as Amazon, Meta and Apple are actively developing image processing softwares and using them in their softwares. This is due to the fact that features like these are artistic, eye-catchy and attention seeking. Whatever catches human attention has the potential to generate revenue and profits. According to [Adroit Market research](https://www.adroitmarketresearch.com/industry-reports/video-editing-software-market), the global video editing software market size is expected to reach close to USD 3245 million by 2029 with an annualized growth rate of 5.6% through the projected period.
""")
st.text("")

c1,c2,c3=st.columns([0.05,0.99,0.05])
with c2:
    st.image('./assets/stat.jpg')

st.text("")
st.write("""
Despite the availability of pretrained models, building custom solutions presents challenges, such as dataset size, mask accuracy, data augmentation techniques, and computational power. The limited computational resources in a specific project allowed only a few iterations on a small dataset of around 3000 points, resulting in a model with poor performance on unseen data (accuracy < 50%). While the current model may not be industry-ready, alternative open-source technologies like Image Matting, exemplified by MODNet, offer potential solutions for effects like Color Pop.

##### Don't forget to try the app! 
###### Click on "App" in sidebar on your left 👈
""")