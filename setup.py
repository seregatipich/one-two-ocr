from setuptools import find_packages, setup

setup(
    name="one_two_ocr",
    version="0.1.0",
    description="A package for extracting text from PDF documents using OCR.",
    author="Sergei Poluektov",
    author_email="seregatipich@outlook.com",
    packages=find_packages(),
    install_requires=["numpy", "opencv-python", "Pillow", "PyMuPDF", "logging"],
    entry_points={
        "console_scripts": [
            "one-two-ocr=one_two_ocr.cli:main",
        ],
    },
)
