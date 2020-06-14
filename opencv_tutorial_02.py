# USAGE
# python opencv_tutorial_02.py --image tetris_blocks.png

# import the necessary packages
import imutils
import cv2 as cv
import sys



img = cv.imread('tetris.jpg')
cv.imshow("Image", img)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# edged=cv.Canny(img, 30,150)
# cv.imshow("Edges", edged)
# # cv.waitKey(0)

T, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
# cv.imshow("Thresh", thresh)

cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
# cnts = imutils.grab_contours(cnts)
output = img.copy()

i=0
for c in cnts:
	cv.drawContours(output, [c],-1, (240,0,159),3)

cv.imshow("Countours", output)
cv.waitKey(0)


sys.exit()
