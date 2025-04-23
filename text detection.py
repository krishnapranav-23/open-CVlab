import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image_path = r"C:\Users\CSE\Downloads\alphabets.jpg"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError(f"Could not load image from: {image_path}")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(thresh, config=custom_config)

print("Detected Text:\n", text)

cv2.imshow("Processed Image", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
