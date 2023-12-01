import streamlit as st

st.set_page_config(page_title="Models", page_icon=":tophat:")

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

st.markdown("# Models :tophat:")

st.write(
    """
    #### UNet
    The project uses [UNet](https://arxiv.org/pdf/1505.04597.pdf) which is a CNN that was developed for biomedical image segmentation at the Computer Science Department of the University of Freiburg. It consists of the repeated application of two 3x3 convolutions (unpadded convolutions), each followed by a rectified linear unit (ReLU) and a 2x2 max pooling operation with stride 2 for downsampling. Here is the architecture:"""
)

st.image("./assets/Unet.jpg",caption="UNet Architecture")

st.text("")

st.write("""
    App uses the same architecture with small modifications in the input size and convoluation padding. The input size is changed from 576 to 256 and the convolution padding is changed from "valid" to "same". The architecture is build using keras module provided by tensorflow.
    """)

st.write("""
    #### Why UNet?
    UNet's architecture resembles a "U" shape, with a contracting path on one side and an expansive path on the other. The contracting path captures context and reduces spatial resolution, while the expansive path recovers the spatial information. This design allows the network to combine both local and global information, which is crucial for semantic segmentation.
    """)

st.write("""
    UNet uses skip connections that connect the encoding (contracting) path to the decoding (expansive) path. These connections enable the network to retain high-resolution features from the early layers, aiding in precise localization. Skip connections also help in mitigating the vanishing gradient problem, allowing for better information flow during training. 
    """)

st.write("""
   #### Transfer Learning
   
   65 images are not enough to train such a model from scratch. Hence, to overcome this problem the app uses transfer learning using the library **[segmentation-models](https://github.com/qubvel/segmentation_models)**.
   
   Leveraging this library, the app imports pretrained weights for the encoder part of the network. The library supports multiple pretrained models, trained on large corpus of images. This app uses **resnet** architecture (trained on Imagenet dataset) for the encoding phase of the network, that involves reduction of the size of image and increase in the number of channels.      
    """)

st.write("""
#### Data Augmentation 

Since 65 images is not a good number for training, the code includes a preprocessing step where each image is randomly transformed using the following operations:

    - Rotation
    - Crop
    - Flip (right/left)
    - Flip (up/down)
    - Brightness
    - Contrast

Tensorflow provides functions to introduce randomness with respect to the above parameters. Here is the [document](https://www.tensorflow.org/api_docs/python/tf/image/random_crop) for it same.
    """)

st.write("Code for building the model is in this [colab notebook](https://colab.research.google.com/drive/1VZK_x1aFUtJYNPbwB5ZSTx0kYO952WDQ?usp=sharing) :book:")