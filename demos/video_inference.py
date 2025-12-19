import gradio as gr
from utils.loader import load_model
import glob
import os
import shutil
import subprocess

model = load_model()

def video_detect(video_file):
    temp_dir = "temp_video_output"
    os.makedirs(temp_dir, exist_ok=True)

    # Chạy predict và ép YOLO lưu vào thư mục cố định
    results = model.predict(
        source=video_file.name,
        conf=0.25,
        save=True,
        project="runs/detect",
        name="exp",
        exist_ok=True
    )

    # Tìm file video .mp4
    saved_videos = glob.glob("runs/detect/exp/*.mp4")
    
    # Trường hợp YOLO lưu .avi → convert sang .mp4
    if not saved_videos:
        avi_files = glob.glob("runs/detect/exp/*.avi")
        if not avi_files:
            return None

        avi_file = avi_files[0]
        mp4_path = avi_file.replace(".avi", ".mp4")

        # Convert avi → mp4 bằng ffmpeg
        subprocess.call([
            "ffmpeg", "-y", "-i", avi_file, "-c:v", "libx264", "-preset", "fast", mp4_path
        ])

        saved_videos = [mp4_path]

    latest_video = max(saved_videos, key=os.path.getctime)
    dest_path = os.path.join(temp_dir, os.path.basename(latest_video))

    shutil.copy(latest_video, dest_path)
    return dest_path

def build(parent):
    video_input = gr.File(label="Upload Video", file_types=[".mp4", ".avi"])
    video_output = gr.Video(label="Result Video")
    video_input.change(fn=video_detect, inputs=video_input, outputs=video_output)
