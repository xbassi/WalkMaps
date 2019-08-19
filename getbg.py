import cv2
import numpy as np
 
c = cv2.VideoCapture("../khadims.avi")
_,f = c.read()
 
avg1 = np.float32(f)
avg2 = np.float32(f)
 
p = 0
res2  =None
while(1):
    try :
        _,f = c.read()
         

        # cv2.accumulateWeighted(f,avg1,0.1)
        cv2.accumulateWeighted(f,avg2,0.01)
         
        # res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)
     
        # cv2.imshow('img',f)
        # cv2.imshow('avg1',res1)
        # cv2.imshow('avg2',res2)
        k = cv2.waitKey(20)
        
        print(p,end="\r")
        p += 1
        if k == 27:
            break
    except:
        break 
cv2.imwrite("bg.png",res2)

# cv2.destroyAllWindows()
# c.release()