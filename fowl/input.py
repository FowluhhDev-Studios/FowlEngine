import pyray as pr

keys = pr.KeyboardKey

def get_key(key):
    return pr.is_key_pressed(key)

def get_key_down(key):
    return pr.is_key_down(key)

def get_key_up(key):
    return pr.is_key_up(key)

