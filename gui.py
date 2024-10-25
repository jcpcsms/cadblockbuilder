import customtkinter as ctk
from tkinter import filedialog, messagebox
import cv2
from ultralytics import YOLO
from PIL import Image, ImageTk

# Post scan notations and image variable as global variable (I know we dont like global but it makes sense here)
annotated_image = None
boxes_info = []

# Select the model
model = YOLO("500.pt") # This is a model with 500 epochs of training
# model = YOLO("best.pt")

# Open file function 
def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        load_image(file_path)
    return file_path
      
# Load image to scan function
def load_image(file_path):
    global annotated_image, boxes_info
    try:
        results = model(source=file_path, show=False, imgsz=640, conf=0.40, dynamic=True, optimize=True)
        display_result(results)  
        save_button.pack(pady=5)    
    except Exception as e:
        print(f"Error loading image: {e}")

# Display the image with results function
def display_result(results):
    global annotated_image, boxes_info
    boxes_info.clear() 
    Results_list = [] 
    for result in results:
        orig_img = result.orig_img
        boxes = result.boxes
        annotated_image = orig_img.copy()
       
# Annotation box over detection 
        for index, box in enumerate(boxes, start=1):
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label_name = result.names[cls]
            boxes_info.append((x1, y1, x2, y2, conf, label_name)) 

            color = (0, 255, 0) if conf > 0.5 else (0, 0, 255)
            cv2.rectangle(annotated_image, (x1, y1), (x2, y2), color, 2)
            text = f"{label_name}: {conf:.2f}"
            cv2.putText(annotated_image, text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            Results_list.append(f"{index}. {label_name} (Confidence: {conf:.2f})")
        
# Get the original image dimensions
        height, width = annotated_image.shape[:2]
        
# Desired maximum dimensions for display
        max_width = 800
        max_height = 800
        
# set scale factor to preserve image geometry
        scale_factor = min(max_width / width, max_height / height)
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        annotated_image = cv2.resize(annotated_image, (new_width, new_height))
        show_image(annotated_image)

# clear results for next image scan
        results_textbox.delete(1.0, ctk.END) 
        results_textbox.insert(ctk.END, "\n".join(Results_list)) 

# Function to show image after scan
def show_image(image):
    cv2_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    pil_image = Image.fromarray(cv2_image)
    tk_image = ImageTk.PhotoImage(pil_image)
    label.configure(image=tk_image)
    label.image = tk_image
    root.geometry(f"{pil_image.width + 20}x{pil_image.height + 100}")

# Function to save new image after scans
def save_image():
    global annotated_image
    if annotated_image is not None:
        save_path = filedialog.asksaveasfilename(defaultextension=".jpeg", filetypes=[("JPEG files", "*.jpeg"), ("All files", "*.*")])
        if save_path:
            cv2.imwrite(save_path, annotated_image)
            messagebox.showinfo(f"Image saved to {save_path}")
    else:
        messagebox.showwarning("Nothing new to save. Try again.")
        
# main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
root = ctk.CTk()
root.geometry("500x500")

drop_area = ctk.CTkFrame(root, width=800, height=800)

# CAD BlockBuilder Label
label = ctk.CTkLabel(root, text="CAD BlockBuilder Beta Image Scanner")
label.pack(pady=20)

# Create a button to open the file dialog
load_button = ctk.CTkButton(root, text="Load Image", command=open_file_dialog)
load_button.pack(pady=10)

# Create a button to save the updated after a scan
save_button = ctk.CTkButton(root, text="Save Annotated Image", command=save_image)

# List results as text
results_textbox = ctk.CTkTextbox(root, width=400, height=200)
results_textbox.pack(pady=5)

root.mainloop()
