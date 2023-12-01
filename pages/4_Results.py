import streamlit as st

st.set_page_config(page_title="Results", page_icon=":bar_chart:")

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

st.markdown("# Results :bar_chart:")

st.write(
    """The model is trained for **50 epochs** with a custom loss function and with the metric Intersection over union"""
)

st.write(
    """
    #### Custom Loss Function
    
    The custom loss function is the combination of dice loss and focal loss.
    
    ##### Dice Loss
    
    It is particularly popular for tasks where the class of interest (foreground) occupies a small portion of the image, making it imbalanced. Since Dice coefficient considers both false positives and false negatives in its calculation, minimizing the Dice loss encourages the model to achieve a balance between precision and recall. This is important for segmentation tasks where both omission errors (missing true positives) and commission errors (false positives) need to be minimized. **Dice coefficient is 2 times The area of Overlap divided by the total number of pixels in both the images.**:
    """
)

c1,c2 = st.columns(2)

with c1:
    st.image("./assets/dice_loss.jpg",caption="Dice Loss")
with c2:
    st.image("./assets/focal_loss.png",caption="Focal Loss")
    
st.write("""
Focal loss applies a modulating term to the cross entropy loss in order to focus learning on hard misclassified examples.         
""")

st.write("""
#### Intersection over Union (IoU)

This is used as a performance metric for the app. IoU quantifies the overlap between the predicted segmentation and the ground truth. It provides a measure of how well the predicted region aligns with the true positive region. In segmentation tasks, accurately capturing the overlap is essential for assessing the quality of the segmentation. IoU is scale-invariant, meaning it is not sensitive to the absolute size of the segmented region. This property makes it suitable for segmentation tasks where the size of the objects of interest may vary.
""")
    
st.write("""     
#### Model Performance

Following are the metrics for loss and accuracy for training and validation sets over 50 epochs:
""")

c3,c4 = st.columns(2)
with c3:
    st.image("./assets/loss.jpg",caption="Dice+Focal Loss")
with c4:
    st.image("./assets/accuracy.jpg",caption="IoU")
    
st.write("""
#### Confusion Matrix        
""")

st.image('./assets/cm.png')