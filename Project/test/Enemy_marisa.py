from pico2d import *
import game_framework
import EnemyHP
import main_state
import random
import DeckSelection
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import BackgroundSelection
import PlayerHP
import game_world

#marisa stand
STAND_TIME_PER_ACTION=1
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
STAND_PER_ACTION=9

#skill1
SKILL1TIME_PER_ACTION=2
SKILL1ACTION_PER_TIME= 1.0/SKILL1TIME_PER_ACTION
SKILL1_PER_ACTION=20

#skill2
SKILL2TIME_PER_ACTION=1
SKILL2ACTION_PER_TIME= 1.0/SKILL2TIME_PER_ACTION
SKILL2_PER_ACTION=9

#skill3
SKILL3TIME_PER_ACTION=2
SKILL3ACTION_PER_TIME= 1.0/SKILL3TIME_PER_ACTION
SKILL3_PER_ACTION=20
# iku lastspell Action Speed
LASTTIME_PER_ACTION=2
LASTACTION_PER_TIME= 1.0/LASTTIME_PER_ACTION
LASTCHEAK_PER_ACTION=20
#Damage
DAMAGETIME_PER_ACTION=1
DAMAGEACTION_PER_TIME= 1.0/DAMAGETIME_PER_ACTION
DAMAGE_PER_ACTION=4

#Down
DOWNTIME_PER_ACTION=3
DOWNACTION_PER_TIME= 1.0/DOWNTIME_PER_ACTION
DOWN_PER_ACTION=21

#itemuse
ITEM1TIME_PER_ACTION=1
ITEM1ACTION_PER_TIME= 1.0/ITEM1TIME_PER_ACTION
ITEM1_PER_ACTION=10

#motion speed
PIXEL_PER_METER=(10.0/0.3)
MOTION_SPEED_KMPH = 0.2
MOTION_SPEED_MPM = (MOTION_SPEED_KMPH*1000.0/60.0)
MOTION_SPEED_MPS=(MOTION_SPEED_MPM/60.0)
MOTION_SPEED_PPS=(MOTION_SPEED_MPS*PIXEL_PER_METER)
# marisa Event
Stand,Skill1,Skill2,Skill3, Last, Damage,Down,Item1,Item2,Item3 = range(10)


