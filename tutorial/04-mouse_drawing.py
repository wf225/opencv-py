import cv2 as cv
import numpy as np

drawing = False  # 是否开始画图
mode = True  # True：画矩形，False：画圆
start = (-1, -1)


# 鼠标的回调函数的参数格式是固定的，不要随意更改。
def mouse_event(event, x, y, flags, param):
    global start, drawing, mode

    # 左键按下：开始画图
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        start = (x, y)
    # 鼠标移动，画图
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv.rectangle(img, start, (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 2, (0, 0, 255), -1)
    # 左键释放：结束画图
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, start, (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 2, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', mouse_event)

while (True):
    cv.imshow('image', img)
    # 按下m切换模式
    if cv.waitKey(1) == ord('m'):
        mode = not mode
    # 按ESC键退出程序
    elif cv.waitKey(1) == 27:
        break