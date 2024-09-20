import pyautogui
import win32api
import win32con
import time
import keyboard
# pyautogui.displayMousePosition()
# https://www.agame.com/game/magic-piano-tiles

# 2150 2245 2324 2413 / 700 
# 创建一个单机函数
# 储存x列表
x_list = [1705, 1772, 1886, 1970]
y = 559
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# 检测到q键按下，则退出
while keyboard.is_pressed('q') == False:
    # 如果像素为黑色则单击 总共四个像素 
    for x in x_list:
        if pyautogui.pixel(x, y)[0] ==0:
            click(x, y)
            # 打印时间和单击日志
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), f"单击{x} {y}")
    # 打印时间  未检测到黑色像素
        else:
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), f"{x} {y} 未检测到黑色像素")
