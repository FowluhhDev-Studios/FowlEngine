import pyray as pr

def init(width: int, height: int, fps: int, title: str):
    pr.init_window(width, height, title)
    pr.set_target_fps(fps)

def can_draw():
    return not pr.window_should_close()

def get_fps():
    return pr.get_fps()

def exit():
    pr.close_window()