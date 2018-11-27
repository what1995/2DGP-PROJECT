from pico2d import *
import os
import EnemyHP
import main_state
import random
import DeckSelection
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import game_world
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import BackgroundSelection
import PlayerHP
#tenshi stand
STAND_TIME_PER_ACTION=0.8
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
STAND_PER_ACTION=6

#skill1
SKILL1TIME_PER_ACTION=2
SKILL1ACTION_PER_TIME= 1.0/SKILL1TIME_PER_ACTION
SKILL1_PER_ACTION=16

#skill2
SKILL2TIME_PER_ACTION=2
SKILL2ACTION_PER_TIME= 1.0/SKILL2TIME_PER_ACTION
SKILL2_PER_ACTION=22

#skill3
SKILL3TIME_PER_ACTION=1.5
SKILL3ACTION_PER_TIME= 1.0/SKILL3TIME_PER_ACTION
SKILL3_PER_ACTION=17
# iku lastspell Action Speed
LASTTIME_PER_ACTION=2
LASTACTION_PER_TIME= 1.0/LASTTIME_PER_ACTION
LASTCHEAK_PER_ACTION=21
#Damage
DAMAGETIME_PER_ACTION=1
DAMAGEACTION_PER_TIME= 1.0/DAMAGETIME_PER_ACTION
DAMAGE_PER_ACTION=6

#Down
DOWNTIME_PER_ACTION=3
DOWNACTION_PER_TIME= 1.0/DOWNTIME_PER_ACTION
DOWN_PER_ACTION=21
#item use
ITEM1TIME_PER_ACTION=1
ITEM1ACTION_PER_TIME= 1.0/ITEM1TIME_PER_ACTION
ITEM1_PER_ACTION=16
#motion speed
PIXEL_PER_METER=(10.0/0.3)
MOTION_SPEED_KMPH = 0.2
MOTION_SPEED_MPM = (MOTION_SPEED_KMPH*1000.0/60.0)
MOTION_SPEED_MPS=(MOTION_SPEED_MPM/60.0)
MOTION_SPEED_PPS=(MOTION_SPEED_MPS*PIXEL_PER_METER)
# iku Event
Stand,Skill1,Skill2,Skill3, Last, Damage,Down,Item1,Item2,Item3 = range(10)

