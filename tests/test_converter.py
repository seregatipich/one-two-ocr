import unittest
from unittest.mock import MagicMock, patch

from PIL import Image

from one_two_ocr_utils.converter import pdf_to_images


class TestConverter(unittest.TestCase):

    @patch("fitz.open")
    @patch("PIL.Image.frombytes")
    def test_pdf_to_images_success(self, mock_frombytes, mock_fitz_open):
        # Mock the fitz.open and related objects
        mock_document = MagicMock()
        mock_page = MagicMock()
        mock_pixmap = MagicMock()

        mock_fitz_open.return_value = mock_document
        mock_document.page_count = 2
        mock_document.load_page.return_value = mock_page
        mock_page.get_pixmap.return_value = mock_pixmap
        mock_pixmap.width = 100
        mock_pixmap.height = 200
        mock_pixmap.samples = b"dummy_image_data"

        # Mock the PIL Image.frombytes
        mock_image = MagicMock(spec=Image.Image)
        mock_frombytes.return_value = mock_image

        # Call the function
        result = pdf_to_images("TestOCR.pdf")

        # Assertions
        self.assertEqual(len(result), 2)
        self.assertIsInstance(result[0], Image.Image)
        self.assertIsInstance(result[1], Image.Image)

        mock_fitz_open.assert_called_once_with("TestOCR.pdf")
        self.assertEqual(mock_document.load_page.call_count, 2)
        self.assertEqual(mock_page.get_pixmap.call_count, 2)
        self.assertEqual(mock_frombytes.call_count, 2)

    @patch("fitz.open")
    @patch("logging.error")
    def test_pdf_to_images_error(self, mock_logging_error, mock_fitz_open):
        # Mock fitz.open to raise an exception
        mock_fitz_open.side_effect = Exception("Test error")

        # Call the function
        result = pdf_to_images("TestOCR.pdf")

        # Assertions
        self.assertEqual(result, [])
        mock_logging_error.assert_called_once_with(
            "Error converting PDF to images: Test error"
        )

    def test_pdf_to_images_dpi(self):
        with patch("fitz.open") as mock_fitz_open, patch(
            "PIL.Image.frombytes"
        ) as mock_frombytes:

            mock_document = MagicMock()
            mock_page = MagicMock()
            mock_pixmap = MagicMock()

            mock_fitz_open.return_value = mock_document
            mock_document.page_count = 1
            mock_document.load_page.return_value = mock_page
            mock_page.get_pixmap.return_value = mock_pixmap

            # Call the function with a custom DPI
            pdf_to_images("TestOCR.pdf", dpi=150)

            # Assert that get_pixmap was called with the correct DPI
            mock_page.get_pixmap.assert_called_once_with(dpi=150)


if __name__ == "__main__":
    unittest.main()
