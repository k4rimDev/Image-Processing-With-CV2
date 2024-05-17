import cv2
from matplotlib import pyplot as plt
import numpy as np

# Load image 
image = cv2.imread('images/chess.jpg')
# Grayscaling
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 10))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# CornerHarris function  want input to be float
gray = np.float32(gray)
h_corners = cv2.cornerHarris(gray, 3, 3, 0.05)
kernel = np.ones((7, 7), np.uint8)
h_corners = cv2.dilate(h_corners, kernel, iterations=10)
image[h_corners > 0.024 * h_corners.max()] = [255, 128, 128]  # Corrected the color value
plt.subplot(1, 1, 1)
# Final Output
plt.imshow(image)
plt.show()
