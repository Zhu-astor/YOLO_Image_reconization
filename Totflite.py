from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("C:/Users/bubbl/Desktop/Contest/AI GO/Classification/datasets/museum_data_annotation.v9i.yolov8/runs/detect/train4/weights/best.pt")

# Export the model to TFLite format
model.export(format="tflite")  # creates 'yolov8n_int8.tflite'
