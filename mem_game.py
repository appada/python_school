import time
import flet 
from flet import *
import random

class GridMenu(UserControl):
    
    def __init__(self,difficulty):
        self.grid = Column(opacity=0, animate_opacity=300)#opacity = visible
        self.grey_tiles: int = 0
        self.correct : int = 0
        self.incorrect : int = 0
        self.difficulty: int = difficulty    
        super().__init__()
        
    def show_color(self, e):
        print(e.data)
        if e.control.data == "grey" : 
            e.control.bgcolor = "green"
            e.control.opacity = 1
            e.control.update()
            # increase correct num
            self.correct += 1
            e.page.update()
        
        else:
            e.control.bgcolor = "red"
            e.control.opacity = 1
            e.control.update()
            self.incorrect += 1
            e.page.update()
        
        
                
    def build(self):
        
        rows = [ 
            Row(
                alignment=MainAxisAlignment.CENTER,
                controls=[Container(width=55, height=55, animate=300, 
                                    #show when clicks a box
                                    on_click=lambda e:self.show_color(e) ) for _ in range(5)]
            ) for _ in range(5)
        ]
        
        colors = ['blue', 'grey']
        for row in rows:
            for container in row.controls:
                #pass a parameter ,level
                container.bgcolor = random.choices(colors, weights=[10, self.difficulty])[0]
                if container.bgcolor == 'grey': #
                    self.grey_tiles +=1
        
        print(f'grey tiles ={self.grey_tiles}')
        
        self.grid.controls = rows
        return self.grid

def main(page: Page):
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    
    stage = Text(size=15, weight='bold')
    result = Text(size=20, weight='bold')
    start_button = Container(content=ElevatedButton(
        on_click=lambda e:start_game(e,GridMenu(2) ), content=Text('START', size=15, weight='bold'),
        width=200
    ))
    
    
            
    
    page.add(
        Row(alignment=MainAxisAlignment.CENTER, controls=[
            Text("memory game", size=30)
        ]),
        
        Row(alignment=MainAxisAlignment.CENTER, controls=[result]),
        Divider(height=20, color="transparent"),
        Row(alignment=MainAxisAlignment.CENTER, controls=[stage]),
        Divider(height=20, color="transparent"),
        Row(alignment=MainAxisAlignment.CENTER, controls=[start_button]),
    )
    
    #game_start
    def start_game(e, level):
        result.value =''
        grid = level
        page.controls.insert(3, grid)
        page.update()
        grid.grid.opacity=1
        grid.grid.update() #controls[0]
        
        #change stage num
        stage.value = f"Stage : {grid.difficulty -1}"
        stage.update()
        
        #prevent from clicking it twice
        start_button.disabled = True
        start_button.update()
        
        time.sleep(1.5) #time for how long tiles are shown
        
        #hide tile after sleep
        for rows in grid.controls[0].controls:
            for container in rows.controls:
                if container.bgcolor == "grey":
                    container.data = "grey" #
                    container.bgcolor="blue"
                    container.update()
                    
        while True:
            if grid.correct == grid.grey_tiles:
                grid.grid.disabled = True
                grid.grid.update()
                
                # win title
                result.value = " Success , You got all tiles"
                result.color = "green"
                result.update()
                
                time.sleep(2)
                
                result.value = ""
                page.controls.remove(grid)
                page.update()
                
                difficulty = grid.difficulty + 1
                
                start_game(e, GridMenu(difficulty))
                break
            
            # check out of try
            if grid.incorrect == 3:
                result.value = "Sorry , you ran out if tries. try again"
                result.color = "red"
                result.update()
                time.sleep(2)
                page.controls.remove(grid)
                page.update()
                start_button.disabled = False
                start_button.update()
                break
                
                
    
    page.update()    

if __name__ == "__main__":
    flet.app(target=main)
