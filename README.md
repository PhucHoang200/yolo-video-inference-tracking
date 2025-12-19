# 🚀 Demo YOLO Nhận Diện & Tracking Video (Giao Diện Gradio)

Dự án này cung cấp một demo trực quan cho **nhận diện đối tượng (object detection)** và **theo dõi đối tượng (object tracking)** trên video bằng **Ultralytics YOLO** (YOLOv8/YOLO11), kết hợp giao diện người dùng bằng **Gradio**.

Dự án được thiết kế với mục tiêu:

* Chạy detection trên video (vẽ bounding box + label + confidence)
* Chạy tracking với ID bám theo đối tượng
* Trả video kết quả ngay trên Gradio
* Tách cấu trúc code gọn gàng, dễ mở rộng, dùng được cho demo hoặc sản phẩm nhỏ

---

## 📦 Tính năng chính

### 🔹 Nhận diện đối tượng trên video (Video Inference)

* Hỗ trợ upload video `.mp4`, `.avi`
* YOLO tự động vẽ:

  * Bounding box
  * Tên lớp
  * Tỉ lệ confidence
* Video kết quả hiển thị ngay trong Gradio UI

### 🔹 Theo dõi đối tượng (Object Tracking)

* Hỗ trợ tracking bằng cơ chế YOLO + ByteTrack/BOTSORT
* Gán **ID duy nhất** cho mỗi đối tượng
* ID duy trì dù đối tượng di chuyển trong nhiều frame
* Tự động lưu video output và trả về video mới nhất

### 🔹 Tổ chức code chuyên nghiệp

* Module load model riêng (`utils/loader.py`)
* Mỗi demo tách thành file riêng (`/demos`)
* `app.py` clean, dễ mở rộng các tab/chức năng khác

---

## 🗂️ Cấu trúc thư mục

```
📦 your-project/
│
├── app.py                     # Khởi chạy Gradio UI
├── utils/
│   └── loader.py              # Load mô hình YOLO
│
├── demos/
│   ├── video_inference.py     # Demo nhận diện video
│   └── tracking_demo.py       # Demo tracking
│
├── README.md                  # Tài liệu dự án
└── requirements.txt           # Thư viện cần cài đặt
```

---

## 🛠️ Cài đặt

### 1️⃣ Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

### 2️⃣ Cài đặt thư viện

```bash
pip install -r requirements.txt
```

hoặc thủ công:

```bash
pip install ultralytics gradio opencv-python
```

---

## ▶️ Chạy ứng dụng

Chạy lệnh sau để mở Gradio:

```bash
python app.py
```

Terminal sẽ hiển thị:

```
* Running on http://127.0.0.1:7860
```

Mở đường dẫn trên trình duyệt để dùng demo.

---

## 🎥 Demo Nhận Diện Video

Demo sử dụng:

```python
results = model.predict(source=video_file.name, conf=0.25, save=True)
return results[0].path
```

YOLO tự lưu output vào:

```
runs/detect/exp*/video.mp4
```

---

## 🧭 Demo Tracking Video

Tracking được gọi bằng:

```python
results = model.predict(
    source=video_file.name,
    task="track",
    conf=0.25,
    save=True
)
```

Kết quả tracking (có ID) được lưu vào:

```
runs/track/exp*/video.mp4
```

Sau đó Gradio đọc và hiển thị video mới nhất.

---

## ℹ️ Lưu ý quan trọng về Tracking ID

YOLO sử dụng ByteTrack/BOTSORT, vì vậy ID:

* **Không đảm bảo chạy liên tục 1,2,3,4…**
* Có thể **nhảy số** nếu đối tượng biến mất rồi xuất hiện lại
* Tăng dần theo thời gian
* Không reset giữa quá trình tracking

Đây là hành vi **hoàn toàn bình thường** của các thuật toán tracking hiện đại.

---

## 🧪 Hỗ trợ các mô hình YOLO

Bạn có thể thay đổi model trong:

`utils/loader.py`

Hỗ trợ:

* YOLOv8: `yolov8n.pt`, `yolov8s.pt`, …
* YOLO11: `yolo11n.pt`, `yolo11s.pt`, …
* Model tự train: `runs/train/exp/weights/best.pt`

---

## ✨ Giao diện minh họa

Bạn có thể thêm ảnh khi triển khai demo:

```
![demo](assets/demo_ui.png)
```

---

## 💡 Hướng phát triển tương lai

* Thêm demo webcam realtime
* Hiển thị FPS trực tiếp trong video
* Chọn nhiều model YOLO trong UI
* Tự động tạo GIF preview kết quả
* Deploy lên HuggingFace Spaces

---

## 🤝 Đóng góp

Mọi ý tưởng, bug report hoặc pull request đều được chào đón!
Nếu bạn muốn mở rộng thêm tính năng mới, cứ tự nhiên tạo issue.

---

## 📄 License

Dự án được phát hành theo giấy phép MIT – bạn được phép sử dụng cho học tập, nghiên cứu và phát triển sản phẩm.

---

## ❤️ Cảm ơn

Cảm ơn:

* **Ultralytics** vì đã cung cấp bộ YOLO tuyệt vời
* **Gradio** vì framework giao diện AI siêu nhanh và dễ dùng

