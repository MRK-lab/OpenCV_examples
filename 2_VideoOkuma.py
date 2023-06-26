import cv2

feameWidth=640
frameHeight=360

cap=cv2.VideoCapture("Mehmet Vuruş.mp4")
#0: kendi kamerası
#1: ek kamera

while True:
    success,img=cap.read()
    img=cv2.resize(img,(feameWidth,frameHeight))
    cv2.imshow("video1",img)

    if cv2.waitKey(25) & 0XFF ==ord("q"):
        break


cv2.destroyAllWindows
