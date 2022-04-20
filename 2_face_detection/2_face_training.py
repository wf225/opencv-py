'''
程序：训练人脸识别器，生成人脸特征数据
cv2模块中EigenFace（特征脸），EigenFace可用来实现人脸识别
Ref: https://blog.csdn.net/loveliuzz/article/details/73810334
'''

import cv2, numpy, os
from utils import absPath

#创建人脸检测器和识别器
labels, faces = [], []
face_cascade = cv2.CascadeClassifier(
    absPath('lbpcascade_frontalface_improved.xml'))
recognizer = cv2.face.LBPHFaceRecognizer_create()


def detect_face(image):
    '''检测人脸区域'''
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5, minSize=(20, 20))
    if (len(faces) == 0):
        return None
    (x, y, w, h) = faces[0]
    return gray[y:y + w, x:x + h]


def read_face(label, images_path):
    '''读取人脸图像'''
    print('trainning:', label, images_path)
    files = os.listdir(images_path)
    for file in files:
        if file.startswith('.'):
            continue
        #从文件中读取图像
        image = cv2.imread(images_path + '/' + file)
        #检测图像中的人脸区域
        face = detect_face(image)
        if face is not None:
            face = cv2.resize(face, (256, 256))
            faces.append(face)
            labels.append(label)


if __name__ == '__main__':
    #读取人脸图像
    read_face(1, absPath('training/spider_man/'))
    read_face(2, absPath('training/iron_man/'))
    #训练人脸识别器
    recognizer.train(faces, numpy.array(labels))
    #保存人脸特征数据
    recognizer.save(absPath('trainner.yml'))
