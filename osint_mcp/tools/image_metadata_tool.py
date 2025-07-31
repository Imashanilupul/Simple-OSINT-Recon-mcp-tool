from PIL import Image
from PIL.ExifTags import TAGS


def extract_image_metadata(path: str) -> str:
    image = Image.open(path)
    exif_data = image._getexif()
    if not exif_data:
        return "No EXIF metadata found."

    result = ""
    for tag, val in exif_data.items():
        result += f"{TAGS.get(tag, tag)}: {val}\n"
    return result
