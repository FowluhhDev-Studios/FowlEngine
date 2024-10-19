import pyray as pr

def get_color(r, g, b, a = 255):
    return pr.Color(r, g, b, a)

def find_center(first, second):
    return int((first / 2) - (second / 2))

def anchor(scr_size, obj_size, offset, direction = -1):
    return int(scr_size + ((obj_size+offset)*-1))

def draw_rect(x, y, w, h, col):
    pr.draw_rectangle(x, y, w, h, col)

def draw_text(x, y, text, size, color):
    pr.draw_text(text, x, y, size, color)

def get_image(file_name):
    return pr.load_image(file_name)

def get_texture(image):
    return pr.load_texture_from_image(image)

def draw_texture(x, y, texture, tint = get_color(255, 255, 255)):
    pr.draw_texture(texture, x, y, tint)