# opencv 霍夫变换检测直线和圆 https://www.cnblogs.com/wojianxin/p/12619034.html

import cv2 as cv
import numpy as np
from utils import absPath

img = cv.imread(absPath('shapes2.png'))
drawing = np.zeros(img.shape[:], dtype=np.uint8)  # 创建画板

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)

# 1. 标准霍夫变换
'''
OpenCV中用cv.HoughLines()在二值图上实现霍夫变换，函数返回的是一组直线的(r,θ)数据：
函数中：
参数1：要检测的二值图（一般是阈值分割或边缘检测后的图）
参数2：距离r的精度，值越大，考虑越多的线
参数3：角度θ的精度，值越小，考虑越多的线
参数4：累加数阈值，值越小，考虑越多的线
'''
# lines = cv.HoughLines(edges, 0.8, np.pi / 180, 90)

# 2. 统计概率霍夫直线变换
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
if len(lines) > 0:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv.line(drawing, (x1, y1), (x2, y2), (255, 0, 0),
                1,
                lineType=cv.LINE_AA)

# 3 霍夫圆变换
'''
参数2：变换方法，一般使用霍夫梯度法，详情：HoughModes
参数3：dp=1：表示霍夫梯度法中累加器图像的分辨率与原图一致
参数4：两个不同圆圆心的最短距离
参数5：param2跟霍夫直线变换中的累加数阈值一样
'''
circles = cv.HoughCircles(edges, cv.HOUGH_GRADIENT, 1, 20, param2=30)
circles = np.int0(np.around(circles))

# 将检测的圆画出来
if len(circles):
    for i in circles[0, :]:
        cv.circle(drawing, (i[0], i[1]), i[2], (0, 255, 0), 2)  # 画出外圆
        cv.circle(drawing, (i[0], i[1]), 2, (0, 0, 255), 3)  # 画出圆心

cv.imshow('probabilistic hough lines + circles', np.hstack((img, drawing)))
cv.waitKey(0)