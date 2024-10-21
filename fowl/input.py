import pyray as pr

keys = pr.KeyboardKey
gamepad_buttons = pr.GamepadButton
gamepad_axis = pr.GamepadAxis
mouse = pr.MouseButton

def get_key(key):
    return pr.is_key_pressed(key)

def get_key_down(key):
    return pr.is_key_down(key)

def get_key_up(key):
    return pr.is_key_up(key)

def get_mouse(button):
    return pr.is_mouse_button_pressed(button)

def get_mouse_down(button):
    return pr.is_mouse_button_down(button)

def get_mouse_up(button):
    return pr.is_mouse_button_up(button)

def get_gamepad_button(gamepadbutton, id = 0):
    return pr.is_gamepad_button_pressed(id, gamepadbutton)

def get_gamepad_button_down(gamepadbutton, id = 0):
    return pr.is_gamepad_button_down(id, gamepadbutton)

def get_gamepad_button_up(gamepadbutton, id = 0):
    return pr.is_gamepad_button_up(id, gamepadbutton)

def get_gamepad_axis(axis, id = 0):
    return pr.get_gamepad_axis_movement(id, axis)