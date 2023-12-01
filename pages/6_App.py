import streamlit as st
import tensorflow as tf
import numpy as np
from keras.models import load_model
from patchify import patchify, unpatchify
from sklearn.preprocessing import MinMaxScaler
import cv2 as cv
from PIL import Image
from stqdm import stqdm
import warnings
from inference import get_mask
import io
warnings.filterwarnings("ignore")

@st.cache_data(show_spinner=False)
def predict_custom(_model,image):
        # st.write(_image_name)
        # image = cv.imread(_image_name)
        progress_bar = st.progress(0)
        patch_size = 256
        SIZE_X = (image.shape[1]//patch_size)*patch_size 
        SIZE_Y = (image.shape[0]//patch_size)*patch_size
        
        large_img = Image.fromarray(image)
        large_img = large_img.crop((0 ,0, SIZE_X, SIZE_Y))
        large_img = np.array(large_img)
        
        patches_img = patchify(large_img, (patch_size, patch_size, 3), step=patch_size)  #Step=256 for 256 patches means no overlap
        patches_img = patches_img[:,:,0,:,:,:]
        
        scaler = MinMaxScaler()
        patched_prediction = []
        
        step_ratio = 1/(patches_img.shape[0]*patches_img.shape[1])
        progress = 0
        count = 0
        for i in range(patches_img.shape[0]):
            for j in range(patches_img.shape[1]):
                count+=1
                single_patch_img = patches_img[i,j,:,:,:]
                single_patch_img = scaler.fit_transform(single_patch_img.reshape(-1, single_patch_img.shape[-1])).reshape(single_patch_img.shape)
                single_patch_img = np.expand_dims(single_patch_img, axis=0)
                pred = model.serve(single_patch_img)
                pred = pred[0, :,:]
                patched_prediction.append(pred)
                progress_bar.progress(progress)
                progress = progress + step_ratio                
                
        patched_prediction = np.array(patched_prediction)
        patched_prediction = np.reshape(patched_prediction, [patches_img.shape[0], patches_img.shape[1], 
                                                patches_img.shape[2], patches_img.shape[3]])
        unpatched_prediction = unpatchify(patched_prediction, (large_img.shape[0], large_img.shape[1]))
        unpatched_prediction = unpatched_prediction.astype(int)
        
        background = np.where(unpatched_prediction < 1)
        bnw = np.mean(large_img[background[0], background[1],:],axis=1)
        fill = np.tile(bnw[:, np.newaxis], (1, 3))
        large_img[background[0],background[1],:] = fill
        progress_bar.empty()
        return large_img

@st.cache_data(show_spinner=False)
def predict_modnet(image):
    mask = get_mask(image,  ckpt_path = "./models/modnet_photographic_portrait_matting.ckpt")
    large_img = np.array(image)
    res = np.where(mask < 1)
    mean_values = np.mean(large_img[res[0], res[1],:],axis=1)
    fill = np.tile(mean_values[:, np.newaxis], (1, 3))
    large_img[res[0],res[1],:] = fill
    # large_img = cv.cvtColor(large_img, cv.COLOR_BGR2RGB)
    return large_img

# st.set_option('deprecation.showfileUploaderEncoding', False)
# @st.cache_resource(show_spinner=False)
# def load_segmentation_model():
#     model = tf.saved_model.load("./models/model 2023-11-27 06_03")
#     return model

def change_button_state():
    st.session_state.execute = True

if 'execute' not in st.session_state:
    st.session_state['execute'] = False

st.set_page_config(
    page_title="Color Pop",
    page_icon = "random",
    initial_sidebar_state = 'auto'
)
hide_streamlit_style = """
            <style>
            .st-emotion-cache-1y4p8pa, st-emotion-cache-1on073z, st-emotion-cache-1on073z {display: flex;}
            .st-emotion-cache-uf99v8 {margin_left: 0px;}
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


with st.sidebar:
        st.image('./assets/icon.jpg')
        st.title("Color Pop")
        st.subheader("Human segmentation application making color-pop effect easy to use!")

# with st.spinner('Model is being loaded..'):
#     model=load_segmentation_model()

st.write("""
         ### Get Color Pop effect on your favorite pictures!
         """
         )
c1,c2 = st.columns([0.7,0.3])
with c1:
    file = st.file_uploader("", type=["jpg", "png","jpeg"])
with c2:
    selected_model = st.selectbox("Choose Model", ("MODNet", "Shivam's"),label_visibility='hidden',index=0)

left, center, right = st.columns([0.45,0.1,0.45])

with center:
    button = st.button("PoP",on_click=change_button_state,type='primary')
    
if file is None:
    pass
else:
    image_bytes = np.asarray(bytearray(file.read()),dtype=np.uint8)
    opencv_image = cv.imdecode(image_bytes, 1)
    opencv_image = cv.cvtColor(opencv_image, cv.COLOR_BGR2RGB)
    
    with left:
        st.image(opencv_image, use_column_width=True)
    
    output_image = None
    if st.session_state.execute:
        # if selected_model == "Shivam's":
        #     output_image = predict_custom(model,opencv_image)
        # else:
        output_image = predict_modnet(opencv_image)
        with right:
            st.image(output_image,use_column_width=True)
            output_image = cv.cvtColor(output_image, cv.COLOR_BGR2RGB)
            is_success, im_buf_arr = cv.imencode(".jpg", output_image)
            output = im_buf_arr.tobytes()
            st.download_button("Download Image", output,file_name="pop.jpg")
        st.snow()