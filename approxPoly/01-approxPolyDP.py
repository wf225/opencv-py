# opencv 多边形近似物体形状 cv.approxPolyDP函数的应用
# https://www.cnblogs.com/wojianxin/p/12610631.html

import cv2 as cv
import numpy as np
import os

currentDir = os.path.dirname(__file__)


def getAbsPath(res):
    return os.path.join(currentDir, res)

# 多边形逼近
# 1.先找到轮廓
img = cv.imread(getAbsPath('test01.png'), 0)
_, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
contours, hierarchy = cv.findContours(thresh, 3, 2)
cnt = contours[0]

# 2.进行多边形逼近，得到多边形的角点
approx1 = cv.approxPolyDP(cnt, 3, True)
approx2 = cv.approxPolyDP(cnt, 15, True)
approx3 = cv.approxPolyDP(cnt, 75, True)

# 3.画出多边形
image = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
cv.polylines(image, [approx1], True, (255, 0, 0), 2)
cv.polylines(image, [approx2], True, (0, 255, 0), 2)
cv.polylines(image, [approx3], True, (0, 0, 255), 2)

print(len(approx1), len(approx2), len(approx3))  # 角点的个数
cv.imshow('approxPloyDP', image)
cv.waitKey(0)
cv.destroyAllWindows()