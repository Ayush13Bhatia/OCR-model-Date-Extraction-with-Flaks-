#!/usr/bin/env python
# coding: utf-8

# Importing Libraries
import cv2
import numpy as np
import pytesseract as tess
from PIL import Image
import os
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
import re
import pickle

# Extracting the text data from image
files = []
texts = []
for file in os.listdir("images/"):
            
            print(file)
            files.append(file)
            img = cv2.imread(file)
            
            #apply dilation and erosion to remove some noise
            kernel = np.ones((1, 1), np.uint8)
            im = cv2.dilate(img, kernel, iterations = len(file))
            im = cv2.dilate(img, kernel, iterations = len(file))

            #write image after removed noise        
            cv2.imwrite(file, img)

            # Recognize tex with tesseract for python
            tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            img = Image.open(f"images/{file}")
            text = tess.image_to_string(img)
            texts.append(text)
            print(f"'\n\n'Saving: {file}", f"image Size: {img.size}""\n\n")   
            print(text)
            
            
print(len(files))


# Extracting the date from Extracted text data
datelist= []

for i in texts: 
   date =  re.findall('\d{4}-\d{2}-\d{2}|\d{1,2}/\d{2}/\d{4}|\d{1,2}-\d{2}-\d{4}|\d{1,2}-\d{1,2}-\d{2}|\d{1,2}\/\d{1,2}\/\d{2}|[\d]{1,2}-[ADFJMNOS]\w*-[\d]{4}|[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4}', i)  
   datelist.append(date)
   print(f"'\n\n'File_name: {file}",'\n\n' f"Extract Date: {date}""\n\n")
   


print(len(datelist))

# Displaying the date except the null values
Expense_date = []
for i in texts: 
    date =  re.finditer('\d{4}-\d{2}-\d{2}|\d{1,2}/\d{2}/\d{4}|\d{1,2}-\d{2}-\d{4}|\d{1,2}-\d{1,2}-\d{2}|\d{1,2}\/\d{1,2}\/\d{2}|[\d]{1,2}-[ADFJMNOS]\w*-[\d]{4}|[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4}', i)
    
    for match in date:
        Expense_date.append(match)
        print(match.group(0)) 
print(len(Expense_date))

# Gathing the available data into dictionary form
dictdate={}
y = 0
for x in files:
    dictdate[x]=datelist[y]
    y+=1
    print(x)

print(dictdate)

print(len(Expense_date))

# Finding the accuracy of Extracted data
accuracy = len(Expense_date)/len(files)*100
print(accuracy)


# Making a pickle file that will interact with Flask

pickle.dump(dictdate, open('model.pkl', 'wb'))
model = pickle.load(open('model.pkl', 'rb'))
print(model)



