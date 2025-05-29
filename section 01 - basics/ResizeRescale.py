import cv2 as cv

# Resize
# Load the image
img = cv.imread('images/doomguy.png')
# Define different scale parameters for width and heigh
fx = 0.88
fy = 0.66

# Different methods to resize
resize_area = cv.resize(img, None, fx=fx, fy=fy, interpolation=cv.INTER_AREA)
resize_linear = cv.resize(img, None, fx=fx, fy=fy, interpolation=cv.INTER_LINEAR)
resize_cubic = cv.resize(img, None, fx=fx, fy=fy, interpolation=cv.INTER_CUBIC)

cv.imshow('resize_area', resize_area)
cv.imshow('resize_linear',resize_linear)
cv.imshow('resize_cubic',resize_cubic)
cv.waitKey(0)
cv.destroyAllWindows()

# Rescale
def rescaleFrame(frame, scale=0.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# rescale image
# img = cv.imread('images/doomguy.png')
# rescale_img = rescaleFrame(img)

# cv.imshow('Original Image', img)
# cv.imshow('Rescale Image', rescale_img)

# cv.waitKey(0)

# resize videos
# vid = cv.VideoCapture('videos/DOOM.mp4')

# while True:
#     isTrue, frame = vid.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Doom', frame)
#     cv.imshow('Doom_resized', frame_resized)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# vid.release()
# cv.destroyAllWindows()
