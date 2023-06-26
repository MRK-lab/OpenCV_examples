import cv2
import numpy as np

img1= cv2.imread("Chamber.png")
img2= cv2.imread("Cypher.png")

print(img1.shape)
print(img2.shape)

img1= cv2.resize(img1,(0,0), None, 0.5, 0.5)
img2= cv2.resize(img2,(0,0), None, 0.5, 0.5)

img1= cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

y= np.hstack((img1, img2))
d= np.vstack((img1, img2))

cv2.imshow("Dikey",d)
cv2.imshow("Yatay",y)

cv2.waitKey(0)
cv2.destroyAllWindows()
