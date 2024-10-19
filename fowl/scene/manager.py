import pyray as pr

class Manager:
    def __init__(self):
        self.scene = None
        self.color = pr.BLACK

    def switch(self, new_scene):
        self.scene = new_scene
        self.scene.manager = self
        self.scene.init()

    def change_bg(self, color):
        self.color = color

    def draw(self):
        if self.scene != None and self.color != None:
            pr.begin_drawing()
            pr.clear_background(self.color)
            self.scene.draw()
            pr.end_drawing()

    def update(self):
        if self.scene != None:
            self.scene.update()