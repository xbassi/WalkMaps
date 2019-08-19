import numpy as np
import cv2
 
# load the image
image = cv2.imread("bg.png")
overlay = cv2.imread("out.png")


overlay = cv2.resize(overlay,(1280,720))


print(overlay.shape)
print(image.shape)


output = image.copy()

alpha = 0.6

cv2.addWeighted(overlay, alpha, output, 1 - alpha,0, output)


cv2.imwrite("merged.png",output)