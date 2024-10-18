from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.yaml")  # build a new model from YAML

# Train the model
results = model.train(data="config.yaml", epochs=50, optimize=True, imgsz=1024, dynamic=True, weight_decay=0.0001)
