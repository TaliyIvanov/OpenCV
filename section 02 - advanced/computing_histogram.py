import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/doomguy.png')

def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = rescaleFrame(img)
# cv.imshow('Original', img)



# Grayscale histogram
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray_hist = cv.calcHist([gray], [0], None, [256], [0, 256])

# cv.waitKey(0)
# cv.destroyAllWindows()

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()


# BGR Histogram
colors = ['b','g','r']
for i, col in enumerate(colors):
    bgr_hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(bgr_hist, color=col)
    plt.xlim([0,256])

plt.show()