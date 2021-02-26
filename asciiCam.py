from asciifyimage import asciify
import sys
import time
import timeit
import numpy as np
import os
import pyfakewebcam
from ascii2img import convert
from PIL import Image
import cv2

cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('rickroll.mpg')
cam = pyfakewebcam.FakeWebcam('/dev/video2', 1280, 720)
cam.print_capabilities()

while(True):
	t1 = timeit.default_timer()
	t3 = timeit.default_timer()
	ret, frame = cap.read()
	textfile = open("content.txt", "w+")
	a = textfile.write(asciify(frame))
	textfile.close()
	t4 = timeit.default_timer()
	print('Grab frame and convert to ascii time: {}'.format(t4-t3))
	t3 = timeit.default_timer()
	convert("content.txt")
	t4 = timeit.default_timer()
	print('text2img time: {}'.format(t4-t3))
	c = os.path.getsize('content.jpeg')
	print('Image size: ', c)
	t3 = timeit.default_timer()
	im0 = np.array(Image.open("content.jpeg"))
	cam.schedule_frame(im0)
	t4 = timeit.default_timer()
	print('write to cam time: {}'.format(t4-t3))
	t2 = timeit.default_timer()
	print('exec time per frame: {} \n\n'.format(t2-t1))
	#time.sleep(1./24.)

cap.release()
cv2.destroyAllWindows()



