import cv2
import os
from ultralytics import YOLO


model = YOLO('yolov8s.pt')

dataset_path = 'C:/Users/hyo56/Downloads/val/val/dancetrack0004/img1'
save_path = 'dancetrack0004_results.txt'


image_files = sorted([f for f in os.listdir(dataset_path) if f.endswith('.jpg')])


with open(save_path, 'w') as f:
    results = model.track(
        source=dataset_path, 
        persist=True, 
        tracker="botsort.yaml", 
        conf=0.1, 
        iou=0.5, 
        classes=[0], 
        stream=True, 
        show=False, 
        
    )

    for frame_idx, r in enumerate(results, start=1):
        
        if r.boxes is not None and r.boxes.id is not None:
            boxes = r.boxes.xywh.cpu().numpy()
            ids = r.boxes.id.cpu().numpy().astype(int)
            confs = r.boxes.conf.cpu().numpy()

            for box, obj_id, conf in zip(boxes, ids, confs):
                x, y, w, h = box
                left = x - w / 2
                top = y - h / 2
                f.write(f"{frame_idx},{obj_id},{left:.2f},{top:.2f},{w:.2f},{h:.2f},{conf:.2f},-1,-1,-1\n")
        
        
        annotated_frame = r.plot()

        
        display_frame = cv2.resize(annotated_frame, (960, 540))

        cv2.imshow("YOLOv8 DanceTrack Player", display_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        
cv2.destroyAllWindows()

