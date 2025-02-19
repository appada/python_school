import pyautogui
import time

click_num = int( input('마우스 클릭 수: '))
delay_sec = float( input('딜레이 (초): '))

# for count_down in range(5, 0, -1):
#     print(f' 시작 카운트 다운 : {count_down}')

print('mouse click start')
for click in range(click_num):
    pyautogui.click()
    print(f'{click + 1} 번 클릭')
    time.sleep(delay_sec)


#######################################################################
import flet as ft
import time
import pyautogui
import keyboard
import threading

def main(page: ft.Page):
    
    print(pyautogui.size())

    count = 0  # 초기 카운트 값

    def increment_text(e):
        nonlocal count
        count += 1
        numbutton.text = f"Count: {count}"
        page.update()

    numbutton = ft.ElevatedButton(text="Count: test", width=200,height=200,
                               on_click=increment_text)
    #
    def start_auto_click(e):
        x = int(X.value)
        y = int(Y.value)
        interval = float(interval_field.value)
        clicks = int(clicks_field.value)
        page.update()

        for index in range(clicks):
            if keyboard.is_pressed('q'):
                print('Auto click stopped by user.')
                break
            pyautogui.click(x, y)
            time.sleep(interval)


    X = ft.TextField(label="X", width=100)
    Y = ft.TextField(label="Y", width=100)
    interval_field = ft.TextField(label="Interval (seconds)", width=150)
    clicks_field = ft.TextField(label="Number of Clicks", width=150)
    start_button = ft.ElevatedButton(text="Start Auto Click", on_click=start_auto_click)
    stop_text = ft.Text('Stop Button is Q')
    #
    r_menu = ft.Column( [ 
        X, 
        Y, 
        interval_field,
        clicks_field,
        start_button,
        stop_text
    ] )
    #
    left_right = ft.Row([ numbutton, r_menu])
    page.add(left_right)

    #
    
    mouse_position = pyautogui.position()
    anouncement = ft.Text(value=f'마우스 위치는 화살표위를 누르세요: {mouse_position} ' )
    mouse_position_text = ft.Text(value="Mouse Position: (0, 0)", size=20)
    page.add(mouse_position_text)
    page.update()


ft.app(target=main)


# def on_key(event: ft.KeyboardEvent):
#     if event.key == "Arrow Up":
#         anouncement.value = pyautogui.position()
#     page.update()
# 
# 
# page.on_keyboard_event = on_key

# # 마우스 위치 업데이트 함수
# def update_mouse_position():
#     while True:
#         if stop_flag.is_set():
#             break
#         x, y = pyautogui.position()
#         mouse_position_text.value = f"Mouse Position: ({x}, {y})"
#         page.update()
#         time.sleep(0.1)
# 
# 
# threading.Thread(target=update_mouse_position).start()




########################################################################

import flet as ft
import time
import pyautogui
import keyboard

def main(page: ft.Page):

    def on_key(event: ft.KeyboardEvent):
        if event.key == "Arrow Up":
            anouncement.value = pyautogui.position()
        page.update()

    page.on_keyboard_event = on_key

    count = 0  # 초기 카운트 값

    def increment_text(e):
        nonlocal count
        count += 1
        numbutton.text = f"Count: {count}"
        page.update()

    numbutton = ft.ElevatedButton(text="Count: test", width=200,height=200,
                               on_click=increment_text)

    def start_auto_click(e):
        x = int(X.value)
        y = int(Y.value)
        interval = float(interval_field.value)
        clicks = int(clicks_field.value)
        page.update()

        for index in range(clicks):
            if keyboard.is_pressed('q'):
                print('Auto click stopped by user.')
                break
            pyautogui.click(x, y)
            time.sleep(interval)

    X = ft.TextField(label="X", width=100)
    Y = ft.TextField(label="Y", width=100)
    interval_field = ft.TextField(label="Interval (seconds)", width=150)
    clicks_field = ft.TextField(label="Number of Clicks", width=150)
    start_button = ft.ElevatedButton(text="Start Auto Click", on_click=start_auto_click)
    stop_text = ft.Text('Stop Button is Q')

    r_menu = ft.Column([X, Y, interval_field,clicks_field,start_button,stop_text])

    left_right = ft.Row([ numbutton, r_menu])
    page.add(left_right)

    #
    monitor = pyautogui.size()
    mouse_position = pyautogui.position()
    anouncement = ft.Text(value=f'마우스 위치는 화살표위를 누르세요: {mouse_position} ' )
    page.add(anouncement)
    page.update()


if __name__ == "__main__":

    ft.app(target=main)

#---------------------------------
click_num = int( input('마우스 클릭 수: '))
delay_sec = float( input('딜레이 (초): '))

for count_down in range(7, 0, -1):
    print(f' 시작 카운트 다운 : {count_down}')

print('mouse click start')
for click in range(click_num):
    pyautogui.click()
    print(f'{click + 1} 번 클릭')
    time.sleep(delay_sec)





    # from flet import Page, UserControl, ElevatedButton, Column
    #
    #
    # class CounterControl(UserControl):
    #     def __init__(self):
    #         super().__init__()
    #         self.count = 0
    #
    #     def build(self):
    #         self.button = ElevatedButton(text=f"Count: {self.count}", on_click=self.increment_text)
    #         return Column([self.button])
    #
    #     def increment_text(self, e):
    #         self.count += 1
    #         self.button.text = f"Count: {self.count}"
    #         self.button.update()
    #
    #
    # def main(page: Page):
    #     counter_control = CounterControl()
    #     page.add(counter_control)
    #
    #
    # if __name__ == "__main__":
    #     import flet
    #
    #     flet.app(target=main)
