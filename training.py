from ultralytics import YOLO

# Load a model
model = YOLO("YOLO11m.yaml")  # build a new model from YAML

# Train the model
results = model.train(data="config0.yaml", epochs=50, optimize=True, imgsz=640, dynamic=True, weight_decay=0.0001, patience=15)
