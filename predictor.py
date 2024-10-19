from ultralytics import YOLO
import cv2

# Load a model
model = YOLO("best.pt") 

# Predict with the model showing greater than .60 confidence
results = model(source="25.jpeg", show=False, conf=0.60)

# Display the image and wait for a key press
cv2.imshow("Detection Results", results[0].plot())  
cv2.waitKey(0) 
cv2.destroyAllWindows()  
