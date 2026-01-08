import cv2
# Noise reduction and diff types of filtering and blur

# Load image
img = cv2.imread("document.jpg")

# Apply Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5,5), 0)

# Apply Median Filtering
median = cv2.medianBlur(img, 5)

# Apply Bilateral Filtering
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

# Show results
cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Filtering", median)
cv2.imshow("Bilateral Filtering", bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()