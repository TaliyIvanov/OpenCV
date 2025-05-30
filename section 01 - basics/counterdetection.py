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

# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny', canny)


# Let's find contours
# counters, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f"Counters count: {len(counters)}") # return 1426

# Let's blur image and try again)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# canny_blur = cv.Canny(blur, 125, 175)
# cv.imshow('Canny', canny_blur)

# counters_blur, hierarchies_blur = cv.findContours(canny_blur, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f"Blur counters count: {len(counters_blur)}") # return 260

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
counters, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f"Counters count: {len(counters)}") # return 1426
cv.imshow('thresh', thresh)

cv.waitKey(0)
cv.destroyAllWindows()