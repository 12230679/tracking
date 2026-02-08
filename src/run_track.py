from ultralytics import YOLO
from pathlib import Path

model = YOLO("yolov8n.pt")

video_path = "data/데이터셋.mp4"
out_dir = Path("outputs")

model.track(
    source=video_path,
    tracker="bytetrack.yaml",
    persist=True,
    save=True,
    project=str(out_dir),
    name="run1",
    classes=[2, 3, 5, 7],
)

print("Done! outputs/run1 확인")
