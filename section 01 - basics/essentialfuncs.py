import cv2 as cv
import numpy as np

img = cv.imread('images/doomguy.png')
cv.imshow('original', img)
# create grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# Blur image
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (Canny Edge Detection)
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dilating the image
dilat = cv.dilate(canny, (3,3), iterations=1)
cv.imshow('Dilated', dilat)

# Eroding
eroded = cv.erode(dilat, (3,3), iterations=3)
cv.imshow('erod', eroded)

# Resize
resized = cv.resize(img, (500,500))
cv.imshow('resized', resized)

# Cropping
crop = img[50:500,30:500]
cv.imshow('cropped', crop)

cv.waitKey(0)
cv.destroyAllWindows()