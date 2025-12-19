import gradio as gr
from utils.loader import load_model

model = load_model()

def webcam_detect(frame):
    results = model.predict(source=frame, conf=0.25, save=False)
    return results[0].plot()

def build(parent):
    # Thêm component trực tiếp vào parent, KhÔNG lồng 'with parent'
    webcam = gr.Video(sources="webcam", streaming=True, label="Webcam Feed")
    output = gr.Image(label="Detection Output")
    # Khi video frame được gửi, gọi hàm detect
    webcam.change(fn=webcam_detect, inputs=webcam, outputs=output)
