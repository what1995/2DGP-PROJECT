from pico2d import *
import main_state
import game_world
import game_framework
import EnemyHP
import random
import DeckSelection
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
import BackgroundSelection
import PlayerHP
#reimu stand
STAND_TIME_PER_ACTION=1.2
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
STAND_PER_ACTION=12

#skill1
SKILL1TIME_PER_ACTION=1.5
SKILL1ACTION_PER_TIME= 1.0/SKILL1TIME_PER_ACTION
SKILL1_PER_ACTION=15

#skill2
SKILL2TIME_PER_ACTION=1
SKILL2ACTION_PER_TIME= 0.8/SKILL2TIME_PER_ACTION
SKILL2_PER_ACTION=13

#skill3
SKILL3TIME_PER_ACTION=2
SKILL3ACTION_PER_TIME= 1.0/SKILL3TIME_PER_ACTION
SKILL3_PER_ACTION=25
# iku lastspell Action Speed
LASTTIME_PER_ACTION=2
LASTACTION_PER_TIME= 1.0/LASTTIME_PER_ACTION
LASTCHEAK_PER_ACTION=23
#Damage
DAMAGETIME_PER_ACTION=1
DAMAGEACTION_PER_TIME= 1.0/DAMAGETIME_PER_ACTION
DAMAGE_PER_ACTION=4

#Down
DOWNTIME_PER_ACTION=3
DOWNACTION_PER_TIME= 1.0/DOWNTIME_PER_ACTION
DOWN_PER_ACTION=21
#item use
ITEM1TIME_PER_ACTION=1
ITEM1ACTION_PER_TIME= 0.8/ITEM1TIME_PER_ACTION
ITEM1_PER_ACTION=9
#motion speed
PIXEL_PER_METER=(10.0/0.3)
MOTION_SPEED_KMPH = 0.2
MOTION_SPEED_MPM = (MOTION_SPEED_KMPH*1000.0/60.0)
MOTION_SPEED_MPS=(MOTION_SPEED_MPM/60.0)
MOTION_SPEED_PPS=(MOTION_SPEED_MPS*PIXEL_PER_METER)
# reimuEvent
Stand,Skill1,Skill2,Skill3, Last, Damage,Down,Item1,Item2,Item3 = range(10)


# Reimu States
ationcheak = 0
class StandState:

    @staticmethod
    def enter(reimu, event):
        global ationcheak
        reimu.motion = 0
        reimu.frame1 = 0
        reimu.frame2 = 0
        ationcheak = 0



    @staticmethod
    def exit(reimu, event):
        pass
    @staticmethod
    def do(reimu):
        global ationcheak
        reimu.frame1 = (reimu.frame1+ STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 11
        main_state.Enemy_Motion_Cheak = False
        if DeckSelection.character == 0 and main_state.reimu_skill1_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 0 and main_state.reimu_skill2_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 0 and  main_state.reimu_skill3_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 0 and main_state.reimu_last_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill1_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill2_atk_cheak==1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_skill3_atk_cheak ==1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 1 and main_state.marisa_last_atk_cheak==1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill1_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill2_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_skill3_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 2 and main_state.iku_last_atk_cheak== 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill1_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill2_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_skill3_atk_cheak == 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)
        if DeckSelection.character == 3 and main_state.tenshi_last_atk_cheak== 1:
            reimu.damage_sound.play()
            reimu.add_event(Damage)

        if main_state.HPcheak==0 and int(EnemyHP.damage) >252:
            reimu.down_sound.play()
            reimu.add_event(Down)
        if main_state.HPcheak == 0and int(EnemyHP.damage) < 251:
            if ationcheak == 1: #test
                reimu.skill1_sound.play()
                main_state.P_HP += 20 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                reimu.add_event(Skill1)
            if ationcheak == 2: #test
                reimu.skill2_sound.play()
                main_state.P_HP += 30 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                reimu.add_event(Skill2)
            if ationcheak == 3: #test
                reimu.skill3_sound.play()
                main_state.P_HP += 40 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                reimu.add_event(Skill3)
            if ationcheak == 4: #test
                reimu.last_sound.play()
                main_state.P_HP += 50 * main_state.Enemy_AtkBuff * main_state.Player_DefBuff
                reimu.add_event(Last)
            if ationcheak == 5: #test
                reimu.item_sound.play()
                main_state.Enemy_DefBuff = 0
                reimu.add_event(Item1)
            if ationcheak == 6: #test
                reimu.item_sound.play()
                main_state.Enemy_AtkBuff = 3
                reimu.add_event(Item2)
            if ationcheak == 7: #test
                reimu.item_sound.play()
                main_state.HP -= 100
                EnemyHP.damage -= 100
                reimu.add_event(Item3)




    @staticmethod
    def draw(reimu):
        if reimu.motion ==0:
            reimu.stand.clip_draw(int(reimu.frame1) *100,0,97,105, reimu.x, reimu.y)

