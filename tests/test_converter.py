import unittest

from one_two_ocr_utils.converter import pdf_to_images


class TestConverter(unittest.TestCase):

    def test_pdf_to_images_success(self):
        # Assuming a valid sample PDF is available at the specified path for testing
        images = pdf_to_images("TestOCR.pdf", dpi=200)
        self.assertTrue(len(images) > 0, "Should convert PDF to at least one image")

    def test_pdf_to_images_invalid_path(self):
        images = pdf_to_images("invalid_path.pdf", dpi=200)
        self.assertEqual(images, [], "Should return an empty list for invalid PDF path")


if __name__ == "__main__":
    unittest.main()
