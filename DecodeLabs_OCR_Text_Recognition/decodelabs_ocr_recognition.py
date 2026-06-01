# -------------------------------------------------
# Project 4: DecodeLabs OCR Text Recognition System
# -------------------------------------------------
# This project implements a basic text recognition system using Python.
# The system loads an image, applies preprocessing techniques, and uses
# OCR to extract readable text from the image.
#
# The project demonstrates:
# - Image loading
# - Grayscale conversion
# - Image thresholding
# - OCR text extraction
# - OCR confidence calculation
# - Bounding boxes around detected text
# - Clear output display
# -------------------------------------------------

import cv2
import pytesseract
from PIL import Image
import os


# -------------------------------------------------
# 1. Set Tesseract OCR path
# -------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# -------------------------------------------------
# 2. Get image path from user
# -------------------------------------------------

image_path = input("Enter image file name, for example sample_text.png: ").strip()


# -------------------------------------------------
# 3. Check if image exists
# -------------------------------------------------

if not os.path.exists(image_path):
    print("Error: Image file not found.")
    print("Please make sure the image is in the same folder as this Python file.")

else:
    # -------------------------------------------------
    # 4. Load the image
    # -------------------------------------------------

    image = cv2.imread(image_path)

    if image is None:
        print("Error: Could not read the image file.")
    else:
        print("\nImage loaded successfully.")

        # -------------------------------------------------
        # 5. Convert image to grayscale
        # -------------------------------------------------

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # -------------------------------------------------
        # 6. Apply thresholding
        # -------------------------------------------------

        threshold_image = cv2.threshold(
            gray_image,
            0,
            255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )[1]

        # -------------------------------------------------
        # 7. Save the processed image
        # -------------------------------------------------

        processed_image_path = "processed_image.png"
        cv2.imwrite(processed_image_path, threshold_image)

        print("Processed image saved as:", processed_image_path)

        # -------------------------------------------------
        # 8. Extract text using OCR
        # -------------------------------------------------

        extracted_text = pytesseract.image_to_string(
            Image.open(processed_image_path)
        )

        print("\nExtracted Text:")
        print("--------------------")

        if extracted_text.strip() == "":
            print("No text was detected. Try using a clearer image.")
        else:
            print(extracted_text)

        print("--------------------")

        # -------------------------------------------------
        # 9. Get OCR data and confidence values
        # -------------------------------------------------

        ocr_data = pytesseract.image_to_data(
            threshold_image,
            output_type=pytesseract.Output.DICT
        )

        confidence_values = []

        for confidence in ocr_data["conf"]:
            try:
                confidence = int(confidence)

                if confidence > 0:
                    confidence_values.append(confidence)

            except ValueError:
                pass

        if len(confidence_values) > 0:
            average_confidence = sum(confidence_values) / len(confidence_values)
            print("Average OCR Confidence:", round(average_confidence, 2), "%")
        else:
            print("Average OCR Confidence: Not available")

        # -------------------------------------------------
        # 10. Draw bounding boxes around detected text
        # -------------------------------------------------

        output_image = image.copy()

        for i in range(len(ocr_data["text"])):
            detected_text = ocr_data["text"][i].strip()

            if detected_text != "":
                x = ocr_data["left"][i]
                y = ocr_data["top"][i]
                w = ocr_data["width"][i]
                h = ocr_data["height"][i]

                cv2.rectangle(
                    output_image,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

        detected_image_path = "ocr_detected_text.png"
        cv2.imwrite(detected_image_path, output_image)

        print("Detected text image saved as:", detected_image_path)

        # -------------------------------------------------
        # 11. Final message
        # -------------------------------------------------

        print("\nOCR recognition completed.")