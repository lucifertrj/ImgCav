import streamlit as st
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img,img_to_array
from tensorflow.keras.applications import inception_v3

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = np.array(img)
    img = np.expand_dims(img,axis=0)
    img = inception_v3.preprocess_input(img)
    return img

def imageCap(img):
    pass


st.title("ImgCaV")
st.header("Play Around with Images")

custom_image = st.file_uploader(label="Try your custom Image",accept_multiple_files=False)
value = st.slider(label="Adjust Image Brightness",min_value=-0.5,max_value=0.8,step=0.2)

if custom_image:
    image = preprocess_image(custom_image.name)
else:
    image = preprocess_image("20545155.jpg")

image = image[0]+value
fig , ax = plt.subplots(1,1)

ax.axis("off")
ax.imshow(image)
fig.savefig(f"img_{value}.png",transparent=True)
sample_img = st.image(f"img_{value}.png")

st.markdown("## Our Image Services")
genre = st.radio("What could you like to try?",('Image Captioning', "Deep Dream"))

st.markdown(f"### {genre}")
if genre == "Image Captioning":
    img = st.file_uploader("Choose an Image, we will provide a caption")
    imageCap(img)
    
elif genre == "Deep Dream":
    st.markdown("#### Before")
    st.image("20545155.jpg")
    st.markdown("#### After")
    st.image("anime.png")