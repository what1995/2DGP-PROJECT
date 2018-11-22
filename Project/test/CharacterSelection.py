import game_framework
import random
from pico2d import *
import DeckSelection
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
#import CharacterSelection
import game_world

name = "characterSelection"
image = None
cheak = None
character = None
mouse_x,mouse_y=0,0
Enemycharacter=None
def enter():
    global image,character
    global cheak
    image = load_image('CharacterSelection.png')
    cheak = load_image('Character_Cheak.png')


def exit():
    global image



def handle_events():
    global character,Enemycharacter,mouse_x,mouse_y
    events = get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            game_framework.quit()
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y=event.x, 600- event.y
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.button)==(SDL_MOUSEBUTTONDOWN,SDL_BUTTON_LEFT):
                if mouse_x> 0 and mouse_x < 150:
                    character = 0
                elif mouse_x> 150 and mouse_x < 300:
                    character = 1
                elif mouse_x > 300 and mouse_x < 450:
                    character = 2
                elif mouse_x> 450 and mouse_x < 600:
                    character = 3
                if mouse_x > 0 and event.x < 600 and mouse_y<400:
                    game_framework.push_state(DeckSelection)



def draw():
    global mouse_x,mouse_y

    clear_canvas()
    image.draw(400,300)
    if 0< mouse_x and mouse_x<150 and mouse_y<400:
        cheak.draw(75,450)
    if 150< mouse_x and mouse_x<300 and mouse_y<400:
        cheak.draw(225,450)
    if 300< mouse_x and mouse_x<450 and mouse_y<400:
        cheak.draw(375,450)
    if 450< mouse_x and mouse_x<600 and mouse_y<400:
        cheak.draw(525,450)

    
    update_canvas()






def update():
    pass


def pause():
    global character


def resume():
    pass
