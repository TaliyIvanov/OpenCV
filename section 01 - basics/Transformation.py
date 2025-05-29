import cv2 as cv
import numpy as np

img = cv.imread('images/doomguy.png')
img = cv.resize(img, (720,360))
cv.imshow('original', img)


# Translation
def translate(img, x ,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0]) # weight and height
    return cv.warpAffine(img, transMat, dimensions)

# negative x --> Left
# positive x --> Right
# negative y --> Up
# positive y --> Down

translated = translate(img, 100, 200)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (height//2,width//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 75)
cv.imshow('Rotated', rotated)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flipped = cv.flip(img, -1)
cv.imshow('Flipped', flipped)

cv.waitKey(0)
cv.destroyAllWindows()