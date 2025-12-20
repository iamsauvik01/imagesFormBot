import os
from ocr.ocr_engine import extract_text

IMAGES_DIR = "images"

def main():
    image_files = [
        f for f in os.listdir(IMAGES_DIR)
        if f.lower().endswith(".jpg")
    ]

    if not image_files:
        print("❌ No JPG images found in images folder")
        return

    for image_name in image_files:
        image_path = os.path.join(IMAGES_DIR, image_name)

        print(f"\n📷 Processing: {image_name}")
        print("🔹 Running OCR...")

        text = extract_text(image_path)

        print("\n====== EXTRACTED TEXT ======")
        print(text)
        print("============================")

if __name__ == "__main__":
    main()
