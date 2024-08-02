import logging

import cv2
import numpy as np
from PIL import Image


def preprocess_image(
    image,
    grayscale=True,
    threshold=True,
    rescale=True,
    noise_removal=True,
    dilation=True,
    erosion=True,
    edge_detection=True,
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

        # Grayscale
        if grayscale:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            logging.info("Converted image to grayscale.")

        # Noise Removal
        if noise_removal:
            image = cv2.medianBlur(image, 5)
            logging.info("Noise removed from image.")

        # Binarization
        if threshold:
            _, image = cv2.threshold(
                image, 128, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            logging.info("Applied thresholding to image.")

        # Dilation
        if dilation:
            kernel = np.ones((1, 1), np.uint8)
            image = cv2.dilate(image, kernel, iterations=1)
            logging.info("Dilation applied to image.")

        # Erosion
        if erosion:
            kernel = np.ones((1, 1), np.uint8)
            image = cv2.erode(image, kernel, iterations=1)
            logging.info("Erosion applied to image.")

        # Edge Detection
        if edge_detection:
            image = cv2.Canny(image, 100, 200)
            logging.info("Edge detection applied to image.")

        # Convert back to PIL format
        image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        logging.info("Image preprocessing completed.")
        return image

    except Exception as e:
        log_processing_status(f"Error preprocessing image: {e}")
        return image


def log_processing_status(status_message):
    logging.error(status_message)
