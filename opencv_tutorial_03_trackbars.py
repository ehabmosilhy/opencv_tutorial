import cv2 as cv
import sys

def trackChaned(x):
	pass

myimage='coke_shelf.jpg'
img_color = cv.imread(myimage)
img = cv.imread(myimage,0)


cv.namedWindow('Color Track Bar')
hh = 'Threshold'
hl = 'Max Value'
wnd = 'Colorbars'
cv.createTrackbar("Threshold", "Color Track Bar", 0, 255, trackChaned)
cv.createTrackbar("Max Val", "Color Track Bar", 255, 255, trackChaned)
cv.imshow("original", img)

while (True):
	thresh = cv.getTrackbarPos("Threshold", "Color Track Bar")
	maxval = cv.getTrackbarPos("Max Val", "Color Track Bar")
	ret, thresh1 = cv.threshold(img, thresh, maxval, cv.THRESH_BINARY_INV)

	cv.imshow("thresh1", thresh1)

	cnts = cv.findContours(thresh1.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)[0]
	output = img_color.copy()

	for c in cnts:
		cv.drawContours(output, [c], -1, (240, 0, 159), 2)

	cv.imshow("Countours", output)

	edged = cv.Canny(img, thresh, 150)
	cv.imshow("Edges", edged)

	if cv.waitKey(1) == 27:
		break

cv.destroyAllWindows()




sys.exit()
def nothing(self):
	print (self)


img = cv.imread('tetris_blocks.png')
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
