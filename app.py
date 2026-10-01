import os
import streamlit as st
from PIL import Image, ImageOps, UnidentifiedImageError
from inference import predict, InferenceError

st.set_page_config(page_title='Animal Image Classifier', layout='centered')
st.title('Animal Image Classifier')
st.write('Upload an image to request a prediction from the configured Roboflow model.')
st.caption('A model may mislabel unfamiliar animals or non-animal images. Confidence is not proof that the label is correct.')
upload = st.file_uploader('Upload a JPG or PNG image', type=['jpg', 'jpeg', 'png'])
if upload:
    if upload.size > 10 * 1024 * 1024:
        st.error('Choose an image smaller than 10 MB.')
        st.stop()
    try:
        image = ImageOps.exif_transpose(Image.open(upload))
        image.load()
    except (UnidentifiedImageError, OSError, Image.DecompressionBombError):
        st.error('This file could not be read as a valid image.')
        st.stop()
    st.image(image, caption='Uploaded image', use_container_width=True)
    if st.button('Classify image', type='primary'):
        try:
            with st.spinner('Requesting prediction…'):
                predictions = predict(image, os.getenv('ROBOFLOW_API_KEY'), os.getenv('ROBOFLOW_PROJECT', 'animal-image-classifier'), os.getenv('ROBOFLOW_VERSION', '1'))
        except InferenceError as exc:
            st.error(str(exc))
        else:
            if not predictions:
                st.info('The model returned no detections for this image.')
            else:
                top = predictions[0]
                st.subheader('Highest-confidence model prediction')
                st.write(top['class'])
                st.write(f"Confidence: {top['confidence']:.1%}")
                st.progress(top['confidence'])
                st.dataframe(predictions, hide_index=True)
