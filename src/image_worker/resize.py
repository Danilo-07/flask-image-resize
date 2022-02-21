from PIL import Image
from io import BytesIO


def resize_image(image: bytes) -> bytes:
    image = Image.open(BytesIO(image))
    resized_image = image.resize((384, 384))
    image_bytes = BytesIO()
    resized_image.save(image_bytes, format=image.format)
    return image_bytes.getvalue()
