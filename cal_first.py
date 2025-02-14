import flet as ft


def main(page: ft.Page):
    page.title = "Calculator Example"
# 계산을 하는 함수 입니다. if 문으로  +-/*  구분해서 계산하게 합니다.
# try except 는 숫자 이외의 다른값이 입력되면 오류가 발생됨으로 예외처리입니다.
    def calculate(e):
        try:
            num1 = float(input1.value)
            num2 = float(input2.value)
            if e.control.text == "+":
                res = num1 + num2
            elif e.control.text == "-":
                res = num1 - num2
            elif e.control.text == "*":
                res = num1 * num2
            elif e.control.text == "/":
                res = num1 / num2
            elif e.control.text == "//":
                res = num1 // num2
            elif e.control.text == "**":
                res = num1 ** num2
            result.value = f" = {res}"
            cal_text.value = e.control.text
        except ValueError:
            result.value = "숫자를 입력하세요"
        page.update()


    # 숫자를 입력받는 TextField 컨트롤
    input1 = ft.TextField(label="Input 1", width=100)
    input2 = ft.TextField(label="Input 2", width=100)
    #계산 기호 표시할 컨트롤
    cal_text = ft.Text(" ", size=20)
    # 결과 Text 컨트롤
    result = ft.Text(value="Result: ", size=30)
    input_row = ft.Row([input1, cal_text, input2, result])


    # 계산버튼 리스트, 버튼들은 한줄(Row)에 배치합니다.세로는 Column
    # Row Column 은 3장을 참고해 주세요.
    button_list = ft.Row([
                ft.ElevatedButton(text="+", on_click=calculate),
                ft.ElevatedButton(text="-", on_click=calculate),
                ft.ElevatedButton(text="*", on_click=calculate),
                ft.ElevatedButton(text="/", on_click=calculate),
                ft.ElevatedButton(text="//", on_click=calculate),
                ft.ElevatedButton(text="**", on_click=calculate),
            ])


    # 페이지에 컨트롤 위젯들을 추가합니다

    page.add(
        input_row,
        button_list,

    )
    page.update()


ft.app(target=main)
