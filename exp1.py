import cv2
import os

img = cv2.imread(os.path.join(os.path.dirname(__file__), "sample.jpeg"))

resized = cv2.resize(img, (400, 300))
blurred = cv2.GaussianBlur(resized, (5, 5), 0)
gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("original", img)
cv2.imshow("resized", resized)
cv2.imshow("blurred", blurred)
cv2.imshow("threshold", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()