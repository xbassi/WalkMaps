import numpy as np
import cv2

from darknet.python.darknet import *

cap = cv2.VideoCapture("khadims.avi")
ret, img = cap.read()
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
net = load_net(b"darknet/yolov3.cfg", b"darknet/yolov3.weights", 0)
meta = load_meta(b"darknet/coco.data")
# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
p = 0

points = []

while(1):

    ret, img = cap.read()

    if img is None:
        break

    if ret:
        p += 1

        if p % 5 == 0:

            img = cv2.resize(img,(608,608))
            # r = detect_np(net, meta, img)
            r = detect(net, meta, img)

            # print(r)

            for i in r:
                if i[0].decode() == "person":

                    x, y, w, h = i[2][0], i[2][1], i[2][2], i[2][3]

                    # points.append([x+(w/2),y+h])

                    xmin, ymin, xmax, ymax = convertBack(float(x), float(y), float(w), float(h))

                    points.append([xmin+((xmax-xmin)/2),ymax])

                    # pt1 = (xmin, ymin)
                    # pt2 = (xmax, ymax)
                    # cv2.rectangle(img, pt1, pt2, (0, 255, 0), 2)
                    # cv2.putText(img, i[0].decode() + " [" + str(round(i[1] * 100, 2)) + "]", (pt1[0], pt1[1] + 20), cv2.FONT_HERSHEY_SIMPLEX, 1, [0, 255, 0], 4)
            
            print("Frame: ",p,end="\r")
            # cv2.imwrite("out/"+str(p).zfill(7)+".png",img)



np.savez("points.npz",data=points)