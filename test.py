import cv2
import numpy as np
import imutils
img = cv2.imread('opencv_polygons_1.png')
img1=img
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

h = img.shape[0]
w = img.shape[1]

for y in range(0,h):
    for x in range(0,w):
        if img[y ,x] >= 50 and img[y,x] <= 150:
            img[y,x] = 255
        else:
            img[y,x] = 0

kernel=np.ones((5,5),np.uint8)
dilation=cv2.dilate(img,kernel,iterations=2)

kernel=np.ones((5,5),np.uint8)
erosion=cv2.erode(dilation,kernel,iterations=3)

contours = cv2.findContours(erosion, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours=imutils.grab_contours(contours)

for c in contours:
    x,y,w,h=cv2.boundingRect(c)
    
    last = erosion[y:y+h, x:x+w]

    cv2.imshow('last',last)
    cv2.waitKey(0)

    area = cv2.contourArea(c)
    equi_di = np.sqrt(4*area/np.pi)
    print('equi_di',equi_di)
    
    apporx=cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
    print('apporx',len(apporx))
    cv2.putText(img1, str(len(apporx)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

 

print('aa', len(contours))

cv2.imshow('img',img)
cv2.imshow('img1',img1)
cv2.imshow('dilation',dilation)
cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()

