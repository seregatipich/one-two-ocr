from setuptools import find_packages, setup

setup(
    name="ocr",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytesseract==0.3.10",
        "pdf2image==1.16.3",
        "Pillow==9.0.1",
        "opencv-python==4.5.5.64",
        "numpy==1.21.5",
    ],
    entry_points={"console_scripts": ["ocr=ocr:main"]},
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple OCR library for processing images and PDFs.",
    url="https://github.com/yourusername/ocr",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
