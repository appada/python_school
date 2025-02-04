import asyncio
import random
import flet as ft

class Box:
    def __init__(self, size, color, initial_left, initial_top, img):
        self.size = size
        self.color = color
        self.left = initial_left
        self.top = initial_top
        self.img = img
        self.container = ft.Container(
            width=self.size,
            height=self.size,
            bgcolor=self.color,
            left=self.left,
            top=self.top,
            image_src=self.img
        )
        
    async def jump(self):
        initial_top = self.top
        self.top = max(0, self.top - 100)
        self.update()
        await asyncio.sleep(0.3)
        self.top = initial_top
        self.update()

    async def move(self, direction, step=10):
        if direction == "up":
            self.top = max(0, self.top - step)
        elif direction == "down":
            self.top = min(600 - self.size, self.top + step)
        elif direction == "left":
            self.left = max(0, self.left - step)
            self.container.image_src = 'z_flet/my_basic/1.png'
        elif direction == "right":
            self.left = min(600 - self.size, self.left + step)
            self.container.image_src = 'z_flet/my_basic/2.png'
        self.update()

    def update(self):
        self.container.top = self.top
        self.container.left = self.left
        self.container.update()

class RandomMovingBox(Box):
    async def move(self, direction, step=10):
        await super().move(direction, step)
        self.container.image_src = 'z_flet/my_basic/3.png'
        self.update()

    async def random_move(self):
        while True:
            direction = random.choice(["left", "right", "up", "down"])
            step = random.randint(5, 15)
            await self.move(direction, step)
            await asyncio.sleep(0.1)

async def main(page: ft.Page):
    page.title = "Cat Movement Example"
    page.window_width = 600
    page.window_height = 600

    box = Box(size=80, color=ft.colors.BLACK, initial_left=250, initial_top=250, img='z_flet/my_basic/1.png')
    random_box = RandomMovingBox(size=40, color=ft.colors.BLACK, initial_left=300, initial_top=300, img='z_flet/my_basic/3.png')
    
    async def on_key(e: ft.KeyboardEvent):
        if e.key == "Arrow Up":
            await box.move("up")
        elif e.key == "Arrow Down":
            await box.move("down")
        elif e.key == "Arrow Left":
            await box.move("left")
        elif e.key == "Arrow Right":
            await box.move("right")
        elif e.key == " ":
            await box.jump()

    page.on_keyboard_event = on_key

    # Add boxes to the page
    page.add(ft.Stack([box.container, random_box.container]))

    # Start the random movement for the random_box
    asyncio.create_task(random_box.random_move())

if __name__ == "__main__":
    ft.app(target=main)