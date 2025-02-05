import ultralytics 
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
results = model.train(data="exam cheating.v2-examdatasetv2.yolov11\data.yaml", epochs=25)