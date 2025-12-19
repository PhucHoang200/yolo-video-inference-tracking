import cv2
from ultralytics.yolo.utils.plotting import Annotator

def plot_yolo_result(img_path, results):
    img = cv2.imread(img_path)
    annotator = Annotator(img)
    for box in results[0].boxes:
        xyxy = box.xyxy[0].cpu().numpy()
        cls = int(box.cls[0].cpu().numpy())
        conf = float(box.conf[0].cpu().numpy())
        label = f"{cls}: {conf:.2f}"
        annotator.box_label(xyxy, label)
    return annotator.result()
