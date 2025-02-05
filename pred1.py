import os
import cv2
import numpy as np
from ultralytics import YOLO

# Define directories and video paths
VIDEO_PATH = os.path.join('.', 'exam cheating.v2-examdatasetv2.yolov11\istockphoto-2168469164-640_adpp_is\istockphoto-1499130481-640_adpp_is.mp4')  # Input video path
OUTPUT_VIDEO_PATH = os.path.join('.', 'exam_cheating_output.mp4')  # Output video path

# Load the YOLO model
model_path = os.path.join('runs', 'detect', 'train4', 'weights', 'best.pt')
model = YOLO(model_path)
threshold = 0.5  # Confidence threshold

class_name_dict = {
    0: 'person',
    1: 'students_cheating',
    2: 'students_not_cheating'
}

# Open video file
cap = cv2.VideoCapture(VIDEO_PATH)
if not cap.isOpened():
    print(f"Failed to open video: {VIDEO_PATH}")
    exit()

# Get video properties
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for MP4
out = cv2.VideoWriter(OUTPUT_VIDEO_PATH, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference on the frame
    results = model(frame)[0]

    for result in results:
        if result.boxes:
            for box in result.boxes:
                conf = box.conf.item()
                cls_id = box.cls.item()  # Class ID

                if conf >= threshold:  # Only process if confidence is above threshold
                    x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())  # Bounding box coordinates

                    # Draw a polygon (rectangle) around the detected object
                    points = [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]
                    label = f"{class_name_dict.get(cls_id, 'Unknown')} {conf:.2f}"
                    
                    if cls_id == 1:
                        color = (0, 0, 255)  # Red for cheating students
                    else:
                        color = (0, 255, 0)  # Green for other detections
                    
                    cv2.polylines(frame, [np.array(points)], isClosed=True, color=color, thickness=3)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 2)
                    
                    print(f"Class: {cls_id}, Confidence: {conf}, Box: ({x1}, {y1}, {x2}, {y2})")
        else:
            print("No detections found.")
    
    # Write the processed frame to output video
    out.write(frame)
    
    # Display the frame (optional)
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Processed video saved at: {OUTPUT_VIDEO_PATH}")
