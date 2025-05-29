import cv2 as cv
import numpy as np


blank = np.zeros((500, 500, 3), dtype='uint8')

# img = cv.imread('images/doomguy.png')
# cv.imshow('doomguy', img)

# 1. Study the channels BGR 
## Copy blanks
# blue_blank = blank.copy()
# green_blank = blank.copy()
# red_blank = blank.copy()

# # change colors
# blue_blank[:] = 255,0,0
# green_blank[:] = 0,255,0 
# red_blank[:] = 0,0,255 

# cv.imshow('Blue', blue_blank)
# cv.imshow('Green', green_blank)
# cv.imshow('Red', red_blank)
# cv.imshow('blank', blank)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 2. Paint the Red Squre on black blank

# blank[:100, :100] = 255,0,0
# blank[100:200, 100:200] = 0,255,000
# blank[200:300, 300:400] = 0,0,255
# cv.imshow('blank', blank)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 3. Draw rectangle
# cv.rectangle(blank,pt1=(0,0),pt2=(250,250),color=(0,255,0),thickness=1)

# cv.imshow('WithRectangle', blank)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 4. Draw circle
# cv.circle(blank, center=(250,250), radius=150, color=(0,255,0), thickness=-1)
# cv.imshow('Circle', blank)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 5. Draw line
# cv.line(blank, pt1=(101,125), pt2=(400,450), color=(0,255,0),thickness=1)

# cv.imshow('Line', blank)

# cv.waitKey(0)
# cv.destroyAllWindows()

# 6 Write text
cv.putText(blank,
           text='write text',
           org=(150,150), 
           fontFace=cv.FONT_HERSHEY_SIMPLEX,
           fontScale=1.2,
           color=(255,255,255), 
           thickness=2)

cv.imshow('Text', blank)

cv.waitKey(0)
cv.destroyAllWindows()