import logging

import cv2
import numpy as np
from PIL import Image


def preprocess_image(
    image,
    grayscale=True,
    adaptive_threshold=True,
    rescale=True,
    noise_removal=True,
    sharpening=True,
    contrast_enhancement=True,
):
    try:
        # Convert PIL image to OpenCV format
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Rescaling
        if rescale:
            image = cv2.resize(
                image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC
            )
            logging.info("Image rescaled.")

        # Convert to grayscale
        if grayscale:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            logging.info("Converted image to grayscale.")
        else:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Noise Removal
        if noise_removal:
            gray = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
            logging.info("Noise removed from image.")

        # Contrast Enhancement
        if contrast_enhancement:
            clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
            gray = clahe.apply(gray)
            logging.info("Contrast enhanced.")

        # Adaptive Thresholding
        if adaptive_threshold:
            binary = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
            )
            logging.info("Applied adaptive thresholding to image.")
        else:
            _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Sharpening
        if sharpening:
            kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            binary = cv2.filter2D(binary, -1, kernel)
            logging.info("Image sharpened.")

        # Ensure black text on white background
        binary = cv2.bitwise_not(binary)

        # Convert back to PIL format
        image = Image.fromarray(binary)

        logging.info("Image preprocessing completed.")
        return image

    except Exception as e:
        logging.error(f"Error preprocessing image: {e}")
        return image


def log_processing_status(status_message):
    logging.error(status_message)
    