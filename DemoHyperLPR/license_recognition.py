from hyperlpr import *
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import threading

from Plate import Plate

b, g, r, a = 255, 0, 0, 0
font_path = "./simsun.ttc"
font = ImageFont.truetype(font_path, 30)
plate = Plate()


try:
    cap = cv2.VideoCapture(0)
    while True:
        # create a timer that resets plate number if not updated within 2 seconds
        timer = threading.Timer(2, plate.reset())

        # Get webcam images
        ret, frame = cap.read()

        # recognize plate using HyperLPR
        recognitionResult = HyperLPR_PlateRecogntion(frame)

        # if at least one plate is recognized
        if len(recognitionResult) > 0:
            maxConfidence = 0
            maxRow = 0
            # identify the result with the highest confidence
            for i in recognitionResult:
                if i[1] > maxConfidence:
                    maxConfidence = i[1]
                    maxRow = i

            if maxConfidence > 0.92:
                timer.cancel()
                plate.update_plate(maxRow[0])
                plate.update_location(maxRow[2])
                # if another plate is not read within 2 seconds, reset plate to empty
                timer.start()

        # if plate number is not reset to None, report it, otherwise, just show the webcam image
        if plate.plateNumber != 0:
            # drawing a filled white rectangle
            cv2.rectangle(frame, (10, 10), (150, 50), (255, 255, 255), thickness=cv2.FILLED)

            # drawing plate number inside white rectangle
            frame = Image.fromarray(frame)
            draw = ImageDraw.Draw(frame)
            draw.text((15, 15), plate.plateNumber, font=font, fill=(b, g, r, a))
            frame = np.array(frame)

        cv2.imshow('License Recognition', frame)

        if cv2.waitKey(1) == 13:  # 13 is the Enter Key
            break

    cap.release()
    cv2.destroyAllWindows()
except cv2.error as e:
    print("failed to read from webcam")
    exit(1)
