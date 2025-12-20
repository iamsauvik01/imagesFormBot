import easyocr

# Initialize once (important for performance)
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):
    """
    Extracts text from an image using EasyOCR
    """
    results = reader.readtext(image_path, detail=0)
    return "\n".join(results)
