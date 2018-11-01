import game_framework
import random
from pico2d import *
import DeckSelection
import main_state
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
#import CharacterSelection
import game_world

name = "backgroundSelection"
Main=None
logo =None
BGbamboo = None
BGHakureiShrine = None
BGclocktower = None
minibamboo = None
miniHakureiShrine = None
miniclocktower = None
BGcheak=None
cheak = None
mouse_x,mouse_y=0,0
def enter():
    global BGbamboo,BGHakureiShrine,BGclocktower,Main,minibamboo,miniHakureiShrine,miniclocktower,logo
    global cheak,BGcheak
    Main= load_image('Main.png')
    logo = load_image('BackGround logo.png')
    BGbamboo = load_image('BGbamboo.png')
    BGHakureiShrine = load_image('BGHakurei Shrine.png')
    BGclocktower = load_image('BGclock tower.png')
    minibamboo = load_image('minibamboo.png')
    miniHakureiShrine = load_image('miniHakurei Shrine.png')
    miniclocktower = load_image('miniclock tower.png')
    cheak = load_image('Character_Cheak.png')


def exit():
    global BGbamboo,BGHakureiShrine,BGclocktower



def handle_events():
    global mouse_x,mouse_y,BGcheak
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
                if 50< mouse_x and mouse_x<250 and mouse_y<375 and mouse_y>225:
                    BGcheak=0
                    game_framework.push_state(main_state)
                elif 300< mouse_x and mouse_x<500 and mouse_y<375 and mouse_y>225:
                    BGcheak=1
                    game_framework.push_state(main_state)
                elif 550< mouse_x and mouse_x<750 and mouse_y<375 and mouse_y>225:
                    BGcheak=2
                    game_framework.push_state(main_state)




def draw():
    global mouse_x,mouse_y,BGcheak

    clear_canvas()
    Main.draw(400, 300)
    if 50< mouse_x and mouse_x<250 and mouse_y<375 and mouse_y>225:
        BGbamboo.draw(400, 300)
        cheak.draw(150,450)
    if 300< mouse_x and mouse_x<500 and mouse_y<375 and mouse_y>225:
        BGHakureiShrine.draw(400, 300)
        cheak.draw(400,450)
    if 550< mouse_x and mouse_x<750 and mouse_y<375 and mouse_y>225:
        BGclocktower.draw(400, 300)
        cheak.draw(650,450)

    minibamboo.draw(150,300)
    miniHakureiShrine.draw(400, 300)
    miniclocktower.draw(650, 300)
    logo.draw(400,550)
    update_canvas()






def update():
    pass



def pause():
    pass



def resume():
    pass
