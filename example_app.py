from fowl import init, keys, draw
from fowl.scene import scene, manager

# Constants
WIDTH = 640
HEIGHT = 480
FPS = 60

# Classes
class TestScene(scene.Scene):
    def init(self):
        print("Hello, TestScene!")
        self.image = draw.get_image("image.png")
        self.texture = draw.get_texture(self.image)
        self.offx = 10
        self.offy = 10
        return super().init()
    
    def draw(self):
        draw.draw_texture(draw.find_center(WIDTH, self.image.width), draw.find_center(HEIGHT, self.image.height), self.texture)
        #draw.draw_rect(10, 10, 50, 50, draw.get_color(255, 255, 255))
        #draw.draw_rect(draw.anchor(WIDTH, 50, self.offx), 10, 50, 50, draw.get_color(255, 255, 255))
        #draw.draw_rect(10, draw.anchor(HEIGHT, 50, self.offy), 50, 50, draw.get_color(255, 255, 255))
        #draw.draw_rect(draw.anchor(WIDTH, 50, self.offx), draw.anchor(HEIGHT, 50, self.offy), 50, 50, draw.get_color(255, 255, 255))
        return super().draw()
    
    def update(self):
        return super().update()

# Variables
title = "Hello, FowlEngine!"

man = manager.Manager()
testscn = TestScene()

# Initialize Window
init.init(WIDTH, HEIGHT, FPS, title)

# Switch scene to new TestScene
man.switch(testscn)

man.change_bg(draw.get_color(127, 0, 255))

while init.can_draw():
    man.update()
    man.draw()

init.exit()

