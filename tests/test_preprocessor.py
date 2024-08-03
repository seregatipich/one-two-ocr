import unittest

import numpy as np
from PIL import Image

from one_two_ocr_utils.preprocessor import preprocess_image


class TestPreprocessor(unittest.TestCase):

    def setUp(self):
        self.image = Image.fromarray(np.ones((100, 100, 3), dtype=np.uint8) * 255)

    def test_preprocess_image_default(self):
        processed_image = preprocess_image(self.image)
        self.assertIsInstance(
            processed_image,
            Image.Image,
            "Processed image should be an instance of PIL.Image.Image",
        )

    def test_preprocess_image_grayscale(self):
        processed_image = preprocess_image(self.image, grayscale=True)
        self.assertEqual(
            processed_image.mode, "L", "Processed image should be in grayscale mode"
        )

    def test_preprocess_image_rescale(self):
        processed_image = preprocess_image(self.image, rescale=True)
        self.assertNotEqual(
            processed_image.size, self.image.size, "Processed image should be rescaled"
        )

    def test_preprocess_image_noise_removal(self):
        processed_image = preprocess_image(self.image, noise_removal=True)
        self.assertIsInstance(
            processed_image,
            Image.Image,
            "Processed image should still be an instance of PIL.Image.Image",
        )

    def test_preprocess_image_threshold(self):
        processed_image = preprocess_image(self.image, threshold=True)
        self.assertIsInstance(
            processed_image,
            Image.Image,
            "Processed image should still be an instance of PIL.Image.Image",
        )

    def test_preprocess_image_dilation(self):
        processed_image = preprocess_image(self.image, dilation=True)
        self.assertIsInstance(
            processed_image,
            Image.Image,
            "Processed image should still be an instance of PIL.Image.Image",
        )

    def test_preprocess_image_erosion(self):
        processed_image = preprocess_image(self.image, erosion=True)
        self.assertIsInstance(
            processed_image,
            Image.Image,
            "Processed image should still be an instance of PIL.Image.Image",
        )

    def test_preprocess_image_edge_detection(self):
        processed_image = preprocess_image(self.image, edge_detection=True)
        self.assertIsInstance(
            processed_image,
            Image.Image,
            "Processed image should still be an instance of PIL.Image.Image",
        )


if __name__ == "__main__":
    unittest.main()
