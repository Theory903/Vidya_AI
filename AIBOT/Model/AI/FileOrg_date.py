import os
import shutil
import datetime

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to organize files by creation date and file name
def organize_files_by_creation_date(source_dir):
    files = os.listdir(source_dir)

    for filename in files:
        if os.path.isfile(os.path.join(source_dir, filename)):
            creation_date = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(source_dir, filename)))
            date_str = creation_date.strftime("%Y-%m-%d")
            
            # Use the original file name (without extension) as the subdirectory name
            subdirectory_name = os.path.splitext(filename)[0]

            date_dir = os.path.join(source_dir, date_str)
            subdirectory_path = os.path.join(date_dir, subdirectory_name)

            create_directory(date_dir)

            # Move the file to the final directory
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(subdirectory_path, filename)

            # Check if the file already exists in the target directory
            if not os.path.exists(target_file):
                create_directory(subdirectory_path)
                shutil.move(source_file, target_file)
                print(f"Moved '{filename}' to '{date_str}/{subdirectory_name}'")

# Specify the source directory where the files are located
source_directory = 'Model/Snap_ai'

# Call the function to organize files by creation date and file name
organize_files_by_creation_date(source_directory)
