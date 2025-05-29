import cv2 as cv
import numpy as np

img = cv.imread('doomguy.png')
if img is not None:
    cv.namedWindow('image', cv.WINDOW_AUTOSIZE)
    cv.imshow('image', img)
    cv.waitKey(0)

    # преобразование в оттенки серого
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Gray', gray)
    cv.waitKey(0)
    cv.destroyAllWindows()  

    # нахождение границ
    edges = cv.Canny(gray, 50, 150)
    cv.imshow('Edges', edges)
    cv.waitKey(0)


    # blured
    blurred = cv.GaussianBlur(img, (5,5), 0)
    cv.imshow('Blurred', blurred)
    cv.waitKey(0)

    # finish out script
    cv.destroyAllWindows()
    print('Changes finished')


else:
    print("Ошибка: Не удалось загрузить изображение.")
