import cv2 as cv

# read images
# img = cv.imread('images/doomguy.png')
# cv.imshow('Doom', img)
# cv.waitKey(0)

# read videos
vid = cv.VideoCapture('videos/DOOM.mp4')

while True:
    isTrue, frame = vid.read()
    cv.imshow('Doom', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

vid.release()
cv.destroyAllWindows()