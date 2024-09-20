import pyautogui
import win32api
import win32con
import time
import keyboard

# 引入pil画一些东西 
import cv2
import numpy as np



# -2849 113
# -2143 628
# https://aimtrainer.io/challenge
# 游戏区域
l_1= [10,113]
l_2= [547,992]
# 画出游戏区域
# 在这里我们需要先创建一个图像对象，然后再创建绘图对象

# 钩子原点 
l_3 = [286,264]
l_3 = [l_3[0]-l_1[0],l_3[1]-l_1[1]]
# 线条长度
l_4 = 5
# 10 113 
# 547 992
# 286264

gold =  (250, 240, 50)
target = (225,225,225)

def push_down():
    # 按下下键 然后松开
    # 0x28 是下箭头键的虚拟键码
    win32api.keybd_event(0x28, 0, 0, 0)  # 按下下键
    time.sleep(0.05)
    win32api.keybd_event(0x28, 0, win32con.KEYEVENTF_KEYUP, 0)  # 松开下键
    # KEYEVENTF_KEYUP 是一个常量，表示键盘按键释放的事件。
    # 在这里，它用于指示系统释放之前按下的下箭头键。
    # 这个常量确保键盘事件被正确识别为按键释放，而不是按键按下。



def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def minnerbot():
    while keyboard.is_pressed('q') == False:
        # 划定寻找区域 截图
        pic = pyautogui.screenshot( region=(l_1[0], l_1[1], l_2[0]-l_1[0], l_2[1]-l_1[1]))
        # 找到黄金
        find_Gold = False
        cv_image = cv2.cvtColor(np.array(pic), cv2.COLOR_RGB2BGR)
        cv2.imshow("picccc", cv_image)
        cv2.waitKey(1)
        for i in range(0,l_2[0]-l_1[0],20):
            for j in range(0+200,l_2[1]-l_1[1],20):
                print("当前坐标",i,j,pic.getpixel((i,j)))
                # 判断是否是黄金
                r,j,b = pic.getpixel((i,j))
                if r >= gold[0] and j >= gold[1] and b <= gold[2]:
                # if (r,j,b) == gold:
                    # 记录坐标 找到黄金点
                    print("黄金点",i,j)
                    # 画一条黄金点到钩子原点的线
                    cv2.line(cv_image, (i, j), (l_3[0], l_3[1] ), (0, 255, 0), 2)

                    # 计算黄金点到钩子原点的斜率
                    k = (j-l_3[1])/(i-l_3[0])
                    print("斜率",k)
                    # 计算线条落在斜率上的像素点
                    x = int(l_3[0] + l_4 / k)
                    y = int(l_3[1] + l_4 * k)
                    print("线条上的点",x,y) 
                    # 画一条钩子原点到线条上的点的线
                    cv2.line(cv_image, (l_3[0], l_3[1] ), (x, y), (0, 0, 255), 2)
                    find_Gold = True
                    # 当这个点是黑色的时候 点击
                    cv2.imshow("picccc", cv_image)
                    cv2.waitKey(1)
                    while True:
                        # 画图
                        print("画图")
                        cv2.imshow("picccc", cv_image)
                        cv2.waitKey(1)
                        print("检测",(x,y),pyautogui.pixel(x,y))
                        r,g,b = pyautogui.pixel(x,y)
                        if r>=target[0] and g>=target[1] and b>=target[2]:
                            print("检测到方向一致 执行钩子")
                            # push_down()
                            click(x+l_1[0],y+l_1[1])
                            break
                if find_Gold  == True:
                    break
            if find_Gold  == True:
                    break
            

if __name__ == "__main__":
    # 倒计时启动
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
    minnerbot()