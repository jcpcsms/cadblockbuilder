#This will generate a list of obejct classes formated for the config.yaml file from the "RAW" class output from CVAT.AI project.
#Save the contents of the RAW file as "RAW.txt" in your project directory then run this and copy the output of the list to the config.yaml file.

import re

def extract_names_and_create_list(raw_file_path, output_file_path):
    names = []

    # Read the RAW file
    with open(raw_file_path, 'r') as raw_file:
        for line in raw_file:
            # Use regex to find the "name" entry
            match = re.search(r'"name":\s*"([^"]+)"', line)
            if match:
                # Extract the name without quotes
                name_value = match.group(1)
                names.append(name_value)
                print(f"Found name: {name_value}")  # Debug print to show found names
            else:
                print(f"No match in line: {line.strip()}")  # Debug print for lines without matches

    # Write the numbered list to the output file
    with open(output_file_path, 'w') as output_file:
        for i, name in enumerate(names, start=0):
            output_file.write(f"{i}: {name}\n")

    print(f"Numbered list created in {output_file_path}")

# Define the file paths
raw_file_path = 'raw.txt'  # Replace with the actual path to your RAW file
output_file_path = 'newest.txt'  # Replace with the desired output path and file name


# Run the function
extract_names_and_create_list(raw_file_path, output_file_path)
