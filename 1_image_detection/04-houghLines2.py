# opencv 霍夫变换检测直线和圆 https://www.cnblogs.com/wojianxin/p/12619034.html

import cv2 as cv
import numpy as np
from utils import absPath

# 1. 霍夫直线变换
img = cv.imread(absPath('shapes2.png'))
drawing = np.zeros(img.shape[:], dtype=np.uint8)  # 创建画板
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)

# a. 标准霍夫变换
'''
OpenCV中用cv.HoughLines()在二值图上实现霍夫变换，函数返回的是一组直线的(r,θ)数据：
函数中：
参数1：要检测的二值图（一般是阈值分割或边缘检测后的图）
参数2：距离r的精度，值越大，考虑越多的线
参数3：角度θ的精度，值越小，考虑越多的线
参数4：累加数阈值，值越小，考虑越多的线
'''
# lines = cv.HoughLines(edges, 0.8, np.pi / 180, 90)

# b. 统计概率霍夫直线变换
'''
minLineLength：最短长度阈值，比这个长度短的线会被排除
maxLineGap：同一直线两点之间的最大距离
'''
lines = cv.HoughLinesP(edges,
                       0.8,
                       np.pi / 180,
                       90,
                       minLineLength=50,
                       maxLineGap=10)

# 将检测的线画出来
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv.line(drawing, (x1, y1), (x2, y2), (255, 0, 0), 1, lineType=cv.LINE_AA)

cv.imshow('probabilistic hough lines', np.hstack((img, drawing)))
cv.waitKey(0)