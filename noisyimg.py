import cv2

img = cv2.imread("noisyimg.jpg", cv2.IMREAD_GRAYSCALE)
if img is None:
    raise FileNotFoundError("noisyimg.jpg not found")

denoised = cv2.fastNlMeansDenoising(img, None, 12, 7, 21)

clahe = cv2.createCLAHE(clipLimit=1.2, tileGridSize=(16, 16))
contrast = clahe.apply(denoised)

cv2.imwrite("cleaned.png", contrast)

cv2.imshow("Original", img)
cv2.imshow("Cleaned", contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
