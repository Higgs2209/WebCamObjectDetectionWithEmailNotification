import cv2
import streamlit as st
from datetime import datetime
import textwrap

from numpy.compat import unicode

st.title("Motion Detector")
start = st.button("Start Camera")

date = datetime.now()
#time = unicode(date.replace(microsecond=0))

day_of_week = date.strftime("%A")
time = date.strftime("%H:%M:%S")


if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame, = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=f"{day_of_week}", org=(20, 50),
                   fontFace=cv2.FONT_ITALIC, fontScale=1.5, color=(20, 100 , 200),
                   thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=f"{time}", org=(20, 100),
                    fontFace=cv2.FONT_ITALIC, fontScale=1, color=(20, 100, 200),
                    thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

