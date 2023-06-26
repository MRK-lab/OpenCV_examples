import cv2

resim=cv2.imread("LOGOO_3.png")
resim2=cv2.imread("mrk_gri.png")

#cv2.imwrite("mrk_gri.png",resim)

cv2.imshow("mrk",resim)
cv2.imshow("mrk2",resim2)

cv2.waitKey(2000)
cv2.destroyAllWindows()
