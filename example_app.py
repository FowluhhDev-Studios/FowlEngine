from fowl import init, input, draw, object, audio
from fowl.scene import scene, manager

# Constants
WIDTH = 640
HEIGHT = 480
FPS = 60

class LogoObject(object.Object):
    def __init__(self, image):
        self.image = draw.get_image("assets/%s.png" %image)
        self.rot = 0
        self.imagesize = 0.5
        self.texture = draw.get_texture(self.image)
    
    def draw(self):
        draw.draw_texture(draw.find_center(WIDTH, self.image.width*self.imagesize), draw.find_center(HEIGHT, self.image.height*self.imagesize) - 32, self.texture, self.imagesize, self.rot)
        return super().draw()

# Classes
class TestScene(scene.Scene):
    def init(self):
        print("Hello, TestScene!")
        self.text = "Hello, FowlEngine!"
        self.textsize = 32
        self.font = draw.get_font("assets/font.fnt")
        self.iname = "image"
        self.logo = LogoObject(self.iname)
        self.is_next = False
        self.music = audio.load_music("assets/music.mp3")
        audio.play_music(self.music)
        return super().init()
    
    def draw(self):
        self.logo.draw()
        draw.draw_text(draw.find_text_center(self.font, self.text, self.textsize), draw.find_center(HEIGHT, 24)+48, self.text, self.font, self.textsize)
        return super().draw()
    
    def update(self):
        audio.update_music(self.music)
        if input.get_key(input.keys.KEY_SPACE) or input.get_gamepad_button(input.gamepad_buttons.GAMEPAD_BUTTON_RIGHT_FACE_DOWN) or input.get_mouse(input.mouse.MOUSE_BUTTON_LEFT):
            self.is_next = not self.is_next
            if self.is_next:
                self.text = "Use this template to make your game!"
                self.textsize = 24
                self.iname = "image2"
                self.logo = LogoObject(self.iname)
                self.manager.change_bg(draw.get_color(255, 127, 0))
            else:
                self.text = "Hello, FowlEngine!"
                self.textsize = 32
                self.iname = "image"
                self.logo = LogoObject(self.iname)
                self.manager.change_bg(draw.get_color(127, 0, 255))
        
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

