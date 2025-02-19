import flet as ft
import time
import pyautogui
import keyboard

def main(page: ft.Page):

    def on_key(event: ft.KeyboardEvent):
        if event.key == "q":
            print('Q pressed')
        elif event.key == "Arrow Up":
            print('Up pressed')
            page.window.close()
        page.update()

    page.on_keyboard_event = on_key

    count = 0  # 초기 카운트 값

    def increment_text(e):
        nonlocal count
        count += 1
        numbutton.text = f"Count: {count}"
        page.update()

    numbutton = ft.ElevatedButton(text="Count: 0", width=200,height=200,
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

    leftright = ft.Row([ numbutton, r_menu])
    page.add(leftright)

    #

    page.update()

if __name__ == "__main__":

    ft.app(target=main)

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
