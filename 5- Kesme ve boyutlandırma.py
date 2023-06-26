import cv2

path="resim.jpg"

img = cv2.imread(path)
print(img.shape) # normal boyut

width,height=800,800
imgRes = cv2.resize(img,(width,height)) # önbce genişlik sonra yükseklik
print(imgRes.shape) # düzenlenmiş boyut

imgCrop= imgRes[200:400,400:600] # önce yükseklik sonra genişlik

imgCropRes= cv2.resize(imgCrop,(imgRes.shape[1],imgRes.shape[0]))

cv2.imshow("normal",img)
cv2.imshow("resize",imgRes)
cv2.imshow("crop",imgCrop)
cv2.imshow("cropRes",imgCropRes)

cv2.waitKey(0)
cv2.destroyAllWindows