class Skill1State:

    @staticmethod
    def enter(reimu, event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.skill1cheak = 0
        reimu.Skill1frame1 = [0,108,213,327,434,541,638,787,936,1080,1215,1319,1425]
        reimu.Skill1frame2 = [108,105,114,107,107,97,149,149,144,135,104,106]
        if event == Skill1:
            reimu.motion = 1


    @staticmethod
    def exit(reimu, event):
        pass
        #if event ==SPACE:
        #    boy.fire_ball()
    @staticmethod
    def do(reimu):
        main_state.Enemy_Motion_Cheak = True
        if int(reimu.skill1cheak)<14:
            reimu.frame1 = (reimu.frame1+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 12
            reimu.frame2 = (reimu.frame2+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 12
        if int(reimu.skill1cheak) > 3:
            main_state.Skill1_Start=True
        reimu.skill1cheak =(reimu.skill1cheak+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time)%15
        if  int(reimu.skill1cheak)>=13:
            reimu.skill1cheak=0
            reimu.add_event(Stand)
            main_state.Skill1_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(reimu):
        if reimu.motion == 1:
            reimu.skill1.clip_draw(reimu.Skill1frame1[int(reimu.frame1)], 0, reimu.Skill1frame2[int(reimu.frame2)], 110, reimu.x, reimu.y)

class Skill2State:
    @staticmethod
    def enter(reimu,event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.skill2cheak = 0
        reimu.Skill2frame1 = [0,66,120,217,304,392,480,572,675]
        reimu.Skill2frame2 = [66,54,97,87,88,88,92,103]
        if event == Skill2:
            reimu.motion = 2

    @staticmethod
    def exit(reimu,event):
        pass
    @staticmethod
    def do(reimu):
        main_state.Enemy_Motion_Cheak = True
        if int(reimu.skill2cheak) < 8:
            reimu.frame1 = (reimu.frame1+  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 8
            reimu.frame2 = (reimu.frame2+  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 8
            main_state.Skill2_Start = True
        if int(reimu.skill2cheak) > 8:
            main_state.Skill2_Start = False
        reimu.skill2cheak = (reimu.skill2cheak+  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%13
        if int(reimu.skill2cheak) >= 12:
            reimu.skill2cheak = 0
            reimu.add_event(Stand)
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1


    @staticmethod
    def draw(reimu):
        if reimu.motion == 2:
            reimu.skill2.clip_draw(reimu.Skill2frame1[int(reimu.frame1)],0, reimu.Skill2frame2[int(reimu.frame2)],120,reimu.x, reimu.y)

class Skill3State:
    @staticmethod
    def enter(reimu,event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.skill3cheak = 0
        reimu.Skill3frame1 = [0,105, 210,315,420, 543, 659, 775, 885, 1000,1100]
        reimu.Skill3frame2 = [104,105,105,104,120,115,115,108,115,100]
        if event == Skill3:
            reimu.motion = 3


    @staticmethod
    def exit(reimu,event):
        pass

    @staticmethod
    def do(reimu):
        main_state.Enemy_Motion_Cheak = True
        if int(reimu.skill3cheak) < 24:
            if int(reimu.skill3cheak) < 5:
                reimu.frame1 = (reimu.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
                reimu.frame2 = (reimu.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
            if int(reimu.skill3cheak) >= 5:
                main_state.Skill3_Start = True
                if int(reimu.skill3cheak) > 20:
                    reimu.frame1 = (reimu.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 11
                    reimu.frame2 = (reimu.frame2+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 10
            reimu.skill3cheak = (reimu.skill3cheak+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time)%25
        if int(reimu.skill3cheak) >= 24:
            reimu.skill3cheak = 0
            reimu.add_event(Stand)
            main_state.Skill3_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(reimu):
        if reimu.motion == 3:
            reimu.skill3.clip_draw(reimu.Skill3frame1[int(reimu.frame1)],0,reimu.Skill3frame2[int(reimu.frame2)],100,reimu.x, reimu.y)

class Laststate:
    @staticmethod
    def enter(reimu, event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.lastframe = 0
        reimu.lastEframe1 = 0
        reimu.lastcheak = 0
        reimu.LastspellEframe1 = 0
        reimu.Lastspellframe1 = 0
        reimu.Lastspellframe2 = 0
        reimu.Lastspellframe3 = 0
        reimu.Lastspellc = 0
        reimu.Lastspelld = 0
        reimu.ReimuLastX = [180, 220, 200]
        reimu.ReimuLastY = [160.175, 200, 225, 250]
        reimu.Lastframe1 = [0,105, 209,311,414, 517, 620, 724, 822, 910, 995,1068,1145,1242,1345,1445]
        reimu.Lastframe2 = [105,104,102,103,104,103,104,98,88,85,74,77,97,103,100]

        if event == Last:
            reimu.motion = 4

    @staticmethod
    def exit(reimu, event):
        pass

    @staticmethod
    def do(reimu):
        main_state.Enemy_Motion_Cheak = True
        if int(reimu.lastcheak) < 22:
            if int(reimu.lastcheak) < 9:
                reimu.frame1 = (reimu.frame1  + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 15
                reimu.frame2 = (reimu.frame2  + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 15
            if int(reimu.lastcheak) >= 16:
                reimu.frame1 = (reimu.frame1  + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 15
                reimu.frame2 = (reimu.frame2  + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 15
            main_state.Last_Start = True
            reimu.lastcheak = (reimu.lastcheak + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time)%23
        if int(reimu.lastcheak) >= 22:
            reimu.lastcheak = 0
            reimu.add_event(Stand)
            main_state.Last_Start = False
            main_state.Enemy_AtkBuff = 1
            main_state.Player_DefBuff = 1
            main_state.turn = 1
            main_state.DeckShow = 1


    @staticmethod
    def draw(reimu):
        if reimu.motion == 4:
            reimu.Lastspell.clip_draw(reimu.Lastframe1[int(reimu.frame1)], 0, reimu.Lastframe2[int(reimu.frame2)], 130,reimu.x, reimu.y+15)


class Damagestate:
    @staticmethod
    def enter(reimu, event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.Damagecheak = 0
        reimu.Damageframe = 0
        if event == Damage:
            reimu.motion = 5
    @staticmethod
    def exit(reimu, event):
        pass

    @staticmethod
    def do(reimu):
        if int(reimu.Damagecheak) < 3:
            reimu.Damageframe = (reimu.Damageframe + DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 3
            reimu.Damagecheak = (reimu.Damagecheak+ DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time)%4
        if int(reimu.Damagecheak) >= 3:
            reimu.Damagecheak = 0
            reimu.add_event(Stand)



    @staticmethod
    def draw(reimu):
        if reimu.motion == 5:
            reimu.Damage.clip_draw(int(reimu.Damageframe)*112,0,110,90, reimu.x, reimu.y)

class Downstate:
    @staticmethod
    def enter(reimu, event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.Downcheak=0
        reimu.Downframe1 = [0,92, 172,272,369, 465, 576, 683, 784, 889, 970]
        reimu.Downframe2 = [92,80,100,97,96,110,105,102,105,103,130]

        if event == Down:
            reimu.motion = 6


    @staticmethod
    def exit(reimu, event):
        pass

    @staticmethod
    def do(reimu):
        if int(reimu.Downcheak) < 20:
            if int(reimu.Downcheak) < 9:
                reimu.frame1 = (reimu.frame1 + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 10
                reimu.frame2 = (reimu.frame2+ DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 10
            reimu.Downcheak = (reimu.Downcheak+ DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time)%21
        if int(reimu.Downcheak) >= 20:
            reimu.Downcheak = 20


    @staticmethod
    def draw(reimu):
        if reimu.motion == 6:
            reimu.Down.clip_draw(reimu.Downframe1[int(reimu.frame1)],0,reimu.Downframe2[int(reimu.frame2)],65, reimu.x, reimu.y-25)
class Item_Doll:
    @staticmethod
    def enter(reimu,event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.item1cheak = 0
        reimu.Skill2frame1 = [0, 66, 120, 217, 304, 392, 480, 572, 675]
        reimu.Skill2frame2 = [66, 54, 97, 87, 88, 88, 92, 103]
        if event == Item1:
            reimu.motion = 7
    @staticmethod
    def exit(reimu,event):
        pass
    @staticmethod
    def do(reimu):
        global HP,HPcheak,skillcheak
        if int(reimu.item1cheak) < 8:
            reimu.frame1 = (reimu.frame1 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 8
            reimu.frame2 = (reimu.frame2 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 8

            reimu.item1cheak = (reimu.item1cheak+ ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time)%9
        if int(reimu.item1cheak) >= 8:
            reimu.item1cheak = 0
            reimu.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(reimu):
        if reimu.motion == 7:
            reimu.item_use.clip_draw(0, 0, 40, 65, 600, 280)
            reimu.skill2.clip_draw(reimu.Skill2frame1[int(reimu.frame1)], 0, reimu.Skill2frame2[int(reimu.frame2)],120, reimu.x, reimu.y)
class Item_Potion:
    @staticmethod
    def enter(reimu, event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.item1cheak = 0
        reimu.Skill2frame1 = [0, 66, 120, 217, 304, 392, 480, 572, 675]
        reimu.Skill2frame2 = [66, 54, 97, 87, 88, 88, 92, 103]
        if event == Item2:
            reimu.motion = 8

    @staticmethod
    def exit(reimu, event):
        pass

    @staticmethod
    def do(reimu):
        global HP, HPcheak, skillcheak
        if int(reimu.item1cheak) < 8:
            reimu.frame1 = (reimu.frame1 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 8
            reimu.frame2 = (reimu.frame2 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 8

            reimu.item1cheak = (
                                           reimu.item1cheak + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9
        if int(reimu.item1cheak) >= 8:
            reimu.item1cheak = 0
            reimu.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(reimu):
        if reimu.motion == 8:
            reimu.item_use.clip_draw(40, 0, 40, 65, 600, 280)
            reimu.skill2.clip_draw(reimu.Skill2frame1[int(reimu.frame1)], 0, reimu.Skill2frame2[int(reimu.frame2)],120, reimu.x, reimu.y)

class Item_Clock:
    @staticmethod
    def enter(reimu, event):
        reimu.frame1 = 0
        reimu.frame2 = 0
        reimu.item1cheak = 0
        reimu.Skill2frame1 = [0, 66, 120, 217, 304, 392, 480, 572, 675]
        reimu.Skill2frame2 = [66, 54, 97, 87, 88, 88, 92, 103]
        if event == Item3:
            reimu.motion = 9

    @staticmethod
    def exit(reimu, event):
        pass

    @staticmethod
    def do(reimu):
        global HP, HPcheak, skillcheak
        if int(reimu.item1cheak) < 8:
            reimu.frame1 = (reimu.frame1 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 8
            reimu.frame2 = (reimu.frame2 + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 8

            reimu.item1cheak = (reimu.item1cheak + ITEM1_PER_ACTION * ITEM1ACTION_PER_TIME * game_framework.frame_time) % 9
        if int(reimu.item1cheak) >= 8:
            reimu.item1cheak = 0
            reimu.add_event(Stand)
            main_state.turn = 1
            main_state.DeckShow = 1

    @staticmethod
    def draw(reimu):
        if reimu.motion == 9:
            reimu.item_use.clip_draw(80, 0, 40, 65, 600, 280)
            reimu.skill2.clip_draw(reimu.Skill2frame1[int(reimu.frame1)], 0, reimu.Skill2frame2[int(reimu.frame2)],120, reimu.x, reimu.y)
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

class Enemy_Reimu:

    def __init__(self):
        self.x, self.y = 600, 200
        self.stand = load_image('./FCGimage/Reimu-Standing-Motion.png')

        self.skill1 = load_image('./FCGimage/Reimu-Skill1-Motion.png')

        self.skill2 = load_image('./FCGimage/Reimu-Skill2-Motion.png')

        self.skill3 = load_image('./FCGimage/Reimu-Skill3-Motion.png')


        self.Lastspell = load_image('./FCGimage/Reimu-Last Spell-Motion.png')
        self.Lasteffect = load_image('./FCGimage/Reimu-Lastspell1.png')
        self.Lasteffect2 = load_image('./FCGimage/Reimu-Lastspell2-1.png')
        self.Lasteffect3 = load_image('./FCGimage/Reimu-Lastspell3-2.png')

        self.Damage = load_image('./FCGimage/ReimuDamage-Motion.png')

        self.Down = load_image('./FCGimage/Reimu-Downs-Motion.png')
        self.skill1_sound = load_wav('./FCGimage/voice/reimu-skill1.wav')
        self.skill1_sound.set_volume(50)
        self.skill2_sound = load_wav('./FCGimage/voice/reimu-skill2.wav')
        self.skill2_sound.set_volume(50)
        self.skill3_sound = load_wav('./FCGimage/voice/reimu-skill3.wav')
        self.skill3_sound.set_volume(50)
        self.last_sound = load_wav('./FCGimage/voice/reimu-Last.wav')
        self.last_sound.set_volume(50)
        self.damage_sound = load_wav('./FCGimage/voice/reimu-damage.wav')
        self.damage_sound.set_volume(30)
        self.down_sound = load_wav('./FCGimage/voice/reimu-down.wav')
        self.down_sound.set_volume(70)
        self.item_sound = load_wav('./FCGimage/voice/reimu-item.wav')
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
