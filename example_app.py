from fowl import init, keys, draw
from fowl.scene import scene, manager

import pyray as pr

# Constants
WIDTH = 640
HEIGHT = 480
FPS = 60

# Classes
class TestScene(scene.Scene):
    def init(self):
        print("Hello, TestScene!")
        return super().init()
    
    def draw(self):
        # pr.draw_text("Hello", 5, 5, 20, pr.BLUE)
        draw.draw_rect(10, 10, 50, 50, draw.get_color(100, 120, 140, 50))
        return super().draw()
    
    def update(self):
        if keys.get_key_down(keys.keys.KEY_A):
            print("A")
        return super().update()

# Variables
title = "Hello, FowlEngine!"

man = manager.Manager()
testscn = TestScene()

# Initialize Window
init.init(WIDTH, HEIGHT, FPS, title)

# Switch scene to new TestScene
man.switch(testscn)

while init.can_draw():
    man.update()
    man.draw()

init.exit()