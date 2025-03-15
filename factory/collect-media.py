import os
import shutil

# Define the file extensions to look for
TARGET_EXTENSIONS = {'.mp3', '.mp4', '.amv', '.gif'}

# Get the current directory
current_dir = os.getcwd()

# Define the sibling directory (Collected_Media) at the same level as current_dir
parent_dir = os.path.dirname(current_dir)
collected_media_dir = os.path.join(parent_dir, "Collected_Media")

# Create the Collected_Media directory if it doesn't exist
os.makedirs(collected_media_dir, exist_ok=True)

# Walk through the directory structure
for root, _, files in os.walk(current_dir):
    for file in files:
        if any(file.lower().endswith(ext) for ext in TARGET_EXTENSIONS):
            source_path = os.path.join(root, file)
            
            # Ensure the source file still exists before copying
            if not os.path.exists(source_path):
                print(f"Skipping missing file: {source_path}")
                continue
            
            destination_path = os.path.join(collected_media_dir, file)
            
            # Avoid overwriting existing files (append a number if necessary)
            counter = 1
            while os.path.exists(destination_path):
                base, ext = os.path.splitext(file)
                destination_path = os.path.join(collected_media_dir, f"{base}_{counter}{ext}")
                counter += 1
            
            try:
                shutil.copy2(source_path, destination_path)
                print(f"Copied: {source_path} -> {destination_path}")
            except Exception as e:
                print(f"Error copying {source_path}: {e}")

print("\nMedia collection complete! Check the 'Collected_Media' directory.")
