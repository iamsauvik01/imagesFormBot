import os
from pathlib import Path

# Path to your images folder
IMAGES_DIR = Path("images")

# Loop through all files in the folder
for file in IMAGES_DIR.iterdir():
    if file.is_file() and file.suffix.lower() == ".jpg":
        # Remove the 'qr_' prefix from the filename
        new_name = file.name.replace("qr_", "", 1)  # only replace the first occurrence
        new_path = file.with_name(new_name)

        # Rename the file
        file.rename(new_path)
        print(f"Renamed: {file.name} -> {new_name}")