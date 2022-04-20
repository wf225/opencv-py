# list all available events:
# [
# 'EVENT_FLAG_ALTKEY',
# 'EVENT_FLAG_CTRLKEY',
# 'EVENT_FLAG_LBUTTON',
# 'EVENT_FLAG_MBUTTON',
# 'EVENT_FLAG_RBUTTON',
# 'EVENT_FLAG_SHIFTKEY',
# 'EVENT_LBUTTONDBLCLK',
# 'EVENT_LBUTTONDOWN',
# 'EVENT_LBUTTONUP',
# 'EVENT_MBUTTONDBLCLK',
# 'EVENT_MBUTTONDOWN',
# 'EVENT_MBUTTONUP',
# 'EVENT_MOUSEHWHEEL',
# 'EVENT_MOUSEMOVE',
# 'EVENT_MOUSEWHEEL',
# 'EVENT_RBUTTONDBLCLK',
# 'EVENT_RBUTTONDOWN',
# 'EVENT_RBUTTONUP']
# import cv2 as cv
# events = [i for i in dir(cv) if 'EVENT' in i]
# print( events )

import numpy as np
import cv2 as cv

print("EVENT_MBUTTONDBLCLK: {}".format(cv.EVENT_MBUTTONDBLCLK))
print("EVENT_LBUTTONDOWN: {}".format(cv.EVENT_LBUTTONDOWN))
print("EVENT_LBUTTONUP: {}".format(cv.EVENT_LBUTTONUP))
print("EVENT_MOUSEHWHEEL: {}".format(cv.EVENT_MOUSEHWHEEL))
print("EVENT_MOUSEMOVE: {}".format(cv.EVENT_MOUSEMOVE))
print("EVENT_MOUSEWHEEL: {}".format(cv.EVENT_MOUSEWHEEL))
print("EVENT_LBUTTONUP: {}".format(cv.EVENT_LBUTTONUP))


# mouse callback function
def draw_circle(event, x, y, flags, param):
    print(event)
    if event == cv.EVENT_LBUTTONUP:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while (1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()