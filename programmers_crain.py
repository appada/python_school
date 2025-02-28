import random

import flet as ft

def main(page:ft.Page):

    buttons = [
        ["😊", "🐳", "⏰", "❤️", "✨","❤️", "✨"],
        ["❤️", "😊", "🐳", "⏰", "✨","❤️", "✨"],
        ["🐳", "⏰", "❤️", "😊", "✨","😊", "✨"],
        ["⏰", "😊", "🐳", "❤️", "✨","❤️", "✨"],
        ["⏰", "✨", "🐳", "❤️", "😊","❤️", "😊"],
        ["⏰", "✨", "🐳", "❤️", "😊","❤️", "😊"],
    ]

    for i in buttons:
         random.shuffle(i)

    stack_check = []
    score = 0

    def pop_button(e):
        nonlocal stack_check
        pop_y = e.control.data

        x=0
        while True:
            if x >= len(buttons):
                break
            if buttons[x][pop_y] != ' ' :
                check_button(buttons[x][pop_y])
                buttons[x][pop_y] = ' '
                break
            x += 1
        make_buttons()

    def check_button( button_icon ):
        nonlocal stack_check,score
        stack_check.append(button_icon)

        if len(stack_check) > 1:
            previous_icon = stack_check[-2]
            current_icon = stack_check[-1]

            if current_icon == previous_icon:
                stack_check.pop()
                stack_check.pop()
                score += 1
                print("ok")
            else:
                print("nope")

    def make_buttons():
        nonlocal stack_check
        page.clean()
        rows = []
        for row in range(len(buttons)):
            cols = []
            for col in range(len(buttons[row])):
                a = ft.ElevatedButton(text=buttons[row][col], data=[row, col])
                cols.append(a)
            rows.append(ft.Row(cols, spacing=5))

        pops = []
        for i, row in enumerate(range(len(buttons[0]))):
            abutton = ft.ElevatedButton(text=str(i), on_click=pop_button, data=i)
            pops.append(abutton)

        stack_check_cols = []
        for col in stack_check:
            abutton = ft.OutlinedButton(col)
            stack_check_cols.append(abutton)

        page.add(ft.Column(rows, spacing=5), ft.Row(pops) , ft.Row(stack_check_cols))

    make_buttons()

ft.app(main)
