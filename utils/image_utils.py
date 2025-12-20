import cv2
import os

def preprocess_image(input_path, output_path):
    """
    Converts image to grayscale and applies thresholding
    for better OCR accuracy.
    """
    img = cv2.imread(input_path)

    if img is None:
        raise ValueError("Image not found or unable to read")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Binary threshold
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    cv2.imwrite(output_path, thresh)

    return output_path
