import random
import json
import EnemyHP
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
from pico2d import *
import game_framework
import FCG_title
import DeckSelection
import Deck
import ikuSkill
import marisaSkill
import reimuSkill
import tenshiSkill
import game_world
import EnemyHP
import PlayerHP
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
from backgroundmusic import BG_Music
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
Bg_Music=None
turn = 1
DeckShow=1
Character_Motion_Cheak=False
Enemy_Motion_Cheak=False
End=False
reimu_skill1_atk_cheak=0
reimu_skill2_atk_cheak=0
reimu_skill3_atk_cheak=0
reimu_last_atk_cheak=0

marisa_skill1_atk_cheak=None
marisa_skill2_atk_cheak=None
marisa_skill3_atk_cheak=None
marisa_last_atk_cheak=None


iku_skill1_atk_cheak=None
iku_skill2_atk_cheak=None
iku_skill3_atk_cheak=None
iku_last_atk_cheak=None

tenshi_skill1_atk_cheak=None
tenshi_skill2_atk_cheak=None
tenshi_skill3_atk_cheak=None
tenshi_last_atk_cheak=None

reimu_skill1_effect=None
marisa_skill1_effect=None
iku_skill1_effect=None
tenshi_skill1_effect=None

enemy_reimu_skill1_effect=None
enemy_marisa_skill1_effect=None
enemy_iku_skill1_effect=None
enemy_tenshi_skill1_effect=None

Player_AtkBuff=1
Player_DefBuff=1

Enemy_AtkBuff=1
Enemy_DefBuff=1

HPcheak=0
HP=0 #enemy
P_HP=0
P_HPcheak=0
HPinit = 0
P_HPinit = 0
Skill1_Start= False
Skill2_Start= False
Skill3_Start= False
Last_Start= False
def enter():
    global iku, background,reimu,tenshi,marisa,PlayerHP,EnemyHP,Enemy_marisa,Enemy_reimu,Enemy_tenshi,Enemy_iku,EnemyPlayer,turn,deck,damageheak
    global reimu_skill1_effect,marisa_skill1_effect,iku_skill1_effect,tenshi_skill1_effect, Bg_Music,HPinit,P_HPinit,DeckShow,End
    global enemy_reimu_skill1_effect,enemy_marisa_skill1_effect,enemy_iku_skill1_effect,enemy_tenshi_skill1_effect,Character_Motion_Cheak,Enemy_Motion_Cheak
    Character_Motion_Cheak = False
    Enemy_Motion_Cheak = False
    End=False
    EnemyPlayer=DeckSelection.Enemycharacter
    Bg_Music =BG_Music()
    game_world.add_object(Bg_Music, 0)
    HPinit=1
    P_HPinit=1
    turn=1
    DeckShow=1


    if EnemyPlayer == 0:
        Enemy_reimu = Enemy_Reimu()
        enemy_reimu_skill1_effect = reimuSkill.REIMU_Skill1()
        game_world.add_object(enemy_reimu_skill1_effect, 2)
        game_world.add_object(Enemy_reimu, 1)
    elif EnemyPlayer == 1:
        Enemy_marisa = Enemy_Marisa()
        enemy_marisa_skill1_effect = marisaSkill.MARISA_Skill1()
        game_world.add_object(enemy_marisa_skill1_effect, 2)
        game_world.add_object(Enemy_marisa, 1)
    elif EnemyPlayer == 2:
        Enemy_iku = Enemy_Iku()
        enemy_iku_skill1_effect=ikuSkill.IKU_Skill1()
        game_world.add_object(enemy_iku_skill1_effect, 2)
        game_world.add_object(Enemy_iku, 1)
    elif EnemyPlayer == 3:
        Enemy_tenshi = Enemy_Tenshi()
        enemy_tenshi_skill1_effect=tenshiSkill.TENSHI_Skill1()
        game_world.add_object(enemy_tenshi_skill1_effect, 2)
        game_world.add_object(Enemy_tenshi, 1)
    if DeckSelection.character == 0:
        reimu = Reimu()
        reimu_skill1_effect = reimuSkill.REIMU_Skill1()
        game_world.add_object(reimu_skill1_effect, 2)
        game_world.add_object(reimu, 1)
    elif DeckSelection.character == 1:
        marisa = Marisa()
        marisa_skill1_effect=marisaSkill.MARISA_Skill1()
        game_world.add_object(marisa_skill1_effect, 2)
        game_world.add_object(marisa, 1)
    elif DeckSelection.character == 2:
        iku = Iku()
        game_world.add_object(iku, 1)
        iku_skill1_effect = ikuSkill.IKU_Skill1()
        game_world.add_object(iku_skill1_effect, 2)
    elif DeckSelection.character == 3:
        tenshi = Tenshi()
        tenshi_skill1_effect = tenshiSkill.TENSHI_Skill1()
        game_world.add_object(tenshi_skill1_effect, 2)
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
    EnemyHP.damage = 0
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    global iku, background, reimu, tenshi, marisa, PlayerHP, EnemyHP, Enemy_marisa, Enemy_reimu, Enemy_tenshi, Enemy_iku, EnemyPlayer, turn,turncheak
    global damageheak,Bg_Music,HP,HPinit,P_HPinit
    global reimu_skill1_effect, marisa_skill1_effect, iku_skill1_effect, tenshi_skill1_effect, Bg_Music
    global enemy_reimu_skill1_effect, enemy_marisa_skill1_effect, enemy_iku_skill1_effect, enemy_tenshi_skill1_effect
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            if End==True and Enemy_Motion_Cheak == False and Character_Motion_Cheak ==False:
                HPinit = 1
                P_HPinit = 1
                game_world.remove_object(reimu_skill1_effect)
                game_world.remove_object(marisa_skill1_effect)
                game_world.remove_object(iku_skill1_effect)
                game_world.remove_object(tenshi_skill1_effect)
                game_world.remove_object(enemy_reimu_skill1_effect)
                game_world.remove_object(enemy_marisa_skill1_effect)
                game_world.remove_object(enemy_iku_skill1_effect)
                game_world.remove_object(enemy_tenshi_skill1_effect)
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
                game_framework.push_state(FCG_title)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_v:
            Deck.spellcheak += 3
        elif event.type == SDL_KEYDOWN and event.key == SDLK_z:
            HPinit,P_HPinit=1 ,1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            HPinit=1
            P_HPinit=1
            game_world.remove_object(reimu_skill1_effect)
            game_world.remove_object(marisa_skill1_effect)
            game_world.remove_object(iku_skill1_effect)
            game_world.remove_object(tenshi_skill1_effect)
            game_world.remove_object(enemy_reimu_skill1_effect)
            game_world.remove_object(enemy_marisa_skill1_effect)
            game_world.remove_object(enemy_iku_skill1_effect)
            game_world.remove_object(enemy_tenshi_skill1_effect)
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
            Bg_Music.bgm.stop()
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



def update():
    global skill1_atk_cheak,skill2_atk_cheak,skill3_atk_cheak,last_atk_cheak
    for game_objcet in game_world.all_objects():
        game_objcet.update()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()







