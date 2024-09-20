import pyautogui
import win32api
import win32con
import time
import keyboard
# 608 0
# 2086 0
# 608 1435
# 2086 1435
# https://aimtrainer.io/challenge
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# 显示五s倒计时
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

def aimtarget():
    while keyboard.is_pressed('q') == False:
        try:
            # 使用不同大小的目标图像进行检测
            target_sizes = [0.8, 1.0, 1.2]  # 缩放因子
            for size in target_sizes:
                target_image = pyautogui.screenshot('aim.png')
                target_location = pyautogui.locateOnScreen(resized_target, region=(608, 0, 1478, 1435), confidence=0.9)
                if target_location:
                    break
            if target_location != None:
                print("检测到目标")    
                x, y, width, height = target_location
                print(f"目标位置: x={x}, y={y}, 宽度={width}, 高度={height}")
                # click(x + width//2, y + height//2)
                print(f"已点击目标中心位置: ({x + width//2}, {y + height//2})")
            else:
                print("未检测到目标")
        except pyautogui.ImageNotFoundException:
            print("未检测到目标")
        except Exception as e:
            print(f"发生错误: {e}")
        
        time.sleep(0.3)

# 864 665 
# 1779 696 
x_l = [1273,2071]
y_l = [451,931]
def aimpixel():
    while not keyboard.is_pressed('q'):
        screen = pyautogui.screenshot(region=(x_l[0], y_l[0], x_l[1]-x_l[0], y_l[1]-y_l[0]))
        width, height = screen.size
        click_s = False
        for i in range(0, width, 10):
            for j in range(0, height, 5):
                r, g, b = screen.getpixel((i, j))
                if r == 255 and g < 100 and b < 100:
                    abs_x, abs_y = x_l[0] + i, y_l[0] + j
                    print(abs_x, abs_y, (r, g, b))
                    print("找到目标")
                    time.sleep(0.3)
                    click_s = True
                    click(abs_x, abs_y)
                    
                    # 移除了time.sleep(0.1)，因为这可能导致连点问题
                    # 如果仍然出现连点，可能需要检查click函数或其他地方的延时设置
                    # time.sleep(0.05)
                    break
            # 如果已经找到目标，则退出循环 重新获取新截图
            if click_s == True:
                print("重新获取新截图")
                break
            
                

if __name__ == "__main__":
    # aimtarget()
    aimpixel()