import cv2
img =cv2.imread(r"C:\Users\CSE\Downloads\ktm.jpg")
cv2.imshow("bike.jpg", img)
cv2.imwrite("bike.png", img)
cv2.imwrite("bike.tiff", img)
cv2.imshow("bike.png", img)
cv2.imshow("bike.tiff", img)
cv2.waitKey(0)