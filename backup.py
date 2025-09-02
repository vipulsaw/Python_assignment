import os
import sys
import subprocess
from datetime import datetime

def check_path_exists(path):
    """Check if a given path exists."""
    return os.path.exists(path) and os.path.isdir(path)

def generate_unique_filename(destination, filename):
    """Generate a unique filename by appending a timestamp if a duplicate exists."""
    file_path = os.path.join(destination, filename)
    if not os.path.exists(file_path):
        return file_path  # No duplicate, return original path

    name, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
    new_filename = f"{name}_{timestamp}{ext}"
    
    return os.path.join(destination, new_filename)

def copy_folder_structure(source, destination):
    """Ensure all folders from source exist in the destination."""
    for root, dirs, files in os.walk(source): # Run the Folders in loop
        relative_path = os.path.relpath(root, source)
        destination_path = os.path.join(destination, relative_path)
        
        if not os.path.exists(destination_path):
            os.makedirs(destination_path)  # Create the subfolder
            print(f"📂 Created folder: {destination_path}")

        # Copy files while renaming duplicates
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = generate_unique_filename(destination_path, file)
            subprocess.run(["cp", source_file, destination_file], check=True)
            print(f"✅ Copied: {source_file} ➝ {destination_file}")

def copy_folder(source, destination):
    """Copy an entire folder and handle subfolders & files correctly."""
    if not check_path_exists(source):
        print(f"❌ Source folder does not exist: {source}")
        sys.exit(1)

    if not check_path_exists(destination):
        print(f"❌ Destination folder does not exist: {destination}")
        sys.exit(1)

    copy_folder_structure(source, destination)

# Main execution
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("❌ Usage: python backup.py <source_folder> <destination_folder>")
        sys.exit(1)

    source_folder = sys.argv[1]
    destination_folder = sys.argv[2]

    copy_folder(source_folder, destination_folder)
