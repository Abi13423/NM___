import cv2
import easyocr

# Load the image
image_path = "car.jpg"  # Replace with your image file
image = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Load OCR reader
reader = easyocr.Reader(['en'])

# Run OCR on the image
results = reader.readtext(gray)

# Loop through detected text areas
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))

    # Draw bounding box and text
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                0.9, (255, 0, 0), 2)

# Display the result
cv2.imshow("Detected Plate", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
