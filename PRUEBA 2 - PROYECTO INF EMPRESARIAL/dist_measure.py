import numpy as np
import cv2

# Define object specific variables
dist = 0
focal = 450
pixels = 30
width = 5

# Find the distance from the camera
def get_dist(rectange_params, image):
    # Find number of pixels covered
    pixels = rectange_params[1][0]
    print(pixels)
    # Calculate distance
    dist = (width * focal) / pixels

    # Write on the image
    image = cv2.putText(image, 'Distance from Camera in CM :', org, font,
                        1, color, 2, cv2.LINE_AA)

    image = cv2.putText(image, str(dist), (110, 50), font,
                        fontScale, color, 1, cv2.LINE_AA)

    return image

# Extract Frames
cap = cv2.VideoCapture(0)

# Basic constants for OpenCV functions
kernel = np.ones((3, 3), 'uint8')
font = cv2.FONT_HERSHEY_SIMPLEX
org = (0, 20)
fontScale = 0.6
color = (0, 0, 255)
thickness = 2

cv2.namedWindow('Object Dist Measure', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Object Dist Measure', 700, 600)

# Loop to capture video frames
while True:
    ret, img = cap.read()

    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Predefined mask for red color detection
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Remove extra garbage from image
    d_img = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=5)

    # Find the histogram
    cont, hierarchy = cv2.findContours(d_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cont = sorted(cont, key=cv2.contourArea, reverse=True)[:1]

    for cnt in cont:
        # Check for contour area
        if (cv2.contourArea(cnt) > 100 and cv2.contourArea(cnt) < 306000):
            # Draw a rectangle on the contour
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int32(box)
            cv2.drawContours(img, [box], -1, (255, 0, 0), 3)

            img = get_dist(rect, img)

    cv2.imshow('Object Dist Measure', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()