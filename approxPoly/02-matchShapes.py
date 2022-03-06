# opencv 物体外形相似度匹配 cv.matchShapes函数使用
# https://www.cnblogs.com/wojianxin/p/12605552.html

# opencv中 cv.matchShapes() 可以检测两个形状之间的相似度，返回值越小，越相似

import numpy as np
import cv2 as cv

img = cv.imread('/Users/wubil/MyGit/opencv-py/approxPolyDP/shapes.jpg', 0)
_, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

contours, hierarchy = cv.findContours(thresh, 3, 2)
img_color = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)  # 用于绘制的彩色图

cnt_a, cnt_b, cnt_c = contours[0], contours[1], contours[2]
cv.drawContours(img_color, [cnt_a], 0, [255, 0, 0], 2)
cv.drawContours(img_color, [cnt_b], 0, [0, 255, 0], 2)
cv.drawContours(img_color, [cnt_c], 0, [0, 0, 255], 2)

# 参数3：匹配方法；参数4：opencv预留参数
print('b,b = ', cv.matchShapes(cnt_b, cnt_b, 1, 0.0))  # 0.0
print('b,c = ', cv.matchShapes(cnt_b, cnt_c, 1, 0.0))  # 2.17e-05
print('b,a = ', cv.matchShapes(cnt_b, cnt_a, 1, 0.0))  # 0.418

cv.imshow('result', img_color)
cv.waitKey(0)
cv.destroyAllWindows()