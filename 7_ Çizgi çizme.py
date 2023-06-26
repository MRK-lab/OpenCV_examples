import cv2
import numpy as np

img= np.zeros((512,512,3), np.uint8)
img2= np.zeros((512,512,3), np.uint8)
img3= np.zeros((512,512,3), np.uint8)
img4= np.zeros((512,512,3), np.uint8)

print(img.shape)
print(img)

img[ : ] = 255,200,0 # bütün resmi boyuyor
img2[21:80, 55:85 ] = 255,0,0 # sadece seçili yeri boyuyor

cv2.line(img3, (0,0), (img3.shape[1],img3.shape[0]), (0,255,0), 3)
# çizgi çizme: resim, başlangış noktası, bitiş noktası, renk, kalınlık
# img.shape[1]: genişlik, diğeri yülseklik


cv2.rectangle(img4,(110,200),(450,100),(0,250,200),cv2.FILLED)
# cv2.FILLED : dikdörtgen içini doldurur. Kalınlık kısmına yazılır

cv2.circle(img4,(150,400),50,(255,255,56),3)
#daire çizer: resim, başlangıç noktası, yarıçap, renk, kalınlık

cv2.putText(img4,"mrk_kul",(150,150),cv2.FONT_HERSHEY_COMPLEX,1,(150,150,150),2)
# yazı yazma: resim, yazı, başlangıç noktası, yazı tipi, boyutu, renk, kalınlık 


cv2.imshow("kara resim",img)
cv2.imshow("kara resim2",img2)
cv2.imshow("cizgili resim",img3)
cv2.imshow("kare resim",img4)

cv2.waitKey(0)
