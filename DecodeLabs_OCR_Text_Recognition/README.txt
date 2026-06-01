# Project 4: DecodeLabs OCR Text Recognition System

## Overview

This project is a basic OCR text recognition system developed using Python. The system loads an image, applies preprocessing techniques, and extracts readable text from the image using Tesseract OCR.

OCR stands for Optical Character Recognition. It allows the computer to recognize text from images and convert it into machine-readable text.

## Features

- Loads an image from the project folder
- Checks if the image file exists
- Converts the image to grayscale
- Applies thresholding to improve text visibility
- Extracts text using OCR
- Calculates average OCR confidence
- Draws bounding boxes around detected text
- Saves the processed image
- Saves the final image with detected text boxes
- Displays extracted text clearly in the terminal

## Technologies Used

- Python
- OpenCV
- pytesseract
- Pillow
- Tesseract OCR Engine

## Concepts Used

- Image processing
- OCR text recognition
- Grayscale conversion
- Thresholding
- Text extraction
- Confidence calculation
- Bounding boxes
- File handling
- Error handling

## Installation

Install the required Python libraries:

```bash
py -m pip install opencv-python pytesseract pillow
```

You also need to install the Tesseract OCR engine on your computer.

After installation, the default Windows path is usually:

```text
C:\Program Files\Tesseract-OCR\tesseract.exe
```

The Python code should include:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## Project Files

The project folder should contain:

```text
DecodeLabs_OCR_Text_Recognition
│
├── decodelabs_ocr_recognition.py
├── sample_text.png
├── processed_image.png
└── ocr_detected_text.png
```

`processed_image.png` and `ocr_detected_text.png` are generated after running the program.

## How to Run

```bash
python decodelabs_ocr_recognition.py
```

or:

```bash
py decodelabs_ocr_recognition.py
```

When asked, enter the image file name:

```text
sample_text.png
```

## Example Output

```text
Image loaded successfully.
Processed image saved as: processed_image.png

Extracted Text:
--------------------
DecodeLabs Artificial Intelligence Internship
Project 4 OCR Recognition
--------------------

Average OCR Confidence: 91.45 %
Detected text image saved as: ocr_detected_text.png

OCR recognition completed.
```

## Project Purpose

The purpose of this project is to understand how AI can process visual input. It demonstrates how images can be preprocessed and passed to an OCR engine to recognize and extract text.

## Notes

The OCR result depends on the quality of the image. Clear printed text usually gives better results than blurry, handwritten, or low-contrast images.