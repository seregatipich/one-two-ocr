# One Two OCR

[![PyPI version](https://badge.fury.io/py/one-two-ocr.svg)](https://badge.fury.io/py/one-two-ocr) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**One Two OCR** is a powerful and simple Python library designed for extracting text from images and PDF documents using Optical Character Recognition (OCR). This library aims to make text extraction straightforward, even from large batches of mixed image and PDF files, by leveraging the popular Tesseract OCR engine.

## Features
- **Extract Text from Images**: Supports popular image formats such as PNG, JPG, BMP, TIFF, and more.
- **Extract Text from PDFs**: Converts each page of a PDF to an image and extracts text.
- **Batch Processing**: Easily process multiple images and PDFs in a single call.
- **Image Enhancement**: Pre-process images to improve OCR accuracy, particularly for poor-quality scans.

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
To use **One Two OCR**, you will need to install the library and its dependencies. You also need Tesseract installed on your system.

### 1. Install Tesseract

#### Windows
- Download the Tesseract installer from [UB Mannheim's Tesseract GitHub releases](https://github.com/UB-Mannheim/tesseract/wiki).
- Run the installer and follow the installation steps.
- Add the Tesseract installation path (e.g., `C:\Program Files\Tesseract-OCR`) to your system's PATH environment variable.

#### macOS
- Use Homebrew to install Tesseract:

  ```sh
  brew install tesseract
  ```

#### Linux
- On Debian-based systems (like Ubuntu), install Tesseract using APT:

  ```sh
  sudo apt update
  sudo apt install tesseract-ocr
  ```

- On Red Hat-based systems (like Fedora), install Tesseract using DNF:

  ```sh
  sudo dnf install tesseract
  ```

- For other distributions, refer to the [Tesseract installation instructions](https://github.com/tesseract-ocr/tesseract).

### 2. Install the Library
Install **One Two OCR** via pip:

```sh
pip install git+https://github.com/seregatipich/one-two-ocr.git
```

This command will install all the required dependencies along with the library.

## Usage
Below are some examples demonstrating how to use **One Two OCR** for various OCR tasks.

### 1. Import and Initialize the OCR Class
Import the `OCR` class from the library and initialize it.

```python
from ocr import OCR

# Initialize the OCR object
ocr = OCR(tesseract_cmd='/usr/local/bin/tesseract')  # Specify the Tesseract path if needed
```

### 2. Extract Text from an Image
Extract text from a single image file:

```python
# Extract text from an image
image_text = ocr.process_image('path/to/your/image.png')
print("Text from image:", image_text)
```

### 3. Extract Text from a PDF
Extract text from a PDF document, with each page being processed individually:

```python
# Extract text from a PDF file
pdf_text = ocr.process_pdf('path/to/your/document.pdf')
print("Text from PDF:", pdf_text)
```

### 4. Enhance an Image
Enhance an image to improve OCR accuracy. This is particularly useful for low-quality images.

```python
ocr.enhance_image('path/to/image.png', 'path/to/enhanced_image.png')
```

### 5. Extract Text from an Enhanced Image
Enhance an image and then extract text from it:

```python
enhanced_text = ocr.process_image_with_enhancement('path/to/your/image.png')
print("Text from enhanced image:", enhanced_text)
```

### 6. Batch Processing
Process multiple images and PDF files in one go:

```python
files = ['path/to/image1.png', 'path/to/document.pdf']
batch_results = ocr.process_batch(files)
for file, text in batch_results.items():
    print(f"Text from {file}: {text}")
```

## Dependencies
**One Two OCR** relies on several Python libraries:

- **pytesseract**: Interface to Tesseract OCR.
- **pdf2image**: Converts PDF pages into images.
- **Pillow**: Python Imaging Library for handling image files.
- **opencv-python**: Image processing and enhancement.
- **numpy**: Supports advanced image processing.

These dependencies will be installed automatically when you install the library.

## Running Tests
The library comes with unit tests to validate its functionality. To run the tests, navigate to the root directory of the project and execute:

```sh
python -m unittest discover tests
```

This command will run all available tests and help ensure that everything is working as expected.

## Contributing
We welcome contributions to improve **One Two OCR**! If you would like to contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License
This library is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as per the terms of the license.

## Contact

For questions or issues, feel free to reach out:

- **Author**: Sergei Poluektov
- **Email**: [seregatipich@outlook.com](mailto:seregatipich@outlook.com)
- **GitHub**: [seregatipich](https://github.com/seregatipich)

---

Thank you for choosing **One Two OCR**! We hope it makes your text extraction tasks easier and faster. Happy coding!
