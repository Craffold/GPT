import cv2
import pytesseract
from PIL import Image
import re

ID_NUMBER_REGEX = re.compile(r"\b\d{10}\b")
BIRTH_DATE_REGEX = re.compile(r"\b\d{4}/\d{2}/\d{2}\b")

def preprocess_image(image_path: str):
    """Load image and return thresholded version that highlights black text."""
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found: {image_path}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Invert threshold to get black text as white on black background
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    return thresh

def ocr_image(processed_image) -> str:
    """Run Tesseract OCR on the preprocessed image."""
    pil_img = Image.fromarray(processed_image)
    text = pytesseract.image_to_string(pil_img, lang="fas+eng")
    return text

def parse_fields(text: str) -> dict:
    """Extract key data fields from OCR text."""
    data = {}
    id_match = ID_NUMBER_REGEX.search(text)
    if id_match:
        data["national_id"] = id_match.group()
    birth_match = BIRTH_DATE_REGEX.search(text)
    if birth_match:
        data["birth_date"] = birth_match.group()
    data["raw_text"] = text.strip()
    return data

def extract_iran_id_data(image_path: str) -> dict:
    """High-level helper that returns fields extracted from an ID card image."""
    processed = preprocess_image(image_path)
    text = ocr_image(processed)
    return parse_fields(text)

if __name__ == "__main__":
    import sys, json
    if len(sys.argv) != 2:
        print("Usage: python iran_id_ocr.py <image-path>")
        sys.exit(1)
    result = extract_iran_id_data(sys.argv[1])
    print(json.dumps(result, ensure_ascii=False, indent=2))
