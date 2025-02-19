import flet as ft
import time
import pyautogui

def main(page: ft.Page):
    print(pyautogui.size())
    print(pyautogui.position())
    count = 0  # 초기 카운트 값

    def increment_text(e):
        nonlocal count
        count += 1  # count = count + 1
        numbutton.text = f"Count: {count}"
        page.update()

    numbutton = ft.ElevatedButton(text="Count: 0", width=200,height=200,
                               on_click=increment_text)

    def start_auto_click(e):
        x = int(X.value)
        y = int(Y.value)
        interval = float(inter_val.value)
        clicks = int(clicks_num.value)
        page.update()

        for _ in range(clicks):
            pyautogui.click(x, y)
            time.sleep(interval)


    X = ft.TextField(label="X", width=100)
    Y = ft.TextField(label="Y", width=100)
    inter_val = ft.TextField(label="Interval (seconds)", width=150)
    clicks_num = ft.TextField(label="Number of Clicks", width=150)
    start_button = ft.ElevatedButton(text="Start Auto Click", on_click=start_auto_click)

    r_menu = ft.Column([X, Y, inter_val, clicks_num, start_button])

    leftright = ft.Row([ numbutton, r_menu])

    page.add(leftright)

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

    # print(pyautogui.size())#해상도
    # print(pyautogui.position())#928,250
    # pyautogui.mouseInfo()#35,24
    # pyautogui.moveTo(928,250,duration=2.5)
    # pyautogui.moveTo(1880,18,duration=2)
    # pyautogui.click()
    # pyautogui.moveTo(974,563,duration=2)
    # pyautogui.click()
    # pyautogui.click(clicks=2,button='right')
    # pyautogui.moveTo(35, 24, duration=1.5)
    # pyautogui.dragRel(200, 200, 1.5, button='left')
    #
