import numpy as np
import cv2

from darknet.python.darknet import *

cap = cv2.VideoCapture("khadims.avi")

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	if frame is None:
		break

	frame = cv2.resize(frame,(512,512))

	# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	cv2.imshow('frame',frame)

	net = load_net(b"darknet/cfg/yolov3.cfg", b"darknet/yolov3.weights", 0)
	meta = load_meta(b"darknet/cfg/coco.data")
	r = detect_np(net, meta, img)

	print(r)
	exit()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


cap.release()
cv2.destroyAllWindows()