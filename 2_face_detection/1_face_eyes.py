''' 人脸识别 '''
import numpy as np
import cv2
# import time
# import datetime
from PIL import Image
from utils import absPath

cap = cv2.VideoCapture(0)


def getface(img):
    # 人脸识别数据
    face_cascade = cv2.CascadeClassifier(
        absPath('res/models/haarcascade_frontalface_default.xml'))

    # 二值化,变为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取人脸识别数据
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        # 绘画人脸识别数据
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # 根据人脸识别数据添加贴纸
        img = addTags(img, x, y, w, h)

    # 人眼识别数据
    eye_cascade = cv2.CascadeClassifier(
        absPath('res/models/haarcascade_eye.xml'))
    # 获取人眼识别数据
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in eyes:
        # 绘画人眼识别数据
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return img


def addTags(img, x, y, w, h):
    im = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    mark = Image.open(absPath("res/004.png"))  # 贴纸地址
    # height = int(w * 987 / 1024)
    # mark = mark.resize((w, height))
    mark = mark.resize((w, h))
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    # layer.paste(mark, (x, y - height))
    layer.paste(mark, (x, y))
    out = Image.composite(layer, im, layer)
    img = cv2.cvtColor(np.asarray(out), cv2.COLOR_RGB2BGR)
    return img


# videoWriter = cv2.VideoWriter('testwrite.avi', cv2.VideoWriter_fourcc(*'MJPG'),
#                               15, (1000, 563))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        # 从新定义图片大小
        img = cv2.resize(frame, (1000, 563))

        # 添加录像时间
        # img = addtime(img)
        # 实时识别
        img = getface(img)
        # 视频显示
        cv2.imshow('frame', img)
        # 保存视频
        # videoWriter.write(img)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("退出视频")
            break
    else:
        break

cap.release()
# videoWriter.release()
cv2.destroyAllWindows()