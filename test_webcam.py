import cv2
import numpy as np

vid = cv2.VideoCapture(0)
i=0
while(True):
    ret, frame = vid.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    cv2.imwrite('img/' + 'ns0' + str(i) + '.jpg',frame)
    i+=1

vid.release()
cv2.destroyAllWindows()

    