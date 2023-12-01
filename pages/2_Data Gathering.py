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
    """**65 Personal images** of people is the dataset used to train the image segmentation model. Images are chosen in such a fashion that ensures that each image has one or more human figures to segment."""
)

st.write(
    """
    Apart from original images, their masks are required to train the model. Mask is like a label for a image data. A mask is essentially a binary map where each pixel is assigned a value to indicate whether it belongs to a particular segment or object. The two common values are 0 and 1, where 0 typically represents the background or areas outside the object, and 1 represents the foreground or the object itself. That is why, image segmentation is often referred as pixel-wise classification, where each pixel of the image is assigned a class, and then compared with the actual class present in the form of mask. Let's see an example image and its corresponding mask:
    """
)
st.text("")
c1,c2 = st.columns(2)

with c1:
    st.image("./assets/normal.jpg",caption="Original Image")
    
with c2:
    st.image("./assets/mask.jpg",caption="Mask")
   
st.write("""
         #### LabelBox
         
         This is the software used to generate masks for the training images. It is an easy to use tool, with an inbuilt feature of human segmentation. See this [Labelbox tutorial](https://labelbox.com/guides/image-segmentation/) for more information.
         
         Afterwards, the masks are downloaded from Labelbox in form of a ndjson file. This file contains the information about the masks. To decode this json file, here is the code:
         
         """)

code= '''
import urllib.request
from PIL import Image
import labelbox as lb
import json

API_KEY = "key"
client = lb.Client(api_key=API_KEY)

with open(r'result.ndjson', 'r') as ndjson_file:
    # Process each line in the file
    for line in ndjson_file:
        # Deserialize the JSON object on each line
        data = json.loads(line)

        # Now 'data' contains the Python dictionary representation of each JSON object in the NDJSON file
        # You can work with 'data' as a regular Python dictionary
        image_name = data['data_row']['external_id']
        project_id = list(data['projects'].keys())[0]
        mask_url = data['projects'][project_id]['labels'][0]['annotations']['objects']
        req = urllib.request.Request(mask_url, headers=client.headers)
        image = Image.open(urllib.request.urlopen(req))
        image.save("./temp/masks/"+image_name)

'''

st.code(code,line_numbers=True)

st.write("""
         #### Data Resizing
         
         To feed images and masks into Unet, they need to be resized into 256x256 pixels. This is how an image looks like before and after resizing:
         """)

c1,c2= st.columns(2)

with c1:
    st.image("./assets/size_image.JPG",caption="Before Resizing")
with c2:
    st.image("./assets/resized_image.jpg",caption= "After Resizing")
    
st.write("""
         #### Mask Thresholding
         
         As discussed earlier, masks in low-level represents the a class. Here, there are just two classes, first is human object **(class=1)** and the background **(class=0)**. Pixels of original masks produced by Labelbox ranged between 0 to 255. However, we want these pixels to be either 1 or 0. To accomodate the same, pixels having a value less than 127 were set as 0 and the rest 1. This will make the mask look more edgy and coarse. This is how mask looks like after this operation:
         """)

c3,c4= st.columns(2)
with c3:
    st.image("./assets/resized_mask.jpg",caption="Original Mask")
with c4:
    st.image("./assets/resized_mask_thresholded.jpg",caption= "After Thresholding")
    
st.write("Code for preprocessing can be found in this [colab notebook](https://colab.research.google.com/drive/1VZK_x1aFUtJYNPbwB5ZSTx0kYO952WDQ?usp=sharing) :book:")