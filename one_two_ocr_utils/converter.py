import logging

import fitz
from PIL import Image


def pdf_to_images(pdf_path, dpi=300):
    images = []
    try:
        document = fitz.open(pdf_path)
        for page_num in range(document.page_count):
            page = document.load_page(page_num)
            pix = page.get_pixmap(dpi=dpi)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            images.append(img)
        logging.info(f"Converted {len(images)} pages from {pdf_path} to images.") # logging does not write log to the console
    except Exception as e:
        logging.error(f"Error converting PDF to images: {e}")
    return images
