import cv2

# Load the MRI image in grayscale
image = cv2.imread("MRI_image.png", cv2.IMREAD_GRAYSCALE)

# Resize for uniformity (optional)
image = cv2.resize(image, (256, 256))

# Apply Gaussian Blur to remove noise
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Apply binary thresholding to segment tumor
_, thresholded = cv2.threshold(blurred, 45, 255, cv2.THRESH_BINARY)

# Show the original and segmented images
cv2.imshow("Original MRI", image)
cv2.imshow("Segmented Tumor", thresholded)

cv2.waitKey(0)
cv2.destroyAllWindows()
