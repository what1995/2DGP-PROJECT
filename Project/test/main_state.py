import random
import json
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
from pico2d import *
import game_framework
import DeckSelection
import iku
import game_world
from iku import Iku
from reimu import Reimu
from tenshi import Tenshi
from marisa import Marisa
from background import BackGround
from PlayerHP import Player_HP
from EnemyHP import Enemy_HP
from Enemy_marisa import Enemy_Marisa
from Enemy_reimu import Enemy_Reimu
from Enemy_tenshi import Enemy_Tenshi
from Enemy_iku import Enemy_Iku

name = "MainState"
turncheak=0
iku = None
reimu=None
tenshi=None
marisa=None
grass = None
Enemy_marisa=None
Enemy_reimu =None
Enemy_tenshi=None
Enemy_iku=None
Player = None
EnemyPlayer=None
turn = 1
skillcheak=0
def enter():
    global iku, background, Player,reimu,tenshi,marisa,PlayerHP,EnemyHP,Enemy_marisa,Enemy_reimu,Enemy_tenshi,Enemy_iku,EnemyPlayer,turn
    Player = DeckSelection.character
    EnemyPlayer=DeckSelection.Enemycharacter
    if turn == 1:
        if EnemyPlayer == 0:
            Enemy_marisa = Enemy_Marisa()
            game_world.add_object(Enemy_marisa, 1)
        elif EnemyPlayer == 1:
            Enemy_reimu = Enemy_Reimu()
            game_world.add_object(Enemy_reimu, 1)
        elif EnemyPlayer == 2:
            Enemy_iku = Enemy_Iku()
            game_world.add_object(Enemy_iku, 1)
        elif EnemyPlayer == 3:
            Enemy_tenshi = Enemy_Tenshi()
            game_world.add_object(Enemy_tenshi, 1)
        if Player == 0:
            reimu = Reimu()
            game_world.add_object(reimu, 1)
        elif Player == 1:
            marisa = Marisa()
            game_world.add_object(marisa, 1)
        elif Player == 2:
            iku = Iku()
            game_world.add_object(iku, 1)
        elif Player == 3:
            tenshi = Tenshi()
            game_world.add_object(tenshi, 1)
    elif turn== -1:
        if Player==0:
            reimu = Reimu()
            game_world.add_object(reimu, 1)
        elif Player==1:
            marisa = Marisa()
            game_world.add_object(marisa, 1)
        elif Player==2:
            iku = Iku()
            game_world.add_object(iku, 1)
        elif Player == 3:
            tenshi = Tenshi()
            game_world.add_object(tenshi, 1)
        if EnemyPlayer==0:
            Enemy_marisa=Enemy_Marisa()
            game_world.add_object(Enemy_marisa, 1)
        elif EnemyPlayer==1:
            Enemy_reimu = Enemy_Reimu()
            game_world.add_object(Enemy_reimu, 1)
        elif EnemyPlayer==2:
            Enemy_iku=Enemy_Iku()
            game_world.add_object(Enemy_iku, 1)
        elif EnemyPlayer == 3:
            Enemy_tenshi=Enemy_Tenshi()
            game_world.add_object(Enemy_tenshi, 1)
    background = BackGround()
    PlayerHP=Player_HP()
    EnemyHP=Enemy_HP()
    game_world.add_object(background,0)
    game_world.add_object(PlayerHP, 0)
    game_world.add_object(EnemyHP, 0)



def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global iku, background, Player, reimu, tenshi, marisa, PlayerHP, EnemyHP, Enemy_marisa, Enemy_reimu, Enemy_tenshi, Enemy_iku, EnemyPlayer, turn,turncheak
    global skillcheak
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            turn = turn * -1
            turncheak=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_1:
            skillcheak=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
            skillcheak=2
        elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
            skillcheak=3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_4:
            skillcheak=4
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_world.remove_object(reimu)
                game_world.remove_object(marisa)
                game_world.remove_object(iku)
                game_world.remove_object(tenshi)
                game_world.remove_object(Enemy_reimu)
                game_world.remove_object(Enemy_marisa)
                game_world.remove_object(Enemy_iku)
                game_world.remove_object(Enemy_tenshi)
                game_framework.push_state(DeckSelection)

        else:
            if Player == 0 and turn ==1:
                reimu.handle_event(event)
            if Player == 1and turn ==1:
                marisa.handle_event(event)
            if Player == 2and turn ==1:
                iku.handle_event(event)
            if Player == 3and turn ==1:
                tenshi.handle_event(event)
            if EnemyPlayer==0and turn ==-1:
                Enemy_marisa.handle_event(event)
            if EnemyPlayer==1and turn ==-1:
                Enemy_reimu.handle_event(event)
            if EnemyPlayer==2and turn ==-1:
                Enemy_iku.handle_event(event)
            if EnemyPlayer==3and turn ==-1:
                Enemy_tenshi.handle_event(event)



def update():
    global iku, background, Player, reimu, tenshi, marisa, PlayerHP, EnemyHP, Enemy_marisa, Enemy_reimu, Enemy_tenshi, Enemy_iku, EnemyPlayer, turn, turncheak

    for game_objcet in game_world.all_objects():
        game_objcet.update()
        if(turncheak==1):
            game_world.remove_object(reimu)
            game_world.remove_object(marisa)
            game_world.remove_object(iku)
            game_world.remove_object(tenshi)
            game_world.remove_object(Enemy_reimu)
            game_world.remove_object(Enemy_marisa)
            game_world.remove_object(Enemy_iku)
            game_world.remove_object(Enemy_tenshi)
            if turn == 1:
                if EnemyPlayer == 0:
                    Enemy_marisa = Enemy_Marisa()
                    game_world.add_object(Enemy_marisa, 1)
                elif EnemyPlayer == 1:
                    Enemy_reimu = Enemy_Reimu()
                    game_world.add_object(Enemy_reimu, 1)
                elif EnemyPlayer == 2:
                    Enemy_iku = Enemy_Iku()
                    game_world.add_object(Enemy_iku, 1)
                elif EnemyPlayer == 3:
                    Enemy_tenshi = Enemy_Tenshi()
                    game_world.add_object(Enemy_tenshi, 1)
                if Player == 0:
                    reimu = Reimu()
                    game_world.add_object(reimu, 1)
                elif Player == 1:
                    marisa = Marisa()
                    game_world.add_object(marisa, 1)
                elif Player == 2:
                    iku = Iku()
                    game_world.add_object(iku, 1)
                elif Player == 3:
                    tenshi = Tenshi()
                    game_world.add_object(tenshi, 1)
            elif turn == -1:
                if Player == 0:
                    reimu = Reimu()
                    game_world.add_object(reimu, 1)
                elif Player == 1:
                    marisa = Marisa()
                    game_world.add_object(marisa, 1)
                elif Player == 2:
                    iku = Iku()
                    game_world.add_object(iku, 1)
                elif Player == 3:
                    tenshi = Tenshi()
                    game_world.add_object(tenshi, 1)
                if EnemyPlayer == 0:
                    Enemy_marisa = Enemy_Marisa()
                    game_world.add_object(Enemy_marisa, 1)
                elif EnemyPlayer == 1:
                    Enemy_reimu = Enemy_Reimu()
                    game_world.add_object(Enemy_reimu, 1)
                elif EnemyPlayer == 2:
                    Enemy_iku = Enemy_Iku()
                    game_world.add_object(Enemy_iku, 1)
                elif EnemyPlayer == 3:
                    Enemy_tenshi = Enemy_Tenshi()
                    game_world.add_object(Enemy_tenshi, 1)
            turncheak=0



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







