# Standard imports
import cv2
import numpy as np
from PIL import Image

# Path to your image
img_path = "outamation/document.jpg"

# 1️⃣ OpenCV: Load the image
img_cv = cv2.imread(img_path)

# ⛔️ Only for non-Colab (won’t work in notebooks)
# cv2.imshow("OpenCV Image", img_cv)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 2️⃣ PIL (Pillow): Load the image
img_pil = Image.open(img_path)

# ⛔️ Only for non-Colab
# img_pil.show()


# 3️⃣ NumPy: Convert image to array and print shape
img_np = np.array(img_pil)
print("NumPy Image Shape:", img_np.shape)