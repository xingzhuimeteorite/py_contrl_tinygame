import numpy as np
import cv2
from PIL import ImageGrab
import time
# youytube
y_l = [204,222]
x = 1200
y = 900
def process_image(img_np):
   
    # 将截图转换为灰度图像
    img_gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    # 边缘检测
    edges = cv2.Canny(img_gray, 50, 150)
    return edges
    
def main():
     
    last_time = time.time()
    while True:
        # 获取屏幕截图
        img = ImageGrab.grab(bbox=(y_l[0],y_l[1],x,y))
        # 将截图转换为numpy数组
        img_np = np.array(img)
        img_l = process_image(img_np)
        cv2.imshow('pic',img_l)
        print("loop time: ",time.time()-last_time)
        last_time = time.time()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == "__main__":
    main()