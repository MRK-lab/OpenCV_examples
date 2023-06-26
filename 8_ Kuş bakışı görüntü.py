import cv2
import numpy as np

img= cv2.imread("yayla.JPG")


pts1=np.float32([[432,479],[453,435],[793,478],[802,437]])
print(pts1)
#432:479,453:435,793:478,802:437

width,height=800,400 # bakmak istediğiniz objenin tahmini boyutu
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix= cv2.getPerspectiveTransform(pts1,pts2)
output=cv2.warpPerspective(img,matrix,(width,height))

cv2.circle(img,(432,479),5,(255,0,0),cv2.FILLED)
# eğitimde pts1[0][0],pts1[0][1] bu şekilde yazılıyor başlangıç konumu ama bende hata alıyorum BAKILACAK

cv2.circle(img,(453,435),5,(255,0,0),cv2.FILLED)
cv2.circle(img,(793,478),5,(255,0,0),cv2.FILLED)
cv2.circle(img,(802,437),5,(255,0,0),cv2.FILLED)



cv2.imshow("Resim",img)
cv2.imshow("Kus bakisi",output)
cv2. waitKey(0)
