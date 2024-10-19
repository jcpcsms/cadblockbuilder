#due to the computing resources it takes to get images and data from CVAT.AT into one location I had to use this to put the images I actually annotated and the annotations
#in a single location. So with this you can copy the images that have matching annotation file names into a your directory in order to load as training data to YOLO

import os
import shutil

def copy_images_if_match(source_folder, target_folder, reference_folder):
    # Get a list of file names in the reference folder
    reference_files = [f for f in os.listdir(reference_folder) if os.path.isfile(os.path.join(reference_folder, f))]
    
    # Loop through each file in the source folder
    for filename in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, filename)

        # Check if it's an image file - update extentions list if needed
        if os.path.isfile(source_file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Check if any reference file name is in the current filename
            if any(ref_file.lower().replace('.txt', '') in filename.lower() for ref_file in reference_files):
                # Copy the file to the target folder
                shutil.copy(source_file_path, target_folder)
                print(f'Copied: {filename}')

# Define your folders
reference_folder = 'obj_train_data' #this should be the folder with the annotation data
source_folder = 'work' 
target_folder = 'Images' 

# Run the function
try:
    copy_images_if_match(source_folder, target_folder, reference_folder)

except Exception as e:
    print(f"An error occurred: {e}")

print("Script finished.")

