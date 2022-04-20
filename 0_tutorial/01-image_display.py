import cv2 as cv
import sys
from utils import absPath

img = cv.imread(cv.samples.findFile(absPath("clouds.jpg")),
                cv.IMREAD_GRAYSCALE)
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite(absPath("clouds.png"), img)