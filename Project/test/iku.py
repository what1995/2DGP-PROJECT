from pico2d import *
import os
import game_framework
import main_state
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
LASTACTION_PER_TIME= 1.0/LASTTIME_PER_ACTION
LASTCHEAK_PER_ACTION=20
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
HPcheak=0
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
        #if event ==SPACE:
        #    boy.fire_ball()
    @staticmethod
    def do(iku):
        global HP,HPcheak
        if int(iku.skill1cheak)<8:
            iku.frame1 = (iku.frame1+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
            iku.frame2 = (iku.frame2 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
        if int(iku.skill1cheak)>=7 and int(iku.skill1cheak)<20:
            iku.S1frame = (iku.S1frame +SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 12
            iku.Skill1Eframe1 = (iku.Skill1Eframe1 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 7
            if int(iku.skill1cheak)==10:
                #HP=10
                HPcheak=1
            if int(iku.skill1cheak)==11:
                #HP=10
                HPcheak=0

        if int(iku.skill1cheak)>20:
            iku.frame1 = (iku.frame1 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
            iku.frame2 = (iku.frame2 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 11
        iku.skill1cheak =(iku.skill1cheak + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time)%24
        if int(iku.skill1cheak)>=22:
            #turn = -1
            #iku.skill1cheak=0
            iku.add_event(Stand)

    @staticmethod
    def draw(iku):
        if iku.motion == 1:
            iku.skill1.clip_draw(iku.Skill1frame1[int(iku.frame1)], 145, iku.Skill1frame2[int(iku.frame2)], 145, iku.x, iku.y)
            if int(iku.skill1cheak) >= 8 and int(iku.skill1cheak) < 20:
                iku.S1effect.clip_draw(0, int(iku.S1frame) * 52, 360, 52, iku.x + 200, iku.y + 10)
                iku.S1effect2.clip_draw(int(iku.Skill1Eframe1) * 65, 0, 68, 60,600-10, iku.y + 10)

class Skill2State:
    @staticmethod
    def enter(iku,event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.S2frame = 0
        iku.Skill2Eframe1 = 0
        iku.skill2cheak = 0
        iku.skill2Px = 300
        iku.skill2Mx = 330
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
            if iku.skill2cheak > 8:
                iku.skill2Mx += int(MOTION_SPEED_PPS)
                iku.skill2Px += int(MOTION_SPEED_PPS)

        if int(iku.skill2cheak) >= 15:
            iku.frame1 = (iku.frame1 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            iku.frame2 = (iku.frame2 + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            iku.skill2Px -= int(MOTION_SPEED_PPS)
            iku.Skill2Eframe1 = (iku.Skill2Eframe1 +SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 6
        iku.skill2cheak = (iku.skill2cheak+ SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%20
        if int(iku.skill2cheak) >= 19:
            skillcheak=0
            iku.skill2cheak = 0
            iku.add_event(Stand)


    @staticmethod
    def draw(iku):
        if iku.motion == 2:
            iku.skill2.clip_draw(iku.Skill2frame1[int(iku.frame1)], 145, iku.Skill2frame2[int(iku.frame2)], 145,iku.x+iku.skill2Px, iku.y)
            if int(iku.skill2cheak) > 6 and int(iku.skill2cheak) < 15:
                iku.S2effect.clip_draw(int(iku.S2frame)* 193, 60, 193, 60, iku.x + iku.skill2Mx, iku.y - 5)

class Skill3State:
    @staticmethod
    def enter(iku,event):
        iku.frame1 = 0
        iku.frame2 = 0
        iku.S3frame = 0
        iku.Skill3Eframe1 = 0
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
        global HP,HPcheak
        if int(iku.skill3cheak) < 19:
            if int(iku.skill3cheak) < 5:
                iku.frame1 = (iku.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
                iku.frame2 = (iku.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
            if int(iku.skill3cheak) >= 5:

                iku.S3frame = (iku.S3frame + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 4
                if int(iku.skill3cheak) == 12:
                    # HP=10
                    HPcheak = 3
                if int(iku.skill3cheak) == 13:
                    # HP=10
                    HPcheak = 0
                if int(iku.skill3cheak) > 17:
                    iku.frame1 = (iku.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
                    iku.frame2 = (iku.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 6
            iku.skill3cheak = (iku.skill3cheak+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time)%20
        if int(iku.skill3cheak) >= 18:
            iku.skill3cheak = 0
            iku.add_event(Stand)

    @staticmethod
    def draw(iku):
        if iku.motion == 3:
            iku.skill3.clip_draw(iku.Skill3frame1[int(iku.frame1)], 145, iku.Skill3frame2[int(iku.frame2)], 145,iku.x, iku.y)
            if int(iku.skill3cheak) >= 5:
                iku.S3effect.clip_draw(int(iku.S3frame) * 260, 0, 260, 250, 600,  iku.y + 25)

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
        if int(iku.lastcheak) < 19:
            if int(iku.lastcheak) < 8:
                iku.frame1 = (iku.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10
                iku.frame2 = (iku.frame2 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10
            if int(iku.lastcheak) >= 8:
                iku.LastspellEframe1 = (iku.LastspellEframe1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 4
                iku.Lastspelld = (iku.Lastspelld +LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 2
                iku.Lastspellc = (iku.Lastspellc + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 2
                if int(iku.lastcheak) == 10:
                    # HP=10
                    HPcheak = 4
                if int(iku.lastcheak) > 10:
                    # HP=10
                    HPcheak = 0

            if int(iku.lastcheak) >= 16:
                iku.frame1 = (iku.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10
                iku.frame2 = (iku.frame2 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 10

        iku.lastcheak = (iku.lastcheak + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) %20
        if int(iku.lastcheak) >= 19:
            iku.lastcheak = 0
            iku.add_event(Stand)
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
        self.S1effect = load_image('IkuSkill1-1.png')
        self.S1effect2 = load_image('IkuSkill1-2.png')

        self.skill2 = load_image('IkuSkill2-Motion.png')
        self.S2effect = load_image('IkuSkill2-1.png')

        self.skill3 = load_image('IkuSkill3-Motion.png')
        self.S3effect = load_image('IkuSkill3-1.png')

        self.Lastspell = load_image('IkuLastspell-Motion.png')
        self.Lasteffect = load_image('IkuLastspell1-1.png')
        self.Lasteffect2 = load_image('IkuLastspell1-2.png')

        self.Damage = load_image('IkuDamage-Motion.png')

        self.Down = load_image('Iku-Down-Motion.png')

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
        global cheak1,HP
        cheak1=2
        if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): ##스킬키 체크
            if main_state.skillcheak==1:
                self.add_event(Skill1)
            if main_state.skillcheak==2:
                HP +=20
                self.add_event(Skill2)
            if main_state.skillcheak==3:
                self.add_event(Skill3)
            if main_state.skillcheak==4:
                self.add_event(Last)



        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

