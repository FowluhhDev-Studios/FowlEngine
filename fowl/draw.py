import pyray as pr

def get_color(r, g, b, a = 255):
    return pr.Color(r, g, b, a)

def find_center(first, second):
    return int((first / 2) - (second / 2))

def anchor(scr_size, obj_size, offset, direction = -1):
    return int(scr_size + ((obj_size+offset)*direction))

def draw_rect(x, y, w, h, col):
    pr.draw_rectangle(x, y, w, h, col)

def draw_circle(x, y, radius, col):
    pr.draw_circle(x, y, radius, col)

def get_font(file_name):
    return pr.load_font(file_name)

def draw_text(x, y, text, font, size, spacing = 1, color = get_color(255, 255, 255)):
    pr.draw_text_ex(font, text, pr.Vector2(x, y), size, spacing, color)

def find_text_center(font, text, size, spacing = 1):
    return find_center(pr.get_screen_width(), pr.measure_text_ex(font, text, size, spacing).x)

def get_image(file_name):
    return pr.load_image(file_name)

def get_texture(image):
    return pr.load_texture_from_image(image)

def draw_texture(x, y, texture, size: tuple[float, float], rot = 0, tint = get_color(255, 255, 255)):
    pr.draw_texture_pro(texture, pr.Rectangle(0, 0, texture.width, texture.height), pr.Rectangle(x, y, texture.width*size[0], texture.height*size[1]), pr.Vector2(0, 0), rot, tint)

def draw_atlas_texture(dest_x, dest_y, atlas_x, atlas_y, atlas_w, atlas_h, texture, size: tuple[float, float], rot = 0, tint = get_color(255, 255, 255)):
    pr.draw_texture_pro(texture, pr.Rectangle(atlas_x, atlas_y, atlas_w, atlas_h), pr.Rectangle(dest_x, dest_y, atlas_w*size[0], atlas_h*size[1]), pr.Vector2(0, 0), rot, tint)