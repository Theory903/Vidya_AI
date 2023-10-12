import os
import shutil

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to organize files by extension
def organize_files_by_extension(source_dir):
    # List all files in the source directory
    files = os.listdir(source_dir)

    # Create a dictionary to store file extensions and their corresponding directories
    extension_dirs = {}

    for filename in files:
        if os.path.isfile(os.path.join(source_dir, filename)):
            # Get the file extension
            file_extension = filename.split('.')[-1].lower()

            # Define a directory based on the file extension
            target_dir = os.path.join(source_dir, file_extension)

            # Create the directory if it doesn't exist in the source directory
            create_directory(target_dir)

            # Move the file to the corresponding directory
            source_file = os.path.join(source_dir, filename)
            target_file = os.path.join(target_dir, filename)

            # Check if the file already exists in the target directory
            if not os.path.exists(target_file):
                shutil.move(source_file, target_file)
                print(f"Moved '{filename}' to '{file_extension}' directory")
