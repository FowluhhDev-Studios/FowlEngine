import pyray as pr

def load_music(file_name):
    return pr.load_music_stream(file_name)

def load_sound(file_name):
    return pr.load_sound(file_name)

def play_music(music):
    pr.play_music_stream(music)

def update_music(music):
    pr.update_music_stream(music)

def pause_music(music):
    pr.pause_music_stream(music)

def resume_music(music):
    pr.resume_music_stream(music)

def stop_music(music):
    pr.stop_music_stream(music)

def play_sound(sound):
    pr.play_sound(sound)

def stop_sound(sound):
    pr.stop_sound(sound)