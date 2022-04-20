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
lines = cv.HoughLines(edges, 0.8, np.pi / 180, 90)

# 将检测的线画出来（注意是极坐标噢）
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    cv.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))

cv.imshow('hough lines', np.hstack((img, drawing)))
cv.waitKey(0)