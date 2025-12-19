import gradio as gr
from demos import realtime_webcam, video_inference, multi_image_grid, tracking_demo

with gr.Blocks() as demo: 
    gr.Markdown("## YOLOv8 Interactive Demo", elem_id="title")

    with gr.Tabs():
        with gr.Tab("Realtime Webcam"):
            realtime_webcam.build(demo)

        with gr.Tab("Video Inference"):
            video_inference.build(demo)

        with gr.Tab("Multi Image Grid"):
            multi_image_grid.build(demo)

        with gr.Tab("Tracking Demo"):
            tracking_demo.build(demo)

demo.launch()
