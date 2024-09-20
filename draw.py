import pygame
import sys
import win32gui
import win32con
import win32api  # 添加这行

# 初始化 Pygame
pygame.init()

# 获取屏幕信息
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h

# 创建透明窗口
screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
# 修改这行
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 0, win32con.LWA_COLORKEY)

# 创建透明surface
transparent = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)

# 预设几条线
pygame.draw.line(transparent, (255, 0, 0), (100, 100), (300, 300), 2)
pygame.draw.line(transparent, (0, 255, 0), (100, 300), (300, 100), 2)
pygame.draw.line(transparent, (0, 0, 255), (200, 100), (200, 300), 2)

# 主循环
drawing = False
last_pos = None
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION and drawing:
            if last_pos:
                pygame.draw.line(transparent, (255, 0, 0), last_pos, event.pos, 2)
            last_pos = event.pos

    # 清空屏幕
    screen.fill((0,0,0))
    # 将透明surface绘制到屏幕上
    screen.blit(transparent, (0, 0))
    pygame.display.flip()
    clock.tick(60)  # 限制帧率为60FPS