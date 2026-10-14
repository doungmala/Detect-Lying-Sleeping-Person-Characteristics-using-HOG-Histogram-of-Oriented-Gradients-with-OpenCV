from typing import no_type_check
import cv2
import numpy as np

img = cv2.imread('243306778_4466272430100027_5893355157568901317_n.jpg')
img1 = cv2.imread('243306778_4466272430100027_5893355157568901317_n.jpg',0)

cv2.imshow('image', img)
cv2.imshow('image1', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()