# Iku States
ationcheak = 0
class StandState:

    @staticmethod
    def enter(tenshi, event):
        global ationcheak
        tenshi.motion = 0
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.Standframe1 = [0,65,126,196,271,345]
        tenshi.Standframe2 = [65,61,70,75,74]
        ationcheak = 0
    @staticmethod
    def exit(tenshi, event):
        pass
    @staticmethod
    def do(tenshi):
        global ationcheak
        tenshi.frame1 = (tenshi.frame1 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 5
        tenshi.frame2 = (tenshi.frame2 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 5
        main_state.Enemy_Motion_Cheak = False
        if DeckSelection.character == 0 and main_state.reimu_skill1_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 0 and main_state.reimu_skill2_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 0 and  main_state.reimu_skill3_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 0 and main_state.reimu_last_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill1_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill2_atk_cheak==1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill3_atk_cheak ==1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_last_atk_cheak==1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill1_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill2_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill3_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_last_atk_cheak== 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill1_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill2_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill3_atk_cheak == 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_last_atk_cheak== 1:
            tenshi.damage_sound.play()
            tenshi.add_event(Damage)

        if main_state.HPcheak==0 and int(EnemyHP.damage) >252:
            tenshi.down_sound.play()
            tenshi.add_event(Down)
        if main_state.HPcheak == 0 and int(EnemyHP.damage) < 251:
            if ationcheak == 1: #test
                tenshi.skill1_sound.play()
                main_state.P_HP += 20 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                tenshi.add_event(Skill1)
            if ationcheak == 2: #test
                tenshi.skill2_sound.play()
                main_state.P_HP += 30 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                tenshi.add_event(Skill2)
            if ationcheak == 3: #test
                tenshi.skill3_sound.play()
                main_state.P_HP += 40 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                tenshi.add_event(Skill3)
            if ationcheak == 4: #test
                tenshi.last_sound.play()
                main_state.P_HP += 50 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                tenshi.add_event(Last)
            if ationcheak == 5: #test
                tenshi.item_sound.play()
                main_state.Enemy_DefBuff = 0
                tenshi.add_event(Item1)
            if ationcheak == 6: #test
                tenshi.item_sound.play()
                main_state.Enemy_AtkBuff = 3
                tenshi.add_event(Item2)
            if ationcheak == 7: #test
                tenshi.item_sound.play()
                main_state.HP -= 100
                EnemyHP.damage -= 100
                tenshi.add_event(Item3)



    @staticmethod
    def draw(tenshi):
        if tenshi.motion ==0:
            tenshi.stand.clip_draw(tenshi.Standframe1[int(tenshi.frame1)], 0, tenshi.Standframe2[int(tenshi.frame2)], 115, tenshi.x, tenshi.y)

class Skill1State:

    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.skill1cheak = 0
        tenshi.Skill1frame1 = [0,75,143,214,294,379,500,616,695,776,852,929,1006,1076,1146,1210]
        tenshi.Skill1frame2 = [75,67,70,77,82,120,112,73,73,73,71,68,65,63,64]
        tenshi.TenshiS1X = [0, 106, 235, 367, 509, 646, 746, 875]
        tenshi.TenshiS1Y = [107, 129, 132, 142, 135, 98, 135]
        if event == Skill1:
            tenshi.motion = 1


    @staticmethod
    def exit(tenshi, event):
        pass
        #if event ==SPACE:
        #    boy.fire_ball()
    @staticmethod
    def do(tenshi):
        main_state.Enemy_Motion_Cheak = True
        if int(tenshi.skill1cheak)<15:
            tenshi.frame1 = (tenshi.frame1 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.frame2 = (tenshi.frame2 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 15
            main_state.Skill1_Start = True
            tenshi.skill1cheak =(tenshi.skill1cheak+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time)%16
        if int(tenshi.skill1cheak)>=15:
            tenshi.skill1cheak=0
            tenshi.add_event(Stand)
            main_state.Skill1_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 1:
            tenshi.skill1.clip_draw(tenshi.Skill1frame1[int(tenshi.frame1)],0,tenshi.Skill1frame2[int(tenshi.frame2)],160, tenshi.x, tenshi.y+30)

class Skill2State:
    @staticmethod
    def enter(tenshi,event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.skill2cheak = 0
        tenshi.Skill2frame1 = [0,70,149,228,305,378,448,520,590,664,740,814,888,960,1026,1100]
        tenshi.Skill2frame2 = [70,79,79,77,73,69,68,67,70,69,66,69,66,60,60]
        if event == Skill2:
            tenshi.motion = 2

    @staticmethod
    def exit(tenshi,event):
        pass
    @staticmethod
    def do(tenshi):
        main_state.Enemy_Motion_Cheak = True
        if int(tenshi.skill2cheak) < 21:
            main_state.Skill2_Start = True
            if int(tenshi.skill2cheak) < 10:
                tenshi.frame1 = (tenshi.frame1 +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
                tenshi.frame2 = (tenshi.frame2 +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
                if int(tenshi.skill2cheak) >= 16:
                    tenshi.frame1 = (tenshi.frame1+  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
                    tenshi.frame2 = (tenshi.frame2 +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.skill2cheak = ( tenshi.skill2cheak +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%22
        if int(tenshi.skill2cheak) >= 21:
            tenshi.skill2cheak = 0
            tenshi.add_event(Stand)
            main_state.Skill2_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1


    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 2:
            tenshi.skill2.clip_draw(tenshi.Skill2frame1[int(tenshi.frame1)], 0, tenshi.Skill2frame2[int(tenshi.frame2)], 115,tenshi.x, tenshi.y)

class Skill3State:
    @staticmethod
    def enter(tenshi,event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.skill3cheak = 0
        tenshi.Skill3frame1 = [0,77,155,240,340,425,528,710,876,960,1040,1110,1190]
        tenshi.Skill3frame2 = [77,78,83,99,80,98,178,160,70,70,63,68]
        if event == Skill3:
            tenshi.motion = 3


    @staticmethod
    def exit(tenshi,event):
        pass

    @staticmethod
    def do(tenshi):
        main_state.Enemy_Motion_Cheak = True
        if int(tenshi.skill3cheak) < 16:
            if  int(tenshi.skill3cheak) < 10:
                tenshi.frame1 = (tenshi.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
                tenshi.frame2 = (tenshi.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
            if  int(tenshi.skill3cheak)>6 and  int(tenshi.skill3cheak)<14:
                main_state.Skill3_Start=True
            if  int(tenshi.skill3cheak) >= 14:
                main_state.Skill3_Start = False
                tenshi.frame1 = (tenshi.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
                tenshi.frame2 = (tenshi.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
            tenshi.skill3cheak = (tenshi.skill3cheak+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time)%17
        if  int(tenshi.skill3cheak)>= 16:
            tenshi.skill3cheak = 0
            tenshi.add_event(Stand)
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 3:
            tenshi.skill3.clip_draw(tenshi.Skill3frame1[int(tenshi.frame1)], 0, tenshi.Skill3frame2[int(tenshi.frame2)], 115,tenshi.x-200, tenshi.y)


class Laststate:
    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.lastcheak = 0
        tenshi.Lastframe1 = [0,72,142,266,435,577,715,842,928,1064,1200,1328,1430,1540,1640,1790,1965,2130,2295,2395,2465]
        tenshi.Lastframe2 = [72,70,124,169,142,137,124,85,132,131,124,96,109,95,145,167,155,150,90,72]

        if event == Last:
            tenshi.motion = 4

    @staticmethod
    def exit(tenshi, event):
        pass

    @staticmethod
    def do(tenshi):
        main_state.Enemy_Motion_Cheak = True
        if int(tenshi.lastcheak) < 20:
            tenshi.frame1 = (tenshi.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 20
            tenshi.frame2 = (tenshi.frame2 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 20
            main_state.Last_Start = True
            tenshi.lastcheak = (tenshi.lastcheak+ LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time)%21
        if int(tenshi.lastcheak) >= 20:
            tenshi.lastcheak = 0
            tenshi.add_event(Stand)
            main_state.Last_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1


    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 4:
            tenshi.Lastspell.clip_draw(tenshi.Lastframe1[int(tenshi.frame1)], 0, tenshi.Lastframe2[int(tenshi.frame2)], 165,tenshi.x-200, tenshi.y+30)

class Damagestate:
    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.Damagecheak = 0
        if event == Damage:
            tenshi.motion = 5
    @staticmethod
    def exit(tenshi, event):
        pass

    @staticmethod
    def do(tenshi):
        if int(tenshi.Damagecheak) < 5:
            tenshi.frame1 = (tenshi.frame1 + DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 5
            tenshi.Damagecheak = (tenshi.Damagecheak + DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 6
        if int(tenshi.Damagecheak) >= 5:
            tenshi.Damagecheak = 0
            tenshi.add_event(Stand)


    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 5:
            tenshi.Damage.clip_draw(int(tenshi.frame1)*80,0,78,115, tenshi.x, tenshi.y)

class Downstate:
    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.Downcheak=0
        tenshi.Downframe1 = [0,120,235,350,470,595]
        tenshi.Downframe2 = [120,115,115,120,125]

        if event == Down:
            tenshi.motion = 6


    @staticmethod
    def exit(tenshi, event):
        pass

    @staticmethod
    def do(tenshi):
        if int(tenshi.Downcheak) < 20:
            if int(tenshi.Downcheak) < 4:
                tenshi.frame1 = (tenshi.frame1 + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 5
                tenshi.frame2 = (tenshi.frame2 + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 5
            tenshi.Downcheak = (tenshi.Downcheak + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 21
        if int(tenshi.Downcheak) >= 20:
            tenshi.Downcheak = 20


        #tenshi.timer -= 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 6:
            tenshi.Down.clip_draw(tenshi.Downframe1[int(tenshi.frame1)], 0, tenshi.Downframe2[int(tenshi.frame2)], 75, tenshi.x, tenshi.y-33)
class Item_Doll:
    @staticmethod
    def enter(tenshi,event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.item1cheak = 0
        tenshi.Skill2frame1 = [0, 70, 149, 228, 305, 378, 448, 520, 590, 664, 740, 814, 888, 960, 1026, 1100]
        tenshi.Skill2frame2 = [70, 79, 79, 77, 73, 69, 68, 67, 70, 69, 66, 69, 66, 60, 60]
        if event == Item1:
            tenshi.motion = 7
    @staticmethod
    def exit(tenshi,event):
        pass
    @staticmethod
    def do(tenshi):
        global HP,HPcheak,skillcheak
        if int(tenshi.item1cheak) < 15:
            tenshi.frame1 = (tenshi.frame1 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.frame2 = (tenshi.frame2 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15

            tenshi.item1cheak = (tenshi.item1cheak+ ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time)%16
        if int(tenshi.item1cheak) >= 15:
            tenshi.item1cheak = 0
            tenshi.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 7:
            tenshi.item_use.clip_draw(0, 0, 40, 65, 600, 280)
            tenshi.skill2.clip_draw(tenshi.Skill2frame1[int(tenshi.frame1)], 0,tenshi.Skill2frame2[int(tenshi.frame2)], 115, tenshi.x, tenshi.y)
class Item_Potion:
    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.item1cheak = 0
        tenshi.Skill2frame1 = [0, 70, 149, 228, 305, 378, 448, 520, 590, 664, 740, 814, 888, 960, 1026, 1100]
        tenshi.Skill2frame2 = [70, 79, 79, 77, 73, 69, 68, 67, 70, 69, 66, 69, 66, 60, 60]
        if event == Item2:
            tenshi.motion = 8

    @staticmethod
    def exit(tenshi, event):
        pass

    @staticmethod
    def do(tenshi):
        global HP, HPcheak, skillcheak
        if int(tenshi.item1cheak) < 15:
            tenshi.frame1 = (tenshi.frame1 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.frame2 = (tenshi.frame2 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15

            tenshi.item1cheak = (tenshi.item1cheak + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 16
        if int(tenshi.item1cheak) >= 15:
            tenshi.item1cheak = 0
            tenshi.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 8:
            tenshi.item_use.clip_draw(40, 0, 40, 65, 600, 280)
            tenshi.skill2.clip_draw(tenshi.Skill2frame1[int(tenshi.frame1)], 0,tenshi.Skill2frame2[int(tenshi.frame2)], 115, tenshi.x, tenshi.y)

class Item_Clock:
    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.item1cheak = 0
        tenshi.Skill2frame1 = [0, 70, 149, 228, 305, 378, 448, 520, 590, 664, 740, 814, 888, 960, 1026, 1100]
        tenshi.Skill2frame2 = [70, 79, 79, 77, 73, 69, 68, 67, 70, 69, 66, 69, 66, 60, 60]
        if event == Item3:
            tenshi.motion = 9

    @staticmethod
    def exit(tenshi, event):
        pass

    @staticmethod
    def do(tenshi):
        global HP, HPcheak, skillcheak
        if int(tenshi.item1cheak) < 15:
            tenshi.frame1 = (tenshi.frame1 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.frame2 = (tenshi.frame2 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15

            tenshi.item1cheak = (tenshi.item1cheak + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 16
        if int(tenshi.item1cheak) >= 15:
            tenshi.item1cheak = 0
            tenshi.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 9:
            tenshi.item_use.clip_draw(80, 0, 40, 65, 600, 280)
            tenshi.skill2.clip_draw(tenshi.Skill2frame1[int(tenshi.frame1)], 0,tenshi.Skill2frame2[int(tenshi.frame2)], 115, tenshi.x, tenshi.y)
next_state_table = {
    StandState: {Skill1: Skill1State, Skill2: Skill2State, Skill3:Skill3State,Last:Laststate, Damage:Damagestate,Down:Downstate,Item1:Item_Doll,Item2:Item_Potion,Item3:Item_Clock},
    Skill1State: {Skill1: StandState,  Stand:StandState},
    Skill2State: {Skill2: StandState, Stand:StandState},
    Skill3State: {Skill3: StandState ,Stand: StandState},
    Laststate: {Last:StandState,Stand: StandState},
    Damagestate: {Damage:StandState, Stand:StandState,Down:Downstate},
    Downstate: {Down:StandState,Stand:StandState,Damage:StandState},
    Item_Doll:{Item1:StandState, Stand:StandState},
Item_Potion:{Item2:StandState, Stand:StandState},
Item_Clock:{Item3:StandState, Stand:StandState}

}

class Enemy_Tenshi:

    def __init__(self):
        self.x, self.y = 600, 200
        self.stand = load_image('TenshiStanding-Motion.png')

        self.skill1 = load_image('TenshiSkill1-Motion.png')

        self.skill2 = load_image('TenshiSkill2-Motion.png')

        self.skill3 = load_image('TenshiSkill3-Motion.png')


        self.Lastspell = load_image('TenshiLastspell-Motion.png')


        self.Damage = load_image('TenshiDamage-Motion.png')

        self.Down = load_image('TenshiDown-Motion.png')
        self.skill1_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-skill1.wav')
        self.skill1_sound.set_volume(50)
        self.skill2_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-skill2.wav')
        self.skill2_sound.set_volume(50)
        self.skill3_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-skill3.wav')
        self.skill3_sound.set_volume(50)
        self.last_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-Last.wav')
        self.last_sound.set_volume(50)
        self.damage_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-damage.wav')
        self.damage_sound.set_volume(30)
        self.down_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-down.wav')
        self.down_sound.set_volume(70)
        self.item_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\tenshi-item.wav')
        self.item_sound.set_volume(50)
        self.item_use = load_image('commonCard.png')
        self.dir = 1
        self.motion = 0
        self.frame = 0
        self.timer = 0
        self.build_behavior_tree()
        self.event_que = []
        self.cur_state = StandState
        self.cur_state.enter(self, None)
    def turn_cheak(self):
        if main_state.turn == -1:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def action_cheak(self):
        global ationcheak
        if ationcheak ==0:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def finish_atk_cheak(self):
        global ationcheak
        if PlayerHP.damage >=212:
            ationcheak=3
            return BehaviorTree.SUCCESS
        else:
            return  BehaviorTree.FAIL
    def buff_ready_cheak(self):
        global ationcheak
        if main_state.Enemy_DefBuff==0 or main_state.Enemy_AtkBuff==3:
            ationcheak= random.randint(1,4)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def atk_cheak(self):
        global ationcheak
        if main_state.Enemy_DefBuff == 1 and main_state.Enemy_AtkBuff == 1:
            ationcheak = random.randint(1, 7)
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def enemy_atk_buff_cheak(self):
        if main_state.Enemy_AtkBuff ==3:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def player_atk_buff_cheak(self):
        global ationcheak
        if main_state.Player_AtkBuff==3:
            success_cheak=random.randint(1,100)
            if success_cheak>75:
                ationcheak=5
                return BehaviorTree.SUCCESS
            else:
                ationcheak=random.randint(1, 7)
                return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL
    def enemy_HP_cheak(self):
        global ationcheak
        if EnemyHP.damage>200:
            success_cheak = random.randint(1, 100)
            if success_cheak>50:
                ationcheak=7
                return BehaviorTree.SUCCESS
            else:
                ationcheak=random.randint(1, 7)
                return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.FAIL


    def Hard_finish_atk_cheak(self):
        global ationcheak
        if PlayerHP.damage >=102:
            ationcheak=4
            return BehaviorTree.SUCCESS
        else:
            return  BehaviorTree.FAIL



    def build_behavior_tree(self):
        turn_cheak_node = LeafNode("Turn Cheak", self.turn_cheak)
        action_cheak_node = LeafNode("Action Stand", self.action_cheak)
        finish_atk_cheak_node = LeafNode("Finish_Atk", self.finish_atk_cheak)
        buff_ready_cheak_node = LeafNode("Buff Ready Cheak", self.buff_ready_cheak)
        atk_cheak_node = LeafNode("Atk", self.atk_cheak)
        ##Hard
        enemy_atk_buff_cheak_node =  LeafNode("Atk_Buff_Cheak", self.enemy_atk_buff_cheak)
        Hard_finish_atk_cheak_node = LeafNode("Finish_Atk", self.Hard_finish_atk_cheak)
        player_atk_buff_cheak_node = LeafNode("Player_Buff_Cheak", self.player_atk_buff_cheak)
        enemy_hp_cheak_node = LeafNode("Enemy_HP_Cheak", self.enemy_HP_cheak)

        ##Nomal
        Finsh_node = SequenceNode("Finish")
        Finsh_node.add_children(turn_cheak_node, action_cheak_node,finish_atk_cheak_node)
        Buff_Atk_node =SequenceNode("BuffAtk")
        Buff_Atk_node.add_children(turn_cheak_node,action_cheak_node,buff_ready_cheak_node)
        Atk_node = SequenceNode("Atk")
        Atk_node.add_children(turn_cheak_node, action_cheak_node,atk_cheak_node)
        action_chase_node = SelectorNode("ActionChase")
        action_chase_node.add_children(Finsh_node, Buff_Atk_node,Atk_node)
        ##Hard
        Hard_Finsh_node = SequenceNode("Hard-Finish")
        Hard_Finsh_node.add_children(turn_cheak_node,action_cheak_node, enemy_atk_buff_cheak_node, Hard_finish_atk_cheak_node)
        Hard_Block_node = SequenceNode("Hard-Block")
        Hard_Block_node.add_children(turn_cheak_node, action_cheak_node,player_atk_buff_cheak_node)
        Hard_HP_node = SequenceNode("Hard-Block")
        Hard_HP_node.add_children(turn_cheak_node, action_cheak_node, enemy_hp_cheak_node)
        Hard_action_chase_node = SelectorNode("Hard_ActionChase")
        Hard_action_chase_node.add_children(Hard_Finsh_node, Hard_Block_node, Hard_HP_node,Buff_Atk_node,Atk_node)
        if BackgroundSelection.Level_cheak==1:
            self.ation = BehaviorTree(action_chase_node)
        if BackgroundSelection.Level_cheak == 2:
            self.ation = BehaviorTree(Hard_action_chase_node)





    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.ation.run()
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        pass
