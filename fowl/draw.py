import pyray as pr

def get_color(r, g, b, a = 255):
    return pr.Color(r, g, b, a)

def draw_rect(x, y, w, h, col):
    pr.draw_rectangle(x, y, w, h, col)