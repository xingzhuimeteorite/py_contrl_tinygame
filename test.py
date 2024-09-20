import win32api
import win32con
import time
import pyautogui
import cv2
import numpy as np
def push_down():
    # 按下下键 然后松开
    # 0x28 是下箭头键的虚拟键码
    win32api.keybd_event(0x28, 0, 0, 0)  # 按下下键
    time.sleep(0.05)
    win32api.keybd_event(0x28, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开下键
    # KEYEVENTF_KEYUP 是一个常量，表示键盘按键释放的事件。
# 像网页中输入下键 似乎有额外操作？


def draw(x1, y1, x2, y2):
    while True:
        # 创建屏幕截图
        pic = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
        # 创建绘图对象        
        # 在截图上绘制矩形
        # 将PIL图像转换为OpenCV格式
        cv_image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
        
        # 在图像上画线
        cv2.line(cv_image, (0, 0), (cv_image.shape[1], cv_image.shape[0]), (0, 255, 0), 2)
        
        # 显示图像
        cv2.imshow("pic", cv_image)
        if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


print("开始")
draw(1693,399,2356,879)
push_down()
print("结束")

