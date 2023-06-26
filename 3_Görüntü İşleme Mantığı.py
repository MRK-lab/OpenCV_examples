import cv2

resim=cv2.imread("monster.jpg")

print(resim)
print(type(resim))
print(resim.shape)
print(resim.size)
print("\nGri tonlar")
resim=cv2.imread("monster.jpg",0)
print(resim.shape)
print(resim.size)
print(resim.dtype)

print("\npikseldeki renk kodunu almak")
resim=cv2.imread("monster.jpg")
print(resim.item(1,1,0)) #blue
print(resim.item(1,1,1)) #green
print(resim.item(1,1,2)) #red

cv2.imshow("cerceve",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
