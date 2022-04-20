import cv2 as cv
import numpy as np

# 创建一副黑色的图片
img = np.zeros((512, 512, 3), np.uint8)

# 画一条线宽为5的蓝色直线
# 参数1：源图像，参数2：起点，参数3：终点，参数4：颜色(蓝色)，参数5：线宽(5)
cv.line(img, (0, 0), (512, 512), (255, 0, 0), 5)

# 画一个绿色边框的矩形
# 参数1：源图像，参数2：左上角坐标，参数3：右下角坐标，参数4：颜色(绿)，参数5：线宽(3)
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# 画一个填充红色的圆
# 参数1：源图像，参数2：圆心坐标，参数3：半径，参数4：颜色(红)，参数5：-1表示填充
cv.circle(img, (447, 63), 63, (0, 0, 255), -1)

# 在图中心画一个填充的半椭圆
# 参数1：源图像
# 参数2：椭圆中心(x,y)
# 参数3：x/y轴的长度
# 参数4：angle—椭圆的旋转角度
# 参数5：startAngle—椭圆的起始角度
# 参数6：endAngle—椭圆的结束角度
# 参数7：颜色(蓝色)
# 参数8：-1表示填充椭圆
cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, (255, 0, 0), -1)

# 画多边形
# 定义四个顶点坐标
pts = np.array([[10, 5], [50, 10], [70, 20], [20, 30]], np.int32)
# 顶点个数：4，矩阵变成4*1*2维
pts = pts.reshape((-1, 1, 2))
# True表示闭合多边形
cv.polylines(img, [pts], True, (0, 255, 255))

# 使用cv.polylines()画多条直线
line1 = np.array([[100, 20], [300, 20]], np.int32).reshape((-1, 1, 2))
line2 = np.array([[100, 60], [300, 60]], np.int32).reshape((-1, 1, 2))
line3 = np.array([[100, 100], [300, 100]], np.int32).reshape((-1, 1, 2))
cv.polylines(img, [line1, line2, line3], True, (0, 255, 255))

# 字体设置
font = cv.FONT_HERSHEY_SIMPLEX
# 参数1：源图像，参数2：文字内容，参数3：文字写入位置(左上角坐标)，参数4：字体，参数5：文字大小，
# 参数6：颜色(白色)，参数7：线宽(2)，参数8：线型(LINE_AA表示抗锯齿线型)
cv.putText(img,
           'OpenCV', (10, 500),
           font,
           1, (255, 255, 255),
           2,
           lineType=cv.LINE_AA)

cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()