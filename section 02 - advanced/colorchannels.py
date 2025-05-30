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

# Let's see what is the channels is
blue_cnah, green_chan, red_chan = cv.split(img)

# cv.imshow('BLUE', blue_cnah)
# cv.imshow('GREEN', green_chan)
# cv.imshow('RED', red_chan)

# it's look very interesting, but what if merged back channels?
channels_list = [blue_cnah, green_chan,red_chan]
merged = cv.merge(channels_list)
# cv.imshow('Merged', merged)

# print(img.sum() == merged.sum()) # return True

# How to create really RGB colors? Let's do it
# create the base blank
blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv.merge([blue_cnah, blank, blank])
green = cv.merge([blank, green_chan, blank])
red = cv.merge([blank, blank, red_chan])

cv.imshow('True Blue', blue)
cv.imshow('True Green', green)
cv.imshow('True Red', red)

cv.waitKey(0)
cv.destroyAllWindows()