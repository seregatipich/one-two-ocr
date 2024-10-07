# One Two OCR

[![PyPI version](https://badge.fury.io/py/one-two-ocr.svg)](https://badge.fury.io/py/one-two-ocr) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**One Two OCR** is a straightforward and powerful Python library that makes it easy to extract text from images and PDF files using Optical Character Recognition (OCR). It's perfect for dealing with large sets of mixed images and PDFs in just a few simple steps.

## Features
- **Extract Text from Images**: Supports popular formats like PNG, JPG, BMP, TIFF, and more.
- **Extract Text from PDFs**: Converts PDF pages to images and extracts text quickly and easily.
- **Batch Processing**: Process multiple images and PDFs at once.
- **Image Enhancement**: Clean up and enhance images for better OCR results, especially helpful with low-quality scans.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
  - [Import and Initialize](#1-import-and-initialize-the-ocr-class)
  - [Extract Text from an Image](#2-extract-text-from-an-image)
  - [Extract Text from a PDF](#3-extract-text-from-a-pdf)
  - [Enhance an Image](#4-enhance-an-image)
  - [Extract Text from an Enhanced Image](#5-extract-text-from-an-enhanced-image)
  - [Batch Processing](#6-batch-processing)
- [Dependencies](#dependencies)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation
To get started with **One Two OCR**, you'll need to install the library and its dependencies. You'll also need to have Tesseract set up on your system.

### 1. Install Tesseract

#### Windows
- Download Tesseract from [UB Mannheim's GitHub page](https://github.com/UB-Mannheim/tesseract/wiki).
- Run the installer.
- Add the installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your system's PATH.

#### macOS
- Install Tesseract using Homebrew:
    ```sh
    brew install tesseract
    ```

#### Linux
- On Debian-based systems (like Ubuntu):
    ```sh
    sudo apt update
    sudo apt install tesseract-ocr
    ```

- On Red Hat-based systems (like Fedora):
    ```sh
    sudo dnf install tesseract
    ```

- For other distributions, see the [Tesseract installation guide](https://github.com/tesseract-ocr/tesseract).

### 2. Install the Library
Install **One Two OCR** via pip:
```sh
pip install git+https://github.com/seregatipich/one-two-ocr.git
```
This will automatically install the necessary dependencies too.

## Usage
Here's a quick rundown on how to use **One Two OCR** for different OCR tasks.

### 1. Import and Initialize the OCR Class
Import the OCR class and get started:
```python
from ocr import OCR

# Initialize the OCR object
ocr = OCR(tesseract_cmd='/usr/local/bin/tesseract')  # Add Tesseract path if needed
```

### 2. Extract Text from an Image
Extract text from an image:
```python
# Extract text from an image
image_text = ocr.process_image('path/to/your/image.png')
print("Text from image:", image_text)
```

### 3. Extract Text from a PDF
Extract text from a PDF file, processing each page individually:
```python
# Extract text from a PDF
pdf_text = ocr.process_pdf('path/to/your/document.pdf')
print("Text from PDF:", pdf_text)
```

### 4. Enhance an Image
Enhance an image to improve OCR accuracy:
```python
ocr.enhance_image('path/to/image.png', 'path/to/enhanced_image.png')
```

### 5. Extract Text from an Enhanced Image
Enhance an image first, then extract text:
```python
enhanced_text = ocr.process_image_with_enhancement('path/to/your/image.png')
print("Text from enhanced image:", enhanced_text)
```

### 6. Batch Processing
Process multiple images and PDFs in one go:
```python
files = ['path/to/image1.png', 'path/to/document.pdf']
batch_results = ocr.process_batch(files)
for file, text in batch_results.items():
    print(f"Text from {file}: {text}")
```

## Dependencies
**One Two OCR** uses several Python packages:
- **pytesseract**: Interface to Tesseract OCR.
- **pdf2image**: Converts PDF pages to images.
- **Pillow**: For handling image files.
- **opencv-python**: Image processing and enhancement.
- **numpy**: Advanced image processing support.

These are installed automatically when you add the library.

## Running Tests
To make sure everything is working, run the tests:
```sh
python -m unittest discover tests
```
This will run all tests to confirm that everything's set up properly.

## Contributing
We'd love for you to contribute! Here's how:
1. Fork the repo.
2. Create a feature branch: `git checkout -b feature/YourFeature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/YourFeature`.
5. Open a pull request.

## License
This library is available under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and share!

## Contact
If you have any questions or run into issues, reach out!

- **Author**: Sergei Poluektov
- **Email**: [seregatipich@outlook.com](mailto:seregatipich@outlook.com)
- **GitHub**: [seregatipich](https://github.com/seregatipich)
