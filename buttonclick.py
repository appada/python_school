import random

import flet as ft

def main(page:ft.Page):

    buttons = [
        ["😊", "🐳", "⏰", "❤️", "✨"],
        ["❤️", "😊", "🐳", "⏰", "✨"],
        ["🐳", "⏰", "❤️", "😊", "✨"],
        ["⏰", "😊", "🐳", "❤️", "✨"],
        ["⏰", "✨", "🐳", "❤️", "😊"],
        ["⏰", "✨", "🐳", "❤️", "😊"],
    ]

    def input_click(e):
        icon_list = list(input_icon.value)
        buttons.clear()

        for row in range(len(icon_list)):
            icon_row = []
            for icon in icon_list:
                icon_row.append(icon)
            random.shuffle(icon_row)
            buttons.append(icon_row)
        make_buttons()


    input_icon = ft.TextField(label='icon here')
    input_button = ft.ElevatedButton('Make', on_click=input_click)
    icon_menu = ft.Row([ input_icon, input_button])


    for i in buttons:
        random.shuffle(i)

    twin_check=[]
    two_color = 'red'
    count = 0
    score = 0

    total = ft.Text(value=score, size=30)

    def button_click(e):
        button = e.control
        nonlocal count, two_color, score
        button.bgcolor = two_color

        count += 1
        if count >= 2 :
            two_color = ft.Colors.random()
            count = 0

        twin_check.append(button.text)
        if len(twin_check) >= 2 :
            if twin_check[0] == twin_check[1]:
                score += 1
                total.value=score
                twin_check.clear()
            twin_check.clear()
        page.update()

    def make_buttons():
        page.clean()
        b_Column = []
        for row in buttons:
            b_Row = []
            for abutton in row:
                a = ft.ElevatedButton(abutton, on_click=button_click)
                b_Row.append(a)

            b_Column.append(ft.Row(b_Row))


        page.add(icon_menu,ft.Column(b_Column),total)

    make_buttons()

ft.app(main)

# total_elements = sum(len(row) for row in buttons)
#
# if score > total_elements / 2:
#     print('같은 아이콘을 전부 찾으셧습니다. ')
