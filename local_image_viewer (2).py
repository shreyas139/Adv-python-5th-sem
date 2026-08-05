import cv2
import os

# Ask user for image path
image_path = input("Enter the full image path: ").strip().strip('"')

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: File not found!")
    exit()

# Read the image
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Unable to open the image. Make sure it's a valid image file.")
    exit()

# Display the image
cv2.imshow("Image Viewer", image)

print("Press any key to close the image window...")
cv2.waitKey(0)
cv2.destroyAllWindows()