import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('images/shapes.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(20, 20))
plt.subplot(2, 2, 1)
plt.title("Original")
plt.imshow(image)

# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Canny edges
edged = cv2.Canny(gray, 30, 200)
plt.subplot(2, 2, 2)
plt.title("Canny Edges")
plt.imshow(edged)

# Finding Contours
contours, hier = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
plt.subplot(2, 2, 3)
plt.imshow(edged)
print("Count of Contours  = " + str(len(contours)))

# All contours
image_contours = np.copy(image)
cv2.drawContours(image_contours, contours, -1, (0, 255, 0), 3)
plt.subplot(2, 2, 4)
plt.title("Contours")
plt.imshow(image_contours)

plt.show()
