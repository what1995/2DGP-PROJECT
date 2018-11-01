import game_framework
from pico2d import *
import CharacterSelection


name = "TitleState"
image = None
start = None

def enter():
    global image
    global start
    image=load_image('Main.png')
    start=load_image('startButton.png')


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


