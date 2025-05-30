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

cv.waitKey(0)
cv.destroyAllWindows()