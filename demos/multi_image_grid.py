import gradio as gr
from utils.loader import load_model
from PIL import Image
import cv2

model = load_model()

def multi_image_detect(files):
    outputs = []
    for f in files:
        result = model.predict(source=f.name, conf=0.25, save=False)
        img = result[0].plot()  # numpy array BGR
        # Chuyển sang RGB
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        outputs.append(Image.fromarray(img_rgb))
    return outputs

def build(parent):
    # gr.Files cho nhiều ảnh
    imgs_input = gr.Files(
        label="Upload Images",
        file_types=[".jpg", ".png"]
    )

    # gr.Gallery: dùng `columns` thay cho `grid` và `height` trực tiếp
    imgs_output = gr.Gallery(
        label="Detection Output",
        show_label=True,
        elem_id="gallery",
        columns=2,        # thay cho grid=[2]
        height="auto"     # chiều cao tự động
    )

    imgs_input.change(fn=multi_image_detect, inputs=imgs_input, outputs=imgs_output)
