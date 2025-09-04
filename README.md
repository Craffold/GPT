# Iranian National ID OCR

This project provides a minimal Python script for extracting text from Iranian national ID cards.
It relies on [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) with the Persian language data.

## Setup

```bash
# install system dependencies
apt-get update
apt-get install -y tesseract-ocr tesseract-ocr-fas python3-pip

# install Python dependencies
pip install -r requirements.txt
```

## Usage

```bash
python iran_id_ocr.py path/to/id-card-image.jpg
```

The script will output a JSON object containing any detected fields such as the national ID number,
birth date, and the raw OCR text.

## Testing

Run `pytest` to execute the test suite.
