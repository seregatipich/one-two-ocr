import logging
from typing import Dict, List

import cv2
import numpy as np
import pytesseract
from pdf2image import convert_from_path
from PIL import Image

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OCR:
    def __init__(self, tesseract_cmd: str = None):
        if tesseract_cmd:
            pytesseract.pytesseract.tesseract_cmd = tesseract_cmd
        logger.info("Initialized OCR with tesseract_cmd: %s", tesseract_cmd)

    def process_image(self, image_path: str) -> str:
        logger.info("Processing image: %s", image_path)
        try:
            with Image.open(image_path) as image:
                logger.info("Image %s opened successfully", image_path)
                text = pytesseract.image_to_string(image)
                logger.debug("OCR text from image %s: %s", image_path, text[:50])
                return text
        except FileNotFoundError:
            logger.error("File not found: %s", image_path)
            raise FileNotFoundError(f"File not found: {image_path}")
        except Exception as e:
            logger.error("Error processing image %s: %s", image_path, e)
            raise ValueError(f"Error processing image {image_path}: {e}")

    def process_pdf(self, pdf_path: str, dpi: int = 300) -> str:
        logger.info("Processing PDF: %s with DPI: %d", pdf_path, dpi)
        try:
            pages = convert_from_path(pdf_path, dpi)
            logger.info(
                "PDF %s converted to images successfully, number of pages: %d",
                pdf_path,
                len(pages),
            )
            text = ""
            for i, page in enumerate(pages):
                page_text = pytesseract.image_to_string(page)
                logger.debug(
                    "OCR text from page %d of %s: %s", i + 1, pdf_path, page_text[:50]
                )
                text += page_text + "\n"
            return text
        except FileNotFoundError:
            logger.error("File not found: %s", pdf_path)
            raise FileNotFoundError(f"File not found: {pdf_path}")
        except Exception as e:
            logger.error("Error processing PDF %s: %s", pdf_path, e)
            raise ValueError(f"Error processing PDF {pdf_path}: {e}")

    def process_batch(self, paths: List[str]) -> Dict[str, str]:
        logger.info("Processing batch of files: %s", paths)
        results = {}
        for path in paths:
            try:
                if path.lower().endswith(".pdf"):
                    logger.info("Processing PDF file: %s", path)
                    results[path] = self.process_pdf(path)
                elif path.lower().endswith(
                    (".png", ".jpg", ".jpeg", ".tiff", ".bmp", ".gif")
                ):
                    logger.info("Processing image file: %s", path)
                    results[path] = self.process_image(path)
                else:
                    logger.warning("Unsupported file format: %s", path)
                    results[path] = f"Unsupported file format: {path}"
            except Exception as e:
                logger.error(str(e))
                results[path] = str(e)
        return results

    def enhance_image(self, image_path: str, output_path: str = None) -> np.ndarray:
        logger.info("Enhancing image: %s", image_path)
        try:
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"Image {image_path} could not be read")
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            denoised = cv2.fastNlMeansDenoising(gray, None, 10, 7, 21)
            enhanced = cv2.adaptiveThreshold(
                denoised, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
            )
            if output_path:
                cv2.imwrite(output_path, enhanced)
                logger.info("Enhanced image saved to: %s", output_path)
            return enhanced
        except FileNotFoundError:
            logger.error("File not found: %s", image_path)
            raise FileNotFoundError(f"File not found: {image_path}")
        except Exception as e:
            logger.error("Error enhancing image %s: %s", image_path, e)
            raise ValueError(f"Error enhancing image {image_path}: {e}")

    def process_image_with_enhancement(self, image_path: str) -> str:
        logger.info("Processing image with enhancement: %s", image_path)
        try:
            enhanced_image = self.enhance_image(image_path)
            text = pytesseract.image_to_string(enhanced_image)
            logger.debug("OCR text from enhanced image %s: %s", image_path, text[:50])
            return text
        except FileNotFoundError:
            logger.error("File not found: %s", image_path)
            raise FileNotFoundError(f"File not found: {image_path}")
        except Exception as e:
            logger.error("Error processing enhanced image %s: %s", image_path, e)
            raise ValueError(f"Error processing enhanced image {image_path}: {e}")

    @staticmethod
    def save_text_to_file(text: str, output_path: str) -> None:
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(text)
            logger.info(f"Text saved to file: {output_path}")
        except Exception as e:
            logger.error(f"Error saving text to file {output_path}: {e}")
            raise ValueError(f"Error saving text to file {output_path}: {e}")
