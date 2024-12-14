from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch


#model = YOLO('museumV3.pt')


# Use the model
results = model.train(data="config.yaml"
                      , epochs=300
                      , workers=0
                      , imgsz = 256
                      , batch = 8
                      , device = 0
                      , lr0 = 0.0001
                      , save_period = 10
                      , save_dir = "/runs/detect"
                      )  # train the modelpip list
