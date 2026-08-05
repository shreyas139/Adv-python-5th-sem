import cv2
import numpy as np

# Create a blank color image (300x400)
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Fill each horizontal strip with a different color (BGR format)

img[0:50, :] = 0      #black
img[50:100, :] = 50    #dark grey
img[100:150, :] = 100    #grey
img[150:200, :] = 150   # light grey
img[200:250, :] = 200   # very light grey
img[250:300, :] = 255  # white


# Display the image
cv2.imshow("Different Colors", img)

cv2.waitKey(0)
cv2.destroyAllWindows()