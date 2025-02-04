import flet as ft 

class Box:
    def __init__(self, size, color, init_left, init_top, img):
        self.size = size
        self.color = color
        self.left = init_left
        self.top = init_top
        self.img = img
        self.container = ft.Container(
            width= self.size,
            height= self.size,
            bgcolor= self.color,
            left= self.left,
            top= self.top,
            image_src=self.img,
        )
        
    def move(self, direction, step=20):
        if direction == "up":
            self.top = max(0, self.top - step)
        elif direction == "down":
            self.top = min(600-self.size, self.top + step)
        elif direction == "left":
            self.left = max(0, self.left - step)
        elif direction == "right":
            self.left = min(600-self.size, self.left + step)
        self.update()
        
    def update(self):
        self.container.top = self.top
        self.container.left = self.left
        self.container.update()
        
def main(page:ft.Page):
    page.title = " Cat movement Ex"
    page.window.width = 600
    page.window.height = 600
    
    box = Box(size=80, color=ft.colors.TEAL, init_left=250, init_top=250, img='z_flet/my_basic/1.png')
    
    async def on_key (e:ft.KeyboardEvent):
        if e.key == "Arrow Up":
            await box.move("up")
        elif e.key == "Arrow Down":
            await box.move("down")
        elif e.key == "Arrow Left":
            await box.move("left")
        elif e.key == "Arrow Right":
            await box.move("right")
            
    page.on_keyboard_event = on_key
    
    page.add(
        ft.Stack([
            box.container    
        ])
    )
    
if __name__ == "__main__":
    ft.app(main)