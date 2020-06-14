# USAGE
# python opencv_tutorial_01.py

# import the necessary packages
import imutils
import cv2 as cv
import sys

# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)

img = cv.imread('jp.png')
h, w, d = img.shape
print(" Height={}, Width = {}, Depth={}".format(h,w, d))
cv.imshow("Hello", img)
cv.waitKey(3)
b, g, r = img[100, 50]
print("R={}, G={}, B={}".format(r, g, b))

# r=h/w
# new_w=int(w)
# new_h=int(new_w*r)
# resized = cv.resize(img, (new_w,new_h))

# resized = imutils.resize(img, width=int(w*0.5))
# print (img.shape)
# print (resized.shape)
# cv.imshow("Resized", resized)
# cv.waitKey(0)

blurred=cv.blur(img, (5,5),0)
cv.imshow("Blurred", blurred)
cv.waitKey(0)

sys.exit()
##########
##########
##########
##########
##########
##########
# image = cv.imread("jp.png")
# (h, w, d) = image.shape
# print("width={}, height={}, depth={}".format(w, h, d))


# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution
cv.imshow("Image", image)
cv.waitKey(0)

# access the RGB pixel located at x=50, y=100, keepind in mind that
# OpenCV stores images in BGR order rather than RGB
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

# extract a 100x100 pixel square ROI (Region of Interest) from the
# input image starting at x=320,y=60 at ending at x=420,y=160
roi = image[60:160, 320:420]
cv.imshow("ROI", roi)
cv.waitKey(0)

# resize the image to 200x200px, ignoring aspect ratio
resized = cv.resize(image, (200, 200))
cv.imshow("Fixed Resizing", resized)
cv.waitKey(0)

# fixed resizing and distort aspect ratio so let's resize the width
# to be 300px but compute the new height based on the aspect ratio
r = 300.0 / w
dim = (300, int(h * r))
resized = cv.resize(image, dim)
cv.imshow("Aspect Ratio Resize", resized)
cv.waitKey(0)

# manually computing the aspect ratio can be a pain so let's use the
# imutils library instead
resized = imutils.resize(image, width=300)
cv.imshow("Imutils Resize", resized)
cv.waitKey(0)

# let's rotate an image 45 degrees clockwise using OpenCV by first
# computing the image center, then constructing the rotation matrix,
# and then finally applying the affine warp
center = (w // 2, h // 2)
M = cv.getRotationMatrix2D(center, -45, 1.0)
rotated = cv.warpAffine(image, M, (w, h))
cv.imshow("OpenCV Rotation", rotated)
cv.waitKey(0)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
cv.imshow("Imutils Rotation", rotated)
cv.waitKey(0)

# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
cv.imshow("Imutils Bound Rotation", rotated)
cv.waitKey(0)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv.GaussianBlur(image, (11, 11), 0)
cv.imshow("Blurred", blurred)
cv.waitKey(0)

# draw a 2px thick red rectangle surrounding the face
output = image.copy()
cv.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
cv.imshow("Rectangle", output)
cv.waitKey(0)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv.circle(output, (300, 150), 20, (255, 0, 0), -1)
cv.imshow("Circle", output)
cv.waitKey(0)

# draw a 5px thick red line from x=60,y=20 to x=400,y=200
output = image.copy()
cv.line(output, (60, 20), (400, 200), (0, 0, 255), 5)
cv.imshow("Line", output)
cv.waitKey(0)

# draw green text on the image
output = image.copy()
cv.putText(output, "OpenCV + Jurassic Park!!!", (10, 25),
           cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv.imshow("Text", output)
cv.waitKey(0)
