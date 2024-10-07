import unittest
from unittest.mock import MagicMock, patch

from src.ocr import OCR
from PIL import Image


class TestOCR(unittest.TestCase):
    def setUp(self):
        self.ocr = OCR()

    @patch("PIL.Image.open")
    @patch("pytesseract.image_to_string")
    def test_process_image(self, mock_image_to_string, mock_image_open):
        mock_image_to_string.return_value = "Sample text"
        result = self.ocr.process_image("test_image.png")
        self.assertEqual(result, "Sample text")
        mock_image_open.assert_called_once_with("test_image.png")
        mock_image_to_string.assert_called_once()

    @patch("pdf2image.convert_from_path")
    @patch("pytesseract.image_to_string")
    def test_process_pdf(self, mock_image_to_string, mock_convert_from_path):
        mock_page = Image.new("RGB", (2550, 3300))  # Create a dummy PIL Image
        mock_convert_from_path.return_value = [mock_page]

        mock_image_to_string.return_value = "Sample text from PDF"
        result = self.ocr.process_pdf("test_document.pdf")
        self.assertEqual(result, "Sample text from PDF\n")
        mock_image_to_string.assert_called()

    @patch.object(OCR, "process_image")
    @patch.object(OCR, "process_pdf")
    def test_process_batch(self, mock_process_pdf, mock_process_image):
        mock_process_image.return_value = "Image text"
        mock_process_pdf.return_value = "PDF text"
        paths = ["test_image.png", "test_document.pdf"]
        result = self.ocr.process_batch(paths)
        self.assertEqual(
            result, {"test_image.png": "Image text", "test_document.pdf": "PDF text"}
        )
        mock_process_image.assert_called_once_with("test_image.png")
        mock_process_pdf.assert_called_once_with("test_document.pdf")

    def test_process_batch_invalid_format(self):
        result = self.ocr.process_batch(["unsupported.txt"])
        self.assertTrue("Unsupported file format" in result["unsupported.txt"])

    @patch("cv2.imread")
    @patch("cv2.cvtColor")
    @patch("cv2.adaptiveThreshold")
    def test_enhance_image(self, mock_adaptive_threshold, mock_cvt_color, mock_imread):
        mock_imread.return_value = MagicMock()
        mock_cvt_color.return_value = MagicMock()
        mock_adaptive_threshold.return_value = MagicMock()
        result = self.ocr.enhance_image("test_image.png")
        self.assertIsNotNone(result)
        mock_imread.assert_called_once_with("test_image.png")
        mock_cvt_color.assert_called_once()
        mock_adaptive_threshold.assert_called_once()

    @patch.object(OCR, "enhance_image")
    @patch("pytesseract.image_to_string")
    def test_process_image_with_enhancement(
        self, mock_image_to_string, mock_enhance_image
    ):
        mock_enhance_image.return_value = MagicMock()
        mock_image_to_string.return_value = "Enhanced image text"
        result = self.ocr.process_image_with_enhancement("test_image.png")
        self.assertEqual(result, "Enhanced image text")
        mock_enhance_image.assert_called_once_with("test_image.png")
        mock_image_to_string.assert_called_once_with(mock_enhance_image.return_value)


if __name__ == "__main__":
    unittest.main()
