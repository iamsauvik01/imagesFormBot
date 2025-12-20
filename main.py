import os
from utils.image_utils import preprocess_image
from ocr.ocr_engine import extract_text

IMAGE_NAME = "sample.jpg"

def main():
    input_image_path = os.path.join("images", IMAGE_NAME)
    processed_image_path = os.path.join("processed_images", IMAGE_NAME)

    os.makedirs("processed_images", exist_ok=True)

    print("🔹 Preprocessing image...")
    preprocess_image(input_image_path, processed_image_path)

    print("🔹 Running OCR...")
    text = extract_text(processed_image_path)

    print("\n====== EXTRACTED TEXT ======\n")
    print(text)
    print("\n===========================\n")

if __name__ == "__main__":
    main()
