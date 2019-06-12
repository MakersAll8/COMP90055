To use the YOLOv3 implementation to test predictions, cd into the darknet directory and execute
./darknet detect alprv3/yolov3.cfg alprv3/weights/yolov3_1000.weights alprv3/images/38.jpg
There are three arguments after detect. The first one is the relative path from the darknet root directory to the YOLOv3 model file. The second argument is the relative path to trained weights. The last is the relative path to the test image. Note that the absolute path can be used as well. In case an exception called AssertionError occurs, cd into darknet/utils from the darknet root and modify the loader.py file. Locate the line that contains offset = 16, and change the value to 20. The AssertError often looks like the following: AssertError: expect X bytes, found Y bytes. The difference between X and Y is 4 bytes.

To start the application, cd into the DemoHyperAPL directory and type
python3 license_recognition.py
The application should start up a window that streams live webcam feeds. Recognized license plate numbers are printed to the upper left corner of the window. Note that reflection from the computer screen could degrade the performance of the ALPR system.

To rename all jpg files in a directory to license plate numbers recognized from the image. Modify the img_dir variable on line 6 of namePhoto.py and type
python3 namePhoto.py
If a Chinese LP is recognized, the jpg file will be renamed to the LP numbers.


Weights binaries cannot be uploaded to GitHub. Please download from Google Drive links below.

https://drive.google.com/file/d/1sliOgM612Qb9Wn2BKi-F2CIDdIvSR4P8/view?usp=sharing

https://drive.google.com/file/d/1JrrjpxF0Hcu8DM22hNblwRtJbdarG_MI/view?usp=sharing
