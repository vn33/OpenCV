import cv2 as cv
img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=2)
cv.imshow('dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=2)
cv.imshow('eroded', eroded)

# Resize
resized = cv.resize(img, (300, 300), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)