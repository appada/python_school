#def 99dan():
# for x in range(2, 10):
# print(f"{i}단:")
#     for y in range(1, 10):
#         print(f"{x} x {y} = {x * y}")

# def 19dan():
#     for i in range(2, 20):
#         print(f"{i}단:")
#         for j in range(1, 10):
#             print(f"{i} x {j} = {i * j}")
#         print()  # 각 단 사이에 빈 줄 추가

# num = int(input("정수를 입력하세요: "))
# if num % 2 == 0:
#     print(f"입력한 정수 {num}은 짝 수 입니다.")
# else:
#     print(f"입력한 정수 {num}은 홀 수 입니다.")

# num = int(input("임의의 정수 입력: "))
# for x in range(1, num + 1, 2):
#     print(x)
# for x in range(2, num + 1, 2):

menu = { "붕어빵" : 1000, "슈크림빵": 2000, "도너츠":2000, "햄버거":4000, "오렌지쥬스":4000, "녹차":3000}
print(menu)

for item in menu:
    print(item, end='\t')
    print(menu[item])

money = int(input('얼마를 입력할까요? '))

selected = []
while True:
    print(menu)
    select = input('메뉴이름을 입력하세요 : ')
    if select in menu:
        selected.append(select)
        price = menu.get(select)
        if money < price:
            print(f'돈이 모자랍니다. 선택을 종료합니다. 남은돈{money}')
            print(f' {selected} 포장합니다. 잔돈 :{money}')
            break
        else:
            money = money - price # money -= price
            print(f' {money}원이 남았습니다.')
            print(f' 선택한 메뉴 : {selected}')
    print("")#빈칸





#
# import random
#
# import flet as ft
#
# def main(page:ft.Page):
#
#     buttons = [
#         ["😊", "🐳", "⏰", "❤️", "✨"],
#         ["❤️", "😊", "🐳", "⏰", "✨"],
#         ["🐳", "⏰", "❤️", "😊", "✨"],
#         ["⏰", "😊", "🐳", "❤️", "✨"],
#         ["⏰", "✨", "🐳", "❤️", "😊"],
#         ["⏰", "✨", "🐳", "❤️", "😊"],
#     ]
#
#     def input_click(e):
#         icon_list = list(input_icon.value)
#         buttons.clear()
#
#         for row in range(len(icon_list)):
#             icon_row = []
#             for icon in icon_list:
#                 icon_row.append(icon)
#             random.shuffle(icon_row)
#             buttons.append(icon_row)
#         make_buttons()
#
#
#     input_icon = ft.TextField(label='icon here')
#     input_button = ft.ElevatedButton('Make', on_click=input_click)
#     icon_menu = ft.Row([ input_icon, input_button])
#
#
#     for i in buttons:
#         random.shuffle(i)
#
#     twin_check=[]
#     two_color = 'red'
#     count = 0
#     score = 0
#
#     total = ft.Text(value=score, size=30)
#
#     def button_click(e):
#         button = e.control
#         nonlocal count, two_color, score
#         button.bgcolor = two_color
#
#         count += 1
#         if count >= 2 :
#             two_color = ft.Colors.random()
#             count = 0
#
#         twin_check.append(button.text)
#         if len(twin_check) >= 2 :
#             if twin_check[0] == twin_check[1]:
#                 score += 1
#                 total.value=score
#                 twin_check.clear()
#             twin_check.clear()
#         page.update()
#
#     def make_buttons():
#         page.clean()
#         b_Column = []
#         for row in buttons:
#             b_Row = []
#             for abutton in row:
#                 a = ft.ElevatedButton(abutton, on_click=button_click)
#                 b_Row.append(a)
#
#             b_Column.append(ft.Row(b_Row))
#
#
#         page.add(icon_menu,ft.Column(b_Column),total)
#
#     make_buttons()
#
# ft.app(main)

# total_elements = sum(len(row) for row in buttons)
#
# if score > total_elements / 2:
#     print('같은 아이콘을 전부 찾으셧습니다. ')