# marisa States
ationcheak = 0
class StandState:

    @staticmethod
    def enter(marisa, event):
        global ationcheak
        marisa.motion = 0
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
        marisa.Standframe2 = [65,61,62,62,62,60,62,61,60,62]
        ationcheak=0

    @staticmethod
    def exit(marisa, event):
        pass
    @staticmethod
    def do(marisa):
        global ationcheak
        marisa.frame1 = (marisa.frame1 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 9
        marisa.frame2 = (marisa.frame2 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 9
        main_state.Enemy_Motion_Cheak = False
        if DeckSelection.character == 0 and main_state.reimu_skill1_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 0 and main_state.reimu_skill2_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 0 and  main_state.reimu_skill3_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 0 and main_state.reimu_last_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill1_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill2_atk_cheak==1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill3_atk_cheak ==1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_last_atk_cheak==1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill1_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill2_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill3_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_last_atk_cheak== 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill1_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill2_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill3_atk_cheak == 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_last_atk_cheak== 1:
            marisa.damage_sound.play()
            marisa.add_event(Damage)

        if main_state.HPcheak==0 and int(EnemyHP.damage) >252:
            marisa.down_sound.play()
            marisa.add_event(Down)
        if main_state.HPcheak == 0 and int(EnemyHP.damage) < 251:
            if ationcheak == 1: #test
                marisa.skill1_sound.play()
                main_state.P_HP += 20 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                marisa.add_event(Skill1)
            if ationcheak == 2: #test
                marisa.skill2_sound.play()
                main_state.P_HP += 30 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                marisa.add_event(Skill2)
            if ationcheak == 3: #test
                marisa.skill3_sound.play()
                main_state.P_HP += 40 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                marisa.add_event(Skill3)
            if ationcheak == 4: #test
                marisa.last_sound.play()
                main_state.P_HP += 50 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                marisa.add_event(Last)
            if ationcheak == 5: #test
                marisa.item_sound.play()
                main_state.Enemy_DefBuff = 0
                marisa.add_event(Item1)
            if ationcheak == 6: #test
                marisa.item_sound.play()
                main_state.Enemy_AtkBuff = 3
                marisa.add_event(Item2)
            if ationcheak == 7: #test
                marisa.item_sound.play()
                main_state.HP -= 100
                EnemyHP.damage -= 100
                marisa.add_event(Item3)




    @staticmethod
    def draw(marisa):
        if marisa.motion ==0:
            marisa.stand.clip_draw(marisa.Standframe1[int(marisa.frame1)], 0, marisa.Standframe2[int(marisa.frame2)], 110, marisa.x, marisa.y)

class Skill1State:

    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.skill1cheak = 0
        marisa.Skill1frame1 = [0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        marisa.Skill1frame2 = [71, 61, 65, 65, 58, 72, 72, 66, 60]
        if event == Skill1:
            marisa.motion = 1


    @staticmethod
    def exit(marisa, event):
        pass

    @staticmethod
    def do(marisa):
        main_state.Enemy_Motion_Cheak = True
        if int(marisa.skill1cheak) < 6:
            marisa.frame1 = (marisa.frame1 +SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 9
            marisa.frame2 = (marisa.frame2 +SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 9
        if int(marisa.skill1cheak) >6:
            if marisa.skill1cheak < 15:
                main_state.Skill1_Start = True
            if int(marisa.skill1cheak) >= 15:
                main_state.Skill1_Start = False
                marisa.frame1 = (marisa.frame1+SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 10
                marisa.frame2 = (marisa.frame2 +SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 9

        marisa.skill1cheak =(marisa.skill1cheak+SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time)%20
        if int(marisa.skill1cheak)>=18:
            marisa.skill1cheak=0
            marisa.add_event(Stand)
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1



    @staticmethod
    def draw(marisa):
        if marisa.motion == 1:
            marisa.skill1.clip_draw(marisa.Skill1frame1[int(marisa.frame1)], 0, marisa.Skill1frame2[int(marisa.frame2)], 105, marisa.x, marisa.y)


class Skill2State:
    @staticmethod
    def enter(marisa,event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.skill2cheak = 0
        marisa.Skill2frame1 =  [0, 85, 165, 240, 318, 395, 464, 525]
        marisa.Skill2frame2 = [85, 80, 75, 78, 76, 67, 64]
        if event == Skill2:
            marisa.motion = 2

    @staticmethod
    def exit(marisa,event):
        pass
    @staticmethod
    def do(marisa):
        main_state.Enemy_Motion_Cheak = True
        if int(marisa.skill2cheak) < 7:
            marisa.frame1 = (marisa.frame1  +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 7
            marisa.frame2 = (marisa.frame2  +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 7
            main_state.Skill2_Start = True
            marisa.skill2cheak = (marisa.skill2cheak+  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%9
        if int(marisa.skill2cheak) >= 7:
            marisa.skill2cheak = 0
            marisa.add_event(Stand)
            main_state.Skill2_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1



    @staticmethod
    def draw(marisa):
        if marisa.motion == 2:
            marisa.skill2.clip_draw(marisa.Skill2frame1[int(marisa.frame1)], 0, marisa.Skill2frame2[int(marisa.frame2)], 120,marisa.x, marisa.y)

class Skill3State:
    @staticmethod
    def enter(marisa,event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.skill3cheak = 0
        marisa.Skill3frame1 = [0, 65, 125, 195, 275, 332, 412, 500, 590, 661]
        marisa.Skill3frame2 = [65, 60, 70, 80, 60, 76, 85, 89, 68, 61]
        if event == Skill3:
            marisa.motion = 3


    @staticmethod
    def exit(marisa,event):
        pass

    @staticmethod
    def do(marisa):
        main_state.Enemy_Motion_Cheak = True
        if int(marisa.skill3cheak) < 17:
            if int(marisa.skill3cheak) < 7:
                marisa.frame1 = (marisa.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
                marisa.frame2 = (marisa.frame2+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
            if int(marisa.skill3cheak) >= 7:
                main_state.Skill3_Start=True
            if int(marisa.skill3cheak) >= 13:
                    marisa.frame1 = (marisa.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
                    marisa.frame2 = (marisa.frame2+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
            marisa.skill3cheak = (marisa.skill3cheak+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time)%20
        if int(marisa.skill3cheak) >= 17:
            marisa.skill3cheak = 0
            marisa.add_event(Stand)
            main_state.Skill3_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(marisa):
        if marisa.motion == 3:
            marisa.skill3.clip_draw(marisa.Skill3frame1[int(marisa.frame1)], 0, marisa.Skill3frame2[int(marisa.frame2)], 110,marisa.x, marisa.y)

class Laststate:
    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.lastframe = 0
        marisa.lastEframe1 = 0
        marisa.lastcheak = 0
        marisa.LastspellEframe1 = 0
        marisa.Lastspellframe1 = 0
        marisa.Lastspellframe2 = 0
        marisa.Lastspellframe3 = 0
        marisa.Lastspellc = 0
        marisa.Lastspelld = 0
        marisa.Lastframe1 = [0, 65,127,187,251,305,386,451,536,610,680,750,815,880,943,1010,1070]
        marisa.Lastframe2 = [65,62,60,64,55,79,62,80,72,66,66,65,63,60,59,58,58]

        if event == Last:
            marisa.motion = 4

    @staticmethod
    def exit(marisa, event):
        pass

    @staticmethod
    def do(marisa):
        main_state.Enemy_Motion_Cheak = True
        if int(marisa.lastcheak) < 18:
            marisa.frame1 = (marisa.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 17
            marisa.frame2 = (marisa.frame2+ LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 17
            if int(marisa.lastcheak) > 4 and int(marisa.lastcheak)<11:
                main_state.Last_Start = True

            marisa.lastcheak = (marisa.lastcheak+ LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time)%20
        if int(marisa.lastcheak) >= 18:
            marisa.lastcheak = 0
            marisa.add_event(Stand)
            main_state.Last_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1



    @staticmethod
    def draw(marisa):
        if marisa.motion == 4:
            marisa.Lastspell.clip_draw(marisa.Lastframe1[int(marisa.frame1)], 0, marisa.Lastframe2[int(marisa.frame2)], 120,marisa.x-250, marisa.y)

class Damagestate:
    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.Damagecheak = 0
        marisa.Damageframe = 0
        marisa.Damageframe1 = [0, 90, 175, 240]
        marisa.Damageframe2 = [90, 85, 65]
        if event == Damage:
            marisa.motion = 5
    @staticmethod
    def exit(marisa, event):
        pass

    @staticmethod
    def do(marisa):
        if int(marisa.Damagecheak) < 3:
            marisa.frame1 = (marisa.frame1 + DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 3
            marisa.frame2 = (marisa.frame2 + DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 3
            marisa.Damagecheak = (marisa.Damagecheak+ DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time)%4
        if int(marisa.Damagecheak) >= 3:
            marisa.Damagecheak = 0
            marisa.add_event(Stand)




    @staticmethod
    def draw(marisa):
        if marisa.motion == 5:
            marisa.Damage.clip_draw(marisa.Damageframe1[int(marisa.frame1)],0,marisa.Damageframe2[int(marisa.frame2)],115, marisa.x, marisa.y)

class Downstate:
    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.Downcheak=0
        marisa.Downframe1 = [0,80,149,232,348,451,548,645]
        marisa.Downframe2 = [80,69,83,116,102,95,100]

        if event == Down:
            marisa.motion = 6


    @staticmethod
    def exit(marisa, event):
        pass

    @staticmethod
    def do(marisa):
        if int(marisa.Downcheak) < 20:
            if int(marisa.Downcheak) < 6:
                marisa.frame1 = (marisa.frame1 + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 7
                marisa.frame2 = (marisa.frame2 + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 7
            marisa.Downcheak = (marisa.Downcheak+ DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time)
        if int(marisa.Downcheak) >= 20:
            marisa.Downcheak=20


        #marisa.timer -= 1

    @staticmethod
    def draw(marisa):
        if marisa.motion == 6:
            marisa.Down.clip_draw(marisa.Downframe1[int(marisa.frame1)], 0, marisa.Downframe2[int(marisa.frame2)], 95, marisa.x, marisa.y-20)
class Item_Doll:
    @staticmethod
    def enter(marisa,event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.item1cheak = 0
        marisa.Skill1frame1 = [0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        marisa.Skill1frame2 = [71, 61, 65, 65, 58, 72, 72, 66, 60]
        if event == Item1:
            marisa.motion = 7
    @staticmethod
    def exit(marisa,event):
        pass
    @staticmethod
    def do(marisa):
        global HP,HPcheak,skillcheak
        if int(marisa.item1cheak) < 9:
            marisa.frame1 = (marisa.frame1 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9
            marisa.frame2 = (marisa.frame2 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9

            marisa.item1cheak = (marisa.item1cheak+ ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time)%10
        if int(marisa.item1cheak) >= 9:
            marisa.item1cheak = 0
            marisa.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(marisa):
        if marisa.motion == 7:
            marisa.item_use.clip_draw(0, 0, 40, 65, 600, 280)
            marisa.skill1.clip_draw(marisa.Skill1frame1[int(marisa.frame1)], 0,marisa.Skill1frame2[int(marisa.frame2)], 105, marisa.x, marisa.y)
class Item_Potion:
    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.item1cheak = 0
        marisa.Skill1frame1 = [0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        marisa.Skill1frame2 = [71, 61, 65, 65, 58, 72, 72, 66, 60]
        if event == Item2:
            marisa.motion = 8

    @staticmethod
    def exit(marisa, event):
        pass

    @staticmethod
    def do(marisa):
        global HP, HPcheak, skillcheak
        if int(marisa.item1cheak) < 9:
            marisa.frame1 = (marisa.frame1 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9
            marisa.frame2 = (marisa.frame2 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9

            marisa.item1cheak = (marisa.item1cheak + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 10
        if int(marisa.item1cheak) >= 9:
            marisa.item1cheak = 0
            marisa.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(marisa):
        if marisa.motion == 8:
            marisa.item_use.clip_draw(40, 0, 40, 65, 600, 280)
            marisa.skill1.clip_draw(marisa.Skill1frame1[int(marisa.frame1)], 0,marisa.Skill1frame2[int(marisa.frame2)], 105, marisa.x, marisa.y)

class Item_Clock:
    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.item1cheak = 0
        marisa.Skill1frame1 = [0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        marisa.Skill1frame2 = [71, 61, 65, 65, 58, 72, 72, 66, 60]
        if event == Item3:
            marisa.motion = 9

    @staticmethod
    def exit(marisa, event):
        pass

    @staticmethod
    def do(marisa):
        global HP, HPcheak, skillcheak
        if int(marisa.item1cheak) < 9:
            marisa.frame1 = (marisa.frame1 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9
            marisa.frame2 = (marisa.frame2 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9

            marisa.item1cheak = (marisa.item1cheak + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 10
        if int(marisa.item1cheak) >= 9:
            marisa.item1cheak = 0
            marisa.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(marisa):
        if marisa.motion == 9:
            marisa.item_use.clip_draw(80, 0, 40, 65, 600, 280)
            marisa.skill1.clip_draw(marisa.Skill1frame1[int(marisa.frame1)], 0,marisa.Skill1frame2[int(marisa.frame2)], 105, marisa.x, marisa.y)
next_state_table = {
    StandState: {Skill1: Skill1State, Skill2: Skill2State, Skill3:Skill3State,Last:Laststate, Damage:Damagestate,Down:Downstate,Item1:Item_Doll,Item2:Item_Potion,Item3:Item_Clock},
    Skill1State: {Skill1: StandState,  Stand:StandState},
    Skill2State: {Skill2: StandState, Stand:StandState},
    Skill3State: {Skill3: StandState ,Stand: StandState},
    Laststate: {Last:StandState,Stand: StandState,Down:Downstate},
    Damagestate: {Damage:StandState, Stand:StandState,Down:Downstate},
    Downstate: {Down:StandState,Stand:StandState,Damage:StandState},
    Item_Doll:{Item1:StandState, Stand:StandState},
Item_Potion:{Item2:StandState, Stand:StandState},
Item_Clock:{Item3:StandState, Stand:StandState}

}


class Enemy_Marisa:

    def __init__(self):
        self.x, self.y = 600, 200
        self.stand = load_image('./FCGimage/MarisaStanding-Motion.png')

        self.skill1 = load_image('./FCGimage/MarisaSkill1-Motion.png')

        self.skill2 = load_image('./FCGimage/MarisaSkill2-Motion.png')

        self.skill3 = load_image('./FCGimage/MarisaSkill3-Motion.png')

        self.Lastspell = load_image('./FCGimage/MarisaLastspell-Motion.png')

        self.Damage = load_image('./FCGimage/MarisaDamage-Motion.png')

        self.Down = load_image('./FCGimage/MarisaDown-Motion.png')

        self.skill1_sound = load_wav('./voice/marisa-skill1.wav')
        self.skill1_sound.set_volume(50)
        self.skill2_sound = load_wav('./voice/marisa-skill2.wav')
        self.skill2_sound.set_volume(50)
        self.skill3_sound = load_wav('./voice/marisa-skill3.wav')
        self.skill3_sound.set_volume(50)
        self.last_sound = load_wav('./voice/marisa-Last.wav')
        self.last_sound.set_volume(50)
        self.damage_sound = load_wav('./voice/marisa-damage.wav')
        self.damage_sound.set_volume(30)
        self.down_sound = load_wav('./voice/marisa-down.wav')
        self.down_sound.set_volume(70)
        self.item_sound = load_wav('./voice/marisa-item.wav')
        self.item_sound.set_volume(50)
        self.item_use = load_image('./FCGimage/commonCard.png')
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
