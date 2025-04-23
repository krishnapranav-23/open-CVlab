import cv2
import numpy as np
# Read the image
image = cv2.imread(r"C:\Users\CSE\Downloads\ktm.jpg")
# Check if the image is loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
    exit()
# Apply GaussianBlur to reduce noise and help edge detection
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
# Use Canny edge detection
edges = cv2.Canny(blurred_image, 50, 150) # Adjust the threshold values as needed
# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()