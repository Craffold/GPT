from iran_id_ocr import extract_iran_id_data
from PIL import Image, ImageDraw
import tempfile

def create_test_image(text: str) -> str:
    image = Image.new("RGB", (400, 200), "white")
    draw = ImageDraw.Draw(image)
    draw.text((10, 80), text, fill="black")
    temp = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    image.save(temp.name)
    return temp.name

def test_extract_returns_text():
    path = create_test_image("1234567890")
    data = extract_iran_id_data(path)
    assert isinstance(data["raw_text"], str)
