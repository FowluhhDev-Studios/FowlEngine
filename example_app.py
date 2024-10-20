from fowl import init, input, draw, object
from fowl.scene import scene, manager

# Constants
WIDTH = 640
HEIGHT = 480
FPS = 60

class LogoObject(object.Object):
    def __init__(self):
        self.image = draw.get_image("assets/image.png")
        self.imagesize = 0.5
        self.texture = draw.get_texture(self.image)
    
    def draw(self):
        draw.draw_texture(draw.find_center(WIDTH, self.image.width*self.imagesize), draw.find_center(HEIGHT, self.image.height*self.imagesize) - 32, self.texture, self.imagesize)
        return super().draw()

# Classes
class TestScene(scene.Scene):
    def init(self):
        print("Hello, TestScene!")
        self.text = "Hello, FowlEngine!"
        self.textsize = 32
        self.font = draw.get_font("assets/font.fnt")
        self.logo = LogoObject()
        return super().init()
    
    def draw(self):
        self.logo.draw()
        draw.draw_text(draw.find_text_center(self.font, self.text, self.textsize), draw.find_center(HEIGHT, 24)+48, self.text, self.font, self.textsize)
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

