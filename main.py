import os
from ocr.ocr_engine import extract_text
from excel.writeExcel import excel_write
from pathlib import Path

IMAGES_DIR = "images"

def main():
    image_files = [
        f for f in os.listdir(IMAGES_DIR)
        if f.lower().endswith(".jpg")
    ]

    if not image_files:
        print("❌ No JPG images found in images folder")
        return
    
    failed_filenames = []
    rows = []
    
    for image_name in image_files:
        image_path = os.path.join(IMAGES_DIR, image_name)
        filename = Path(image_name).stem
        
        text = extract_text(image_path)
        if text.count("*") == 6:
            print(f"OCR Passed: {filename}")
            data = text.split("*")
            data.append(filename)
            rows.append(data)
        else:
            failed_filenames.append(filename)

    if rows:
        excel_write(rows)
    
    failed_size = len(failed_filenames)
    print(f"{failed_size} Failed. \n List: {failed_filenames}")
    

if __name__ == "__main__":
    main()
