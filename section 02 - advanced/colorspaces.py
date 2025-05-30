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

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
cv.imshow('Gray', gray)

#BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

cv.waitKey(0)
cv.destroyAllWindows()