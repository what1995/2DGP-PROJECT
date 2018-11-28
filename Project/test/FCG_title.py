import game_framework
from pico2d import *


import CharacterSelection
import game_world

name = "TitleState"
image = None
start = None
music = None
def enter():
    global image, start,music
    image=load_image('./FCGimage/Main.png')
    start=load_image('./FCGimage/startButton.png')
    music = load_music('./Background/title.mp3')
    music.set_volume(40)
    music.repeat_play()


def exit():
    global image
    global start
    del(image)
    del(start)


def handle_events():
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(CharacterSelection)


def draw():
    clear_canvas()
    image.draw(400,300)
    start.draw(400,100)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass


