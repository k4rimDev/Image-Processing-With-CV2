import cv2
from matplotlib import pyplot as plt
import numpy as np

image = cv2.imread('images/messi.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height = 300
width = 500

plt.figure(figsize=(20, 20))
plt.subplot(2, 2, 1)
plt.title("Original")
plt.imshow(image)
hgt, wdt = image.shape[:2]
start_row, start_col = int(hgt * .25), int(wdt * .25)
end_row = start_row + height
end_col = start_col + width
cropped = image[start_row:end_row , start_col:end_col]

plt.subplot(2, 2, 2)
plt.imshow(cropped)
