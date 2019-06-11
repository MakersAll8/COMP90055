import cv2
import os

from hyperlpr import HyperLPR_PlateRecogntion

img_dir = "/home/ubuntu/Desktop/2019 Semester 1/Project/DemoHyperLPR/img/"

for filename in os.listdir(img_dir):
    print("Working on image: "+filename)
    if '.jpg' in filename:
        img = cv2.imread(img_dir + filename)
        recognitionResult = HyperLPR_PlateRecogntion(img)
        maxConfidence = 0
        maxRow = 0
        imageName = 'default'
        # identify the result with the highest confidence
        for i in recognitionResult:
            if i[1] > maxConfidence:
                maxConfidence = i[1]
                maxRow = i

        if maxConfidence > 0.8:
            imageName = maxRow[0]
            os.rename(img_dir+filename, img_dir+imageName+'.jpg')
