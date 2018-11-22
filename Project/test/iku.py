from pico2d import *
import os
import game_framework
import main_state
import Deck
import Enemy_iku
import EnemyHP
#iku stand
STAND_TIME_PER_ACTION=1
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
STAND_PER_ACTION=9

#skill1
SKILL1TIME_PER_ACTION=2
SKILL1ACTION_PER_TIME= 1.0/SKILL1TIME_PER_ACTION
SKILL1_PER_ACTION=24

#skill2
SKILL2TIME_PER_ACTION=2
SKILL2ACTION_PER_TIME= 1.0/SKILL2TIME_PER_ACTION
SKILL2_PER_ACTION=20

#skill3
SKILL3TIME_PER_ACTION=2
SKILL3ACTION_PER_TIME= 1.0/SKILL3TIME_PER_ACTION
SKILL3_PER_ACTION=20
# iku lastspell Action Speed
LASTTIME_PER_ACTION=2
LASTACTION_PER_TIME= 0.5/LASTTIME_PER_ACTION
LASTCHEAK_PER_ACTION=35
#Damage
DAMAGETIME_PER_ACTION=0.5
DAMAGEACTION_PER_TIME= 1.0/DAMAGETIME_PER_ACTION
DAMAGE_PER_ACTION=4

#Down
DOWNTIME_PER_ACTION=3
DOWNACTION_PER_TIME= 1.0/DOWNTIME_PER_ACTION
DOWN_PER_ACTION=21
#motion speed
PIXEL_PER_METER=(10.0/0.3)
MOTION_SPEED_KMPH = 0.2
MOTION_SPEED_MPM = (MOTION_SPEED_KMPH*1000.0/60.0)
MOTION_SPEED_MPS=(MOTION_SPEED_MPM/60.0)
MOTION_SPEED_PPS=(MOTION_SPEED_MPS*PIXEL_PER_METER)
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import game_world

cheak1 = 0
skillcheak=0
# iku Event
Stand,Skill1, Skill2,Skill3, Last, Damage,Down = range(7)

key_event_table = {
(SDL_MOUSEBUTTONDOWN, 1): Skill1,
    (SDL_MOUSEBUTTONDOWN, 2): Skill2,
    (SDL_MOUSEBUTTONDOWN, 3): Skill3,
    (SDL_MOUSEBUTTONDOWN, 4): Last,
(SDL_KEYDOWN, SDLK_z): Damage,
(SDL_KEYDOWN, SDLK_x): Down
}

