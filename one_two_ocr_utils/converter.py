import logging

from pdf2image import convert_from_path


def pdf_to_images(pdf_path, dpi=300):
    try:
        images = convert_from_path(pdf_path, dpi)
        logging.info(f"Converted {len(images)} pages from {pdf_path} to images.")

        return images

    except Exception as error:

        logging.info(f"Errorconverting PDF to images: {error}")
        return []
