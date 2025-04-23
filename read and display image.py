import cv2
img = cv2.imread(r"C:\Users\CSE\Downloads\ktm.jpg")
cv2.imshow("bike", img)
height = img.shape[0]
width = img.shape[1]
print("Height of Image:", height)
print("Width of Image:", width)
cv2.waitKey(0)