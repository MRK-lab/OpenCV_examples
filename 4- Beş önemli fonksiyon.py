import cv2
import numpy as np


path="resim.jpg"

img=cv2.imread(path)
img=cv2.resize(img,(500,500))

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBulur=cv2.GaussianBlur(img,(5,5),5)
imgCanny=cv2.Canny(imgBulur,200,200) # orjinal resimd eğilde buğulu olanı koymamın nedeni daha temiz gözükmesi

kernel=np.ones((5,5),np.uint8)
print(kernel)
imgGen=cv2.dilate(imgCanny,kernel,4)
imgDar=cv2.erode(imgGen,kernel,1)



cv2.imshow("orjinal",img)
cv2.imshow("gray",imgGray)
cv2.imshow("bulgulu", imgBulur)
cv2.imshow("canny", imgCanny)
cv2.imshow("genisletilmis",imgGen)
cv2.imshow("dar",imgDar)


cv2.waitKey(0)
cv2.destroyWindows()
