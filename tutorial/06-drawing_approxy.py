import cv2 as cv
import numpy as np

drawing = False  # 是否开始画图
mode = True  # True：画矩形，False：画圆
start = (-1, -1)
pos = []


# 鼠标的回调函数的参数格式是固定的，不要随意更改。
def mouse_event(event, x, y, flags, param):
    global start, drawing, mode, pos

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
                pos.append([x, y])
    # 左键释放：结束画图
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv.rectangle(img, start, (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 2, (0, 0, 255), -1)
            # Numpy 二维数组
            pts = np.array([pos], np.int32)
            # pts = np.array([pos], np.int32).reshape((-1, 1, 2))
            approx2 = cv.approxPolyDP(pts, 15, True)
            cv.polylines(img, [approx2], True, (0, 255, 0), 2)
            pos.clear()


winName = "Drawing"
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow(winName)
cv.setMouseCallback(winName, mouse_event)

while (True):
    cv.imshow(winName, img)
    # 按下m切换模式
    if cv.waitKey(1) == ord('m'):
        mode = not mode
    # 按ESC键退出程序
    elif cv.waitKey(1) == 27:
        break