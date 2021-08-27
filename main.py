import cv2
import pytesseract

img = cv2.imread('test.png')
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\Chandan\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'
raw_list = pytesseract.image_to_string(img).split("\n")
print("Character Detection Successful")

credits = {0:4, 1:4, 2:3, 3:3, 4:2.5, 5:1.5, 6:1, 7:1}
grade_values = {"s": 10, "ss":10, "a":9, "b":8, "c":7, "d":5, "e":4, "f":0}
#values = {0:"20MA110", 1:"20CH110", 2:"20CV110", 3:"20EC110", 4:"20ME120", 5:"20CH12L", 6:"20HU120", 7:"20HU130" }

processed_list1 = []
for i in raw_list:
    if "20" in i:
        processed_list1.append(i)

processed_list2 = []
for i in processed_list1:
    processed_list2.append(i.split(" "))


print("Text processing complete")

grades = []

for i in processed_list2:
    if i[-1].lower() in grade_values.keys():
        grades.append(i[-1].lower())

print("Grades Extraction Successful")

dict={i:grades[i] for i in range(len(grades))}

print("Grades dictionary generated")

sgpa_numerator = 0

for i in range(len(grades)):
    sgpa_numerator += grade_values[grades[i]]*credits[i]

sgpa = sgpa_numerator/20

print(f"Your SGPA is {sgpa}")