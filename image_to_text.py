# -*- coding: utf-8 -*-
"""
Created on Thu April  23 20:58:13 2024


"""
# importing required libraries and modules
import pytesseract
import PIL
import cv2
from PIL import Image
from pytesseract import Output

# text extraction
myconfig = r"--psm 11 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open('image.jpg'),config=myconfig)
#print(text)

# image processing part(opencv library is used for this)

img = cv2.imread("image.jpg")
height, width, _ = img.shape

# box around individual letter
#boxes = pytesseract.image_to_boxes(img, config = myconfig)
#print(boxes)
#for box in boxes.splitlines():
#    box = box.split(" ")
#    img = cv2.rectangle(img, (int(box[1]), height-int(box[2])), (int(box[3]), height-int(box[4])), (0,255,0), 2 )


data = pytesseract.image_to_data(img, config = myconfig, output_type = Output.DICT)
#print(data.keys())
#print(data['text'])


# box around complete word
amount_boxes = len(data['text'])
for i in range(amount_boxes):
    if float(data['conf'][i]) > 1:
        (x,y,width,height) = (data['left'][i], data['top'][i], data['width'][i], data['height'][i])
        img = cv2.rectangle(img, (x,y), (x+width, y+height), (0,255,0), 2)
        img = cv2.putText(img, data['text'][i], (x,y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, cv2.LINE_AA)
        print(data['text'][i])

# save the processed output
cv2.imwrite("annotated_image.jpeg", img)


