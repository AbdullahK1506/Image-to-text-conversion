# Image to Text with OCR and Annotation
This project performs Optical Character Recognition (OCR) on an image using Tesseract and OpenCV. It extracts text from the image, draws bounding boxes around detected words, and saves the annotated image.

## Features
* Extracts text from an image using Tesseract OCR
* Uses OpenCV to:
  * Draw bounding boxes around recognized words
  * Annotate the image with the recognized text
* Saves the output as an annotated image

## Requirements
Install the following libraries (if not already installed):

```
pip install pytesseract opencv-python pillow
```

You also need to install Tesseract OCR on your system and ensure it’s accessible from the command line.
* For Windows: [https://github.com/tesseract-ocr/tesseract](https://github.com/tesseract-ocr/tesseract)
* For Ubuntu: `sudo apt install tesseract-ocr`

## Usage
1. Place the target image in the same directory and rename it to `image.jpg`.
2. Run the script:

```
python image_to_text.py
```

3. The script will:
   * Print extracted words to the terminal.
   * Create and save an annotated image as `annotated_image.jpeg`.

## Configuration
The Tesseract OCR is configured with:

```
myconfig = r"--psm 11 --oem 3"
```

* `--psm 11`: Sparse text with OSD.
* `--oem 3`: Default OCR engine mode.
You can tweak these settings for better accuracy depending on your image type.

## Output
* `annotated_image.jpeg`: Image with bounding boxes and detected text.
* Console output: Prints each recognized word with confidence > 1.

## Notes
* The code is currently designed to read `image.jpg` only.
* Modify the filename if working with different images.
* Can be extended to extract line-level or character-level boxes.

