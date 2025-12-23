import pytesseract
from PIL import Image

# REQUIRED on Windows – update only if your path is different
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text(image_path):
    img = Image.open(image_path)

    text = pytesseract.image_to_string(img, lang="eng")
    return text

# if __name__ == "__main__":
#     extract_text()
