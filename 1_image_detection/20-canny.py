# opencv 检测图像边缘 Canny算法应用 https://www.cnblogs.com/wojianxin/p/12597673.html

import cv2 as cv
import numpy as np
from utils import absPath

img = cv.imread(absPath('paojie_g.png'), 0)
cv.namedWindow('window')

# # 1. 二值化图像处理后，边缘检测效果更好
# _, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
# # canny边缘检测，60以下置为0,180以上置为255,第2、3参数的作用可查看本文最后一部分内容
# edges = cv.Canny(thresh, 60, 180)

# cv.imshow('canny', np.hstack((img, edges)))
# cv.waitKey(0)
# cv.destroyAllWindows()


# 2.
def track_back(x):
    pass


# 创建滑动条
cv.createTrackbar('maxVal', 'window', 30, 100, track_back)
cv.createTrackbar('minVal', 'window', 180, 255, track_back)

while (True):
    # 获取滑动条的值
    max_val = cv.getTrackbarPos('maxVal', 'window')
    min_val = cv.getTrackbarPos('minVal', 'window')

    edges = cv.Canny(img, min_val, max_val)
    cv.imshow('window', edges)

    # 按下ESC键退出
    if cv.waitKey(30) == 27:
        break