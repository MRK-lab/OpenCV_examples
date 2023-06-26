import cv2
import numpy as np

cv2.namedWindow("resim",cv2.WINDOW_NORMAL) # resami kenarlaedan ayarlamak için
def mausePoints(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


img= cv2.imread("Cypher.png")
cv2.imshow("resim",img)

cv2.setMouseCallback("resim",mausePoints)
 
cv2.waitKey(0)
