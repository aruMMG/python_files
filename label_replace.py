import os
import shutil

# Define the source directory containing the text files
source_directory = "/home/aru/phd/objective2/generative_models/diffusion/text2image/80"

# Define the destination directory where modified files will be saved
save_directory = "/home/aru/phd/objective2/generative_models/diffusion/text2image/labels/80"

# Create the destination directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

# Iterate through all text files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith(".txt"):
        source_file_path = os.path.join(source_directory, filename)
        save_file_path = os.path.join(save_directory, filename)

        # Open the source file for reading and the save file for writing
        with open(source_file_path, "r") as source_file, open(save_file_path, "w") as save_file:
            # Iterate through each line in the source file
            for line in source_file:
                # Split the line by space
                parts = line.split()
                if len(parts) >= 1:
                    # Replace the first integer with 0
                    parts[0] = "0"
                    # Join the modified parts and write to the save file
                    save_file.write(" ".join(parts) + "\n")

print("Conversion complete. Modified files are saved in the destination directory.")
