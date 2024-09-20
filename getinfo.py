
import pyautogui

# 获取屏幕分辨率
screen_width, screen_height = pyautogui.size()

while True:
    # 获取鼠标位置
    mouse_x, mouse_y = pyautogui.position()

    # 获取屏幕颜色
    color = pyautogui.pixel(mouse_x, mouse_y)

    # 打印日志
    print(f"屏幕分辨率: {screen_width}x{screen_height}")
    print(f"鼠标位置: ({mouse_x}, {mouse_y})")
    print(f"屏幕颜色: {color}")

    # 添加短暂延迟，避免过于频繁的循环
    pyautogui.sleep(0.3)
    # yanshi 0.5
