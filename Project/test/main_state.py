import random
import json
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
from pico2d import *
import game_framework
import DeckSelection
import Deck
import iku
import ikuSkill
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
from Deck import PlayDeck
#from ikuSkill import IKU_Skill1

name = "MainState"
turncheak=0
iku = None
reimu=None
tenshi=None
marisa=None
Enemy_marisa=None
Enemy_reimu =None
Enemy_tenshi=None
Enemy_iku=None
EnemyPlayer=None
deck=None
turn = 1
skillcheak=0
iku_skill1_effect=None
Player_AtkBuff=1
Player_DefBuff=1
HPcheak=0
HP=0
def enter():
    global iku, background,reimu,tenshi,marisa,PlayerHP,EnemyHP,Enemy_marisa,Enemy_reimu,Enemy_tenshi,Enemy_iku,EnemyPlayer,turn,deck
    global iku_skill1_effect
    EnemyPlayer=DeckSelection.Enemycharacter


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
    if DeckSelection.character == 0:
        reimu = Reimu()
        game_world.add_object(reimu, 1)
    elif DeckSelection.character == 1:
        marisa = Marisa()
        game_world.add_object(marisa, 1)
    elif DeckSelection.character == 2:
        iku = Iku()
        game_world.add_object(iku, 1)
        iku_skill1_effect = ikuSkill.IKU_Skill1()
        game_world.add_object(iku_skill1_effect, 2)
    elif DeckSelection.character == 3:
        tenshi = Tenshi()
        game_world.add_object(tenshi, 1)
    background = BackGround()
    PlayerHP=Player_HP()
    EnemyHP=Enemy_HP()
    deck=PlayDeck()
    game_world.add_object(deck, 1)
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
    global iku, background, reimu, tenshi, marisa, PlayerHP, EnemyHP, Enemy_marisa, Enemy_reimu, Enemy_tenshi, Enemy_iku, EnemyPlayer, turn,turncheak
    global skillcheak,iku_skill1_effect
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_v:
            Deck.spellcheak += 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_world.remove_object(iku_skill1_effect)
                game_world.remove_object(reimu)
                game_world.remove_object(marisa)
                game_world.remove_object(iku)
                game_world.remove_object(tenshi)
                game_world.remove_object(Enemy_reimu)
                game_world.remove_object(Enemy_marisa)
                game_world.remove_object(Enemy_iku)
                game_world.remove_object(Enemy_tenshi)
                game_world.remove_object(background)
                game_world.remove_object(PlayerHP)
                game_world.remove_object(EnemyHP)
                game_world.remove_object(deck)
                game_framework.push_state(DeckSelection)

        else:
            if DeckSelection.character == 0 and turn ==1:
                reimu.handle_event(event)
            if DeckSelection.character == 1and turn ==1:
                marisa.handle_event(event)
            if DeckSelection.character == 2and turn ==1:
                iku.handle_event(event)
            if DeckSelection.character == 3and turn ==1:
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



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







