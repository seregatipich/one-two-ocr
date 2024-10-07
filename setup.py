from setuptools import setup, find_packages

setup(
    name="one-two-ocr",
    version="0.1.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "pytesseract==0.3.10",
        "pdf2image==1.16.3",
        "Pillow==9.0.1",
        "opencv-python==4.5.5.64",
        "numpy>=1.21.0,<2.0.0",
    ],
    author="Sergei Poluektov",
    author_email="seregatipich@outlook.com",
    description="A simple OCR library for processing images and PDFs.",
    url="https://github.com/seregatipich/one-two-ocr",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
