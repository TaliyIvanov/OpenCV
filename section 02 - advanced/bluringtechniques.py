import cv2 as cv
import numpy as np

img = cv.imread('images/doomguy.png')

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)
cv.imshow('Original', img)

# we have a window with 9 pixels
# pixel in a center is average from 8 other pixels

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average', average)

# Gaussian Blur
gaus_blur = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gaus_blur)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral
bilat = cv.bilateralFilter(img, 5,15,15)
cv.imshow('Bilateral', bilat)

cv.waitKey(0)
cv.destroyAllWindows()