name = 'iku'
# Iku States
turn =None
HP=0
mouse_x,mouse_y=0,0
skillstart=False
class StandState:

    @staticmethod
    def enter(iku, event):
        iku.motion = 0
        iku.frame1 = 0
        iku.frame2 = 0
        iku.Standframe1 = [0, 73, 140, 200, 265, 324, 385, 446, 510, 580]
        iku.Standframe2 = [74, 64, 60, 62, 58, 59, 63, 65, 70]



    @staticmethod
    def exit(iku, event):
        pass
    @staticmethod
    def do(iku):
        iku.frame1 = (iku.frame1 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 9
        iku.frame2 = (iku.frame2 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 9




    @staticmethod
    def draw(iku):
        if iku.motion ==0:
            iku.stand.clip_draw(iku.Standframe1[int(iku.frame1)], 130, iku.Standframe2[int(iku.frame2)], 130, iku.x, iku.y)

class Skill1State:

    @staticmethod
    def enter(iku, event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.S1frame = 0
        iku.Skill1Eframe1 = 0
        iku.skill1cheak = 0
        iku.Skill1frame1 = [0, 68, 133, 193, 259, 329, 390, 470, 543, 615, 680, 745]
        iku.Skill1frame2 = [68, 65, 60, 66, 68, 59, 78, 74, 70, 63, 68]
        if event == Skill1:
            iku.motion = 1


    @staticmethod
    def exit(iku, event):
        pass

    @staticmethod
    def do(iku):
        global HP,HPcheak,skillcheak,skillstart
        if int(iku.skill1cheak)<8:
            iku.frame1 = (iku.frame1+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
            iku.frame2 = (iku.frame2 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
        if int(iku.skill1cheak)>=7 and int(iku.skill1cheak)<20:
            skillcheak=1
            main_state.HPcheak = 1
            main_state.Skill1_Start=True

        if int(iku.skill1cheak)>20:
            iku.frame1 = (iku.frame1 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
            iku.frame2 = (iku.frame2 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
        iku.skill1cheak =(iku.skill1cheak + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time)%24
        if int(iku.skill1cheak)>=22:
            skillcheak=0
            iku.add_event(Stand)
            main_state.Skill1_Start=False
            main_state.turn = -1
            Deck.spellcheak += 3

    @staticmethod
    def draw(iku):
        if iku.motion == 1:
            iku.skill1.clip_draw(iku.Skill1frame1[int(iku.frame1)], 145, iku.Skill1frame2[int(iku.frame2)], 145, iku.x, iku.y)


class Skill2State:
    @staticmethod
    def enter(iku,event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.skill2cheak = 0
        iku.skill2Px = 300
        iku.Skill2frame1 = [0, 70, 130, 200, 283, 356, 422, 490, 597, 732, 912, 1087, 1247, 1375, 1463, 1520]
        iku.Skill2frame2 = [70, 60, 70, 83, 73, 66, 66, 101, 133, 178, 173, 157, 124, 83, 63]
        if event == Skill2:
            iku.motion = 2

    @staticmethod
    def exit(iku,event):
        pass
    @staticmethod
    def do(iku):
        global HP,HPcheak,skillcheak
        if int(iku.skill2cheak) < 11:
            iku.frame1 = (iku.frame1 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            iku.frame2 = (iku.frame2 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
        if int(iku.skill2cheak) > 5 and int(iku.skill2cheak) < 15:
            skillcheak=1
            main_state.HPcheak =1
            if iku.skill2cheak > 8:
                main_state.Skill2_Start = True
                iku.skill2Px += int(MOTION_SPEED_PPS)
        if int(iku.skill2cheak) >= 15:
            iku.frame1 = (iku.frame1 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            iku.frame2 = (iku.frame2 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            main_state.Skill2_Start = False
            iku.skill2Px -= int(MOTION_SPEED_PPS)
        iku.skill2cheak = (iku.skill2cheak+ SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%20
        if int(iku.skill2cheak) >= 19:
            skillcheak=0
            iku.skill2cheak = 0
            iku.add_event(Stand)
            main_state.turn = -1
            Deck.spellcheak += 3


    @staticmethod
    def draw(iku):
        if iku.motion == 2:
            iku.skill2.clip_draw(iku.Skill2frame1[int(iku.frame1)], 145, iku.Skill2frame2[int(iku.frame2)], 145,iku.x+iku.skill2Px, iku.y)

class Skill3State:
    @staticmethod
    def enter(iku,event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.skill3cheak = 0
        iku.Skill3frame1 = [0, 64, 126, 196, 268, 338, 405]
        iku.Skill3frame2 = [64, 62, 70, 72, 67, 68]
        if event == Skill3:
            iku.motion = 3
    @staticmethod
    def exit(iku,event):
        pass
    @staticmethod
    def do(iku):
        global HP,HPcheak,skillcheak
        if int(iku.skill3cheak) < 19:
            if int(iku.skill3cheak) < 5:
                iku.frame1 = (iku.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
                iku.frame2 = (iku.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
            if int(iku.skill3cheak) >= 5:
                main_state.Skill3_Start=True
                if int(iku.skill3cheak) >= 7:
                    main_state.HPcheak=1
                if int(iku.skill3cheak) > 17:
                    iku.frame1 = (iku.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
                    iku.frame2 = (iku.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
            iku.skill3cheak = (iku.skill3cheak+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time)%20
        if int(iku.skill3cheak) >= 18:
            iku.skill3cheak = 0
            iku.add_event(Stand)
            main_state.Skill3_Start = False
            main_state.turn = -1
            Deck.spellcheak += 3

    @staticmethod
    def draw(iku):
        if iku.motion == 3:
            iku.skill3.clip_draw(iku.Skill3frame1[int(iku.frame1)], 145, iku.Skill3frame2[int(iku.frame2)], 145,iku.x, iku.y)


class Laststate:
    @staticmethod
    def enter(iku, event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.lastframe = 0
        iku.lastEframe1 = 0
        iku.lastcheak = 0
        iku.LastspellEframe1 = 0
        iku.Lastspellframe1 = 0
        iku.Lastspellframe2 = 0
        iku.Lastspellframe3 = 0
        iku.Lastspellc = 0
        iku.Lastspelld = 0
        iku.IkuLastX = [0, 120, 75]
        iku.IkuLastY = [120, 75]
        iku.Lastframe1 = [0, 60, 120, 180, 243, 315, 440, 570, 700, 825, 945, 1035]
        iku.Lastframe2 = [60, 60, 60, 63, 72, 125, 130, 130, 125, 120]
        iku.timer = pico2d.get_time()

        if event == Last:
            iku.motion = 4

    @staticmethod
    def exit(iku, event):
        pass

    @staticmethod
    def do(iku):
        global HP,HPcheak
        if int(iku.lastcheak) < 34:
            if int(iku.lastcheak) < 8:
                iku.frame1 = (iku.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10
                iku.frame2 = (iku.frame2 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10
            if int(iku.lastcheak) >= 8:
                iku.LastspellEframe1 = (iku.LastspellEframe1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 4
                iku.Lastspelld = (iku.Lastspelld +LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 2
                iku.Lastspellc = (iku.Lastspellc + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 2
                main_state.HPcheak = 1
            if int(iku.lastcheak) >= 32:
                iku.frame1 = (iku.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10
                iku.frame2 = (iku.frame2 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10

        iku.lastcheak = (iku.lastcheak + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) %35
        if int(iku.lastcheak) >= 34:
            iku.lastcheak = 0
            iku.add_event(Stand)
            main_state.turn = -1
            Deck.spellcheak += 3
        #delay(0.1)

    @staticmethod
    def draw(iku):
        if iku.motion == 4:
            iku.Lastspell.clip_draw(iku.Lastframe1[int(iku.frame1)], 140, iku.Lastframe2[int(iku.frame2)], 140,iku.x, iku.y)
            if int(iku.lastcheak) >= 8:
                iku.Lasteffect2.clip_draw(iku.IkuLastX[int((iku.Lastspelld + 1) % 2)], 0,iku.IkuLastY[int(iku.Lastspellc)], 255, 600 - 50, iku.y + 70)
                iku.Lasteffect2.clip_draw(iku.IkuLastX[int((iku.Lastspelld + 1) % 2)], 0, iku.IkuLastY[int(iku.Lastspellc)], 255, 600 + 40, iku.y + 70)
                iku.Lasteffect2.clip_draw(iku.IkuLastX[int(iku.Lastspelld)], 0, iku.IkuLastY[int(iku.Lastspellc)], 255,600, iku.y + 70)
                iku.Lasteffect.clip_draw(int(iku.LastspellEframe1) * 270, 0, 270, 255, 600 + 15, iku.y + 210)

class Damagestate:
    @staticmethod
    def enter(iku, event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.Damagecheak = 0
        iku.Damageframe = 0
        iku.Damageframe1 = [0, 94, 174, 245]
        iku.Damageframe2 = [94, 80, 73]
        if event == Damage:
            iku.motion = 5
    @staticmethod
    def exit(iku, event):
        pass

    @staticmethod
    def do(iku):
        if int(iku.Damagecheak) < 3:
            iku.frame1 = (iku.frame1+ DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 3
            iku.frame2 = (iku.frame2 +DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time) % 3
            iku.Damagecheak = ( iku.Damagecheak + DAMAGE_PER_ACTION * DAMAGEACTION_PER_TIME * game_framework.frame_time)%4
        if int(iku.Damagecheak) >= 3:
            iku.Damagecheak = 0
            iku.add_event(Stand)


    @staticmethod
    def draw(iku):
        if iku.motion == 5:
            iku.Damage.clip_draw(iku.Damageframe1[int(iku.frame1)],135,iku.Damageframe2[int(iku.frame2)],135, iku.x, iku.y)

class Downstate:
    @staticmethod
    def enter(iku, event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.Downcheak=0
        iku.Downframe1 = [0, 125, 240, 374, 514, 651, 793, 945]
        iku.Downframe2 = [125, 115, 134, 140, 136, 140, 158]

        if event == Down:
            iku.motion = 6


    @staticmethod
    def exit(iku, event):
        pass

    @staticmethod
    def do(iku):
        if int(iku.Downcheak) < 20:
            if int(iku.Downcheak) < 6:
                iku.frame1 = (iku.frame1 + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 7
                iku.frame2 = (iku.frame2 +DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time) % 7
            iku.Downcheak = (iku.Downcheak + DOWN_PER_ACTION * DOWNACTION_PER_TIME * game_framework.frame_time)%21
        if int(iku.Downcheak) >= 20:
            iku.Downcheak = 20
            #iku.add_event(Stand)


        #iku.timer -= 1

    @staticmethod
    def draw(iku):
        if iku.motion == 6:
            iku.Down.clip_draw(iku.Downframe1[int(iku.frame1)], 105, iku.Downframe2[int(iku.frame2)], 105, iku.x, iku.y-30)

next_state_table = {
    StandState: {Skill1: Skill1State, Skill2: Skill2State, Skill3:Skill3State,Last:Laststate, Damage:Damagestate,Down:Downstate},
    Skill1State: {Skill1: StandState,  Stand:StandState},
    Skill2State: {Skill2: StandState, Stand:StandState},
    Skill3State: {Skill3: StandState ,Stand: StandState},
    Laststate: {Last:StandState,Stand: StandState},
    Damagestate: {Damage:StandState, Stand:StandState},
    Downstate: {Down:StandState,Stand:StandState}

}

class Iku:

    def __init__(self):
        self.x, self.y = 200, 200
        self.stand = load_image('Iku-Standing-Motion.png')

        self.skill1 = load_image('IkuSkill1-Motion.png')

        self.skill2 = load_image('IkuSkill2-Motion.png')

        self.skill3 = load_image('IkuSkill3-Motion.png')

        self.Lastspell = load_image('IkuLastspell-Motion.png')
        self.Lasteffect = load_image('IkuLastspell1-1.png')
        self.Lasteffect2 = load_image('IkuLastspell1-2.png')

        self.Damage = load_image('IkuDamage-Motion.png')

        self.Down = load_image('Iku-Down-Motion.png')
        self.skill1_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\iku-skill1.wav')
        self.skill1_sound.set_volume(50)
        self.skill2_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\iku-skill2.wav')
        self.skill2_sound.set_volume(50)
        self.skill3_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\iku-skill3.wav')
        self.skill3_sound.set_volume(50)
        self.last_sound = load_wav('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\Project\\FCGimage\\voice\\iku-Last.wav')
        self.last_sound.set_volume(50)

        self.dir = 1
        self.motion = 0
        self.frame = 0
        self.timer = 0
        self.event_que = []
        self.cur_state = StandState
        self.cur_state.enter(self, None)





    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        global cheak1,HP,mouse_x,mouse_y,AtkBuff,DefBuff
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y=event.x, 600- event.y
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): ##스킬키 체크
            if main_state.turn==1:
                if mouse_x > 270 and mouse_x < 330 and mouse_y > 55 and mouse_y < 145:
                    if Deck.PlayerDeck[Deck.spellcheak%12]==1:
                        main_state.HP += 20 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill1_sound.play()
                        self.add_event(Skill1)
                    if Deck.PlayerDeck[Deck.spellcheak%12]==2:
                        main_state.HP += 30* main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill2_sound.play()
                        self.add_event(Skill2)
                    if Deck.PlayerDeck[Deck.spellcheak%12]==3:
                        main_state.HP += 40 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill3_sound.play()
                        self.add_event(Skill3)
                    if Deck.PlayerDeck[Deck.spellcheak%12]==4:
                        main_state.HP += 50 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.last_sound.play()
                        self.add_event(Last)
                if mouse_x > 370 and mouse_x < 430 and mouse_y > 55 and mouse_y < 145:
                    if Deck.PlayerDeck[(Deck.spellcheak+1)%12]==1:
                        main_state.HP += 20 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill1_sound.play()
                        self.add_event(Skill1)
                    if Deck.PlayerDeck[(Deck.spellcheak+1)%12]==2:
                        main_state.HP += 30 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill2_sound.play()
                        self.add_event(Skill2)
                    if Deck.PlayerDeck[(Deck.spellcheak+1)%12]==3:
                        main_state.HP += 40 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill3_sound.play()
                        self.add_event(Skill3)
                    if Deck.PlayerDeck[(Deck.spellcheak+1)%12]==4:
                        main_state.HP += 50 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.last_sound.play()
                        self.add_event(Last)
                if mouse_x > 470 and mouse_x < 530 and mouse_y > 55 and mouse_y < 145:
                    if Deck.PlayerDeck[(Deck.spellcheak+2)%12]==1:
                        main_state.HP += 20 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill1_sound.play()
                        self.add_event(Skill1)
                    if Deck.PlayerDeck[(Deck.spellcheak+2)%12]==2:
                        main_state.HP += 30 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill2_sound.play()
                        self.add_event(Skill2)
                    if Deck.PlayerDeck[(Deck.spellcheak+2)%12]==3:
                        main_state.HP += 40 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.skill3_sound.play()
                        self.add_event(Skill3)
                    if Deck.PlayerDeck[(Deck.spellcheak+2)%12]==4:
                        main_state.HP += 50 * main_state.Player_AtkBuff * main_state.Player_DefBuff
                        self.last_sound.play()
                        self.add_event(Last)
        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

