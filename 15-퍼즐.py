import flet as ft
import random

def main(page: ft.Page):
    page.title = "15-퍼즐 게임"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # 게임 상태
    numbers = list(range(1, 16)) + [None]
    random.shuffle(numbers)

    # 게임 보드 생성
    board = ft.GridView(
        expand=1,
        runs_count=4,
        max_extent=100,
        child_aspect_ratio=1.0,
        spacing=5,
        run_spacing=5,
    )

    def check_win():
        if numbers == list(range(1, 16)) + [None]:
            page.dialog = ft.AlertDialog(
                title=ft.Text("축하합니다!"),
                content=ft.Text("퍼즐을 완성했습니다!"),
            )
            page.dialog.open = True
            page.update()

    def on_tile_click(e):
        index = board.controls.index(e.control)
        empty_index = numbers.index(None)
        # 인접한 타일인지 확인
        if (abs(index % 4 - empty_index % 4) + abs(index // 4 - empty_index // 4)) == 1:
            # 타일 교환
            numbers[index], numbers[empty_index] = numbers[empty_index], numbers[index]
            update_board()
            check_win()


    def update_board():
        board.controls.clear()
        for num in numbers:
            if num:
                board.controls.append(
                    ft.Container(
                        content=ft.Text(str(num), size=30, color='black'),
                        alignment=ft.alignment.center,
                        bgcolor=ft.Colors.BLUE_200,
                        border_radius=10,
                        on_click=on_tile_click,
                    )
                )
            else:
                board.controls.append(ft.Container())
        page.update()

    update_board()

    # 새 게임 버튼
    def new_game(e):
        random.shuffle(numbers)
        update_board()

    new_game_btn = ft.ElevatedButton("새 게임", on_click=new_game)

    page.add(ft.Container(board, width=410,height=410),
             new_game_btn)

ft.app(target=main)
