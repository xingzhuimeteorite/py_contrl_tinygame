# 检测键盘摁下事件
import keyboard


def on_key_event(event):
    print(f"键盘事件: {event.name} 状态: {event.event_type}")

keyboard.hook(on_key_event)

while True:
    try:
        keyboard.wait()
    except KeyboardInterrupt:
        print("程序已停止")
        break