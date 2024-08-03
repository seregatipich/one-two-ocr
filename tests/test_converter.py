import os
import sys
import unittest
from unittest.mock import MagicMock, patch

from one_two_ocr_utils.converter import pdf_to_images


class TestPDFToImages(unittest.TestCase):

    @patch("converter.fitz.open")
    def test_pdf_to_images_success(self, mock_fitz_open):
        # Mock the document and page behavior
        mock_document = MagicMock()
        mock_document.page_count = 2
        mock_page = MagicMock()
        mock_pixmap = MagicMock()
        mock_pixmap.width = 100
        mock_pixmap.height = 200
        mock_pixmap.samples = b"\x00" * (100 * 200 * 3)

        mock_page.get_pixmap.return_value = mock_pixmap
        mock_document.load_page.return_value = mock_page
        mock_fitz_open.return_value = mock_document

        with patch(
            "converter.Image.frombytes", return_value=MagicMock()
        ) as mock_frombytes:
            images = pdf_to_images("dummy_path.pdf")
            self.assertEqual(len(images), 2)
            self.assertTrue(mock_frombytes.called)
            self.assertTrue(mock_fitz_open.called)
            self.assertTrue(mock_document.load_page.called)
            self.assertTrue(mock_page.get_pixmap.called)

    @patch("converter.fitz.open", side_effect=Exception("Test Exception"))
    def test_pdf_to_images_failure(self, mock_fitz_open):
        with patch("converter.logging.error") as mock_logging_error:
            images = pdf_to_images("dummy_path.pdf")
            self.assertEqual(images, [])
            self.assertTrue(mock_logging_error.called)


if __name__ == "__main__":
    unittest.main()
