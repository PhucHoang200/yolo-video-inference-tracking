import gradio as gr
from utils.loader import load_model
import glob
import os
import subprocess

model = load_model()

def tracking_video(video_file):

    results = model.track(
        source=video_file.name,
        conf=0.25,
        save=True,
        persist=True,
        project="runs/track",
        name="exp",
        exist_ok=True
    )

    # Tìm file .mp4
    saved_videos = glob.glob("runs/track/exp/*.mp4")

    # Nếu chỉ có .avi → convert sang .mp4
    if not saved_videos:
        avi_files = glob.glob("runs/track/exp/*.avi")
        if not avi_files:
            return None

        avi_file = avi_files[0]
        mp4_path = avi_file.replace(".avi", ".mp4")

        subprocess.call([
            "ffmpeg", "-y", "-i", avi_file, "-c:v", "libx264", "-preset", "fast", mp4_path
        ])

        saved_videos = [mp4_path]

    latest_video = max(saved_videos, key=os.path.getctime)
    return latest_video

def build(parent):
    video_input = gr.File(label="Upload Video for Tracking", file_types=[".mp4", ".avi"])
    video_output = gr.Video(label="Tracking Result")
    video_input.change(fn=tracking_video, inputs=video_input, outputs=video_output)
