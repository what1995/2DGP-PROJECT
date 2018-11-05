from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import game_world
import game_framework
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
#motion speed
PIXEL_PER_METER=(10.0/0.3)
MOTION_SPEED_KMPH = 0.2
MOTION_SPEED_MPM = (MOTION_SPEED_KMPH*1000.0/60.0)
MOTION_SPEED_MPS=(MOTION_SPEED_MPM/60.0)
MOTION_SPEED_PPS=(MOTION_SPEED_MPS*PIXEL_PER_METER)
Stand,Skill1, Skill2,Skill3, Last, Damage,Down = range(7)

key_event_table = {
(SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): Skill1,
    (SDL_KEYDOWN, SDLK_a): Skill2,
    (SDL_KEYDOWN, SDLK_s): Skill3,
    (SDL_KEYDOWN, SDLK_d): Last,
(SDL_KEYDOWN, SDLK_z): Damage,
(SDL_KEYDOWN, SDLK_x): Down
}


# Iku States

class StandState:

    @staticmethod
    def enter(tenshi, event):
        tenshi.motion = 0
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.Standframe1 = [0,65,126,196,271,345]
        tenshi.Standframe2 = [65,61,70,75,74]
    @staticmethod
    def exit(tenshi, event):
        pass
    @staticmethod
    def do(tenshi):
        tenshi.frame1 = (tenshi.frame1 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 5
        tenshi.frame2 = (tenshi.frame2 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 5



    @staticmethod
    def draw(tenshi):
        if tenshi.motion ==0:
            tenshi.stand.clip_draw(tenshi.Standframe1[int(tenshi.frame1)], 115, tenshi.Standframe2[int(tenshi.frame2)], 115, tenshi.x, tenshi.y)

class Skill1State:

    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.S1frame = 0
        tenshi.Skill1Eframe1 = 0
        tenshi.skill1cheak = 0
        tenshi.Skill1Y = 160
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
        if int(tenshi.skill1cheak)<15:
            tenshi.frame1 = (tenshi.frame1 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.frame2 = (tenshi.frame2 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 15
            if int(tenshi.skill1cheak)>7:
                tenshi.S1frame = (tenshi.S1frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 8
                tenshi.Skill1Eframe1 = (tenshi.Skill1Eframe1 + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 7
            if int(tenshi.skill1cheak) > 9:
                tenshi.Skill1Y -= int(MOTION_SPEED_PPS)*1
            tenshi.skill1cheak =(tenshi.skill1cheak+ SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time)%16
        if int(tenshi.skill1cheak)>=15:
            tenshi.skill1cheak=0
            tenshi.Skill1Y = 160
            tenshi.add_event(Stand)

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 1:
            tenshi.skill1.clip_draw(tenshi.Skill1frame1[int(tenshi.frame1)],160,tenshi.Skill1frame2[int(tenshi.frame2)],160, tenshi.x, tenshi.y+30)
            if int(tenshi.skill1cheak) > 7:
                tenshi.S1effect.clip_draw(tenshi.TenshiS1X[int(tenshi.S1frame)],0,tenshi.TenshiS1Y[int(tenshi.Skill1Eframe1)],165,600,tenshi.y+tenshi.Skill1Y)

class Skill2State:
    @staticmethod
    def enter(tenshi,event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.S2frame = 0
        tenshi.Skill2Eframe1 = 0
        tenshi.skill2cheak = 0
        tenshi.TSkill2Px1 = 75
        tenshi.TSkill2Px2 = 97
        tenshi.TSkill2Px3 = 65
        tenshi.Skill2frame1 = [0,70,149,228,305,378,448,520,590,664,740,814,888,960,1026,1100]
        tenshi.Skill2frame2 = [70,79,79,77,73,69,68,67,70,69,66,69,66,60,60]
        if event == Skill2:
            tenshi.motion = 2

    @staticmethod
    def exit(tenshi,event):
        pass
    @staticmethod
    def do(tenshi):
        if int(tenshi.skill2cheak) < 21:
            if int(tenshi.skill2cheak) < 10:
                tenshi.frame1 = (tenshi.frame1 +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
                tenshi.frame2 = (tenshi.frame2 +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            if int(tenshi.skill2cheak) >= 10:
                tenshi.S2frame = (tenshi.S2frame +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 3
                if int(tenshi.skill2cheak) < 21:
                    tenshi.TSkill2Px1 += int(MOTION_SPEED_PPS)*2
                    tenshi.TSkill2Px2 += int(MOTION_SPEED_PPS)*3
                    tenshi.TSkill2Px3 += int(MOTION_SPEED_PPS)*4
                if int(tenshi.skill2cheak) >= 16:
                    tenshi.frame1 = (tenshi.frame1+  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
                    tenshi.frame2 = (tenshi.frame2 +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 15
            tenshi.skill2cheak = ( tenshi.skill2cheak +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%22
        if int(tenshi.skill2cheak) >= 21:
            tenshi.skill2cheak = 0
            tenshi.add_event(Stand)


    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 2:
            tenshi.skill2.clip_draw(tenshi.Skill2frame1[int(tenshi.frame1)], 115, tenshi.Skill2frame2[int(tenshi.frame2)], 115,tenshi.x, tenshi.y)
            if int(tenshi.skill2cheak) >= 10:
                tenshi.S2effect.clip_draw(0,int(tenshi.S2frame)*50,70,50,tenshi.x+tenshi.TSkill2Px1,tenshi.y)
                tenshi.S2effect.clip_draw(0,int(tenshi.S2frame)*50,70,50,tenshi.x+tenshi.TSkill2Px2,tenshi.y+25)
                tenshi.S2effect.clip_draw(0,int(tenshi.S2frame)*50,70,50,tenshi.x+tenshi.TSkill2Px3,tenshi.y-25)

class Skill3State:
    @staticmethod
    def enter(tenshi,event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.S3frame = 0
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
        if int(tenshi.skill3cheak) < 16:
            if  int(tenshi.skill3cheak) < 10:
                tenshi.frame1 = (tenshi.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
                tenshi.frame2 = (tenshi.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
            if  int(tenshi.skill3cheak)>6 and  int(tenshi.skill3cheak)<14:
                tenshi.S3frame = (tenshi.S3frame + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 7
            if  int(tenshi.skill3cheak) >= 14:
                tenshi.frame1 = (tenshi.frame1 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
                tenshi.frame2 = (tenshi.frame2 + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 12
            tenshi.skill3cheak = (tenshi.skill3cheak+ SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time)%17
        if  int(tenshi.skill3cheak)>= 16:
            tenshi.skill3cheak = 0
            tenshi.add_event(Stand)
    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 3:
            tenshi.skill3.clip_draw(tenshi.Skill3frame1[int(tenshi.frame1)], 115, tenshi.Skill3frame2[int(tenshi.frame2)], 115,tenshi.x+200, tenshi.y)
            if  int(tenshi.skill3cheak)>6 and  int(tenshi.skill3cheak)<14:
                tenshi.S3effect.clip_draw(int(tenshi.S3frame)*260,107,260,120,tenshi.x+350,tenshi.y-10)

class Laststate:
    @staticmethod
    def enter(tenshi, event):
        tenshi.frame1 = 0
        tenshi.frame2 = 0
        tenshi.lastframe = 0
        tenshi.lastEframe1 = 0
        tenshi.lastcheak = 0
        tenshi.LastspellEframe1 = 0
        tenshi.Lastframe1 = [0,72,142,266,435,577,715,842,928,1064,1200,1328,1430,1540,1640,1790,1965,2130,2295,2395,2465]
        tenshi.Lastframe2 = [72,70,124,169,142,137,124,85,132,131,124,96,109,95,145,167,155,150,90,72]

        if event == Last:
            tenshi.motion = 4

    @staticmethod
    def exit(tenshi, event):
        pass

    @staticmethod
    def do(tenshi):
        if int(tenshi.lastcheak) < 20:
            tenshi.frame1 = (tenshi.frame1 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 20
            tenshi.frame2 = (tenshi.frame2 + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 20
            if int(tenshi.lastcheak) == 9:
                tenshi.LastspellEframe1 = 1
            if int(tenshi.lastcheak) == 15:
                tenshi.LastspellEframe1 = 2

            tenshi.lastcheak = (tenshi.lastcheak+ LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time)%21
        if int(tenshi.lastcheak) >= 20:
            tenshi.lastcheak = 0
            tenshi.add_event(Stand)

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 4:
            tenshi.Lastspell.clip_draw(tenshi.Lastframe1[int(tenshi.frame1)], 165, tenshi.Lastframe2[int(tenshi.frame2)], 165,tenshi.x+200, tenshi.y+30)
            if int(tenshi.lastcheak) > 3:
                tenshi.Lasteffect2.clip_draw(0,0,250,250,600, tenshi.y )
                if int(tenshi.lastcheak) > 4:
                    tenshi.Lasteffect.clip_draw(tenshi.LastspellEframe1*260,0,260,250,600, tenshi.y )

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
            tenshi.Damage.clip_draw(int(tenshi.frame1)*80,115,78,115, tenshi.x, tenshi.y)

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
            tenshi.Downcheak = 0
            tenshi.add_event(Stand)


        #tenshi.timer -= 1

    @staticmethod
    def draw(tenshi):
        if tenshi.motion == 6:
            tenshi.Down.clip_draw(tenshi.Downframe1[int(tenshi.frame1)], 75, tenshi.Downframe2[int(tenshi.frame2)], 75, tenshi.x, tenshi.y-33)

next_state_table = {
    StandState: {Skill1: Skill1State, Skill2: Skill2State, Skill3:Skill3State,Last:Laststate, Damage:Damagestate,Down:Downstate},
    Skill1State: {Skill1: StandState,  Stand:StandState},
    Skill2State: {Skill2: StandState, Stand:StandState},
    Skill3State: {Skill3: StandState ,Stand: StandState},
    Laststate: {Last:StandState,Stand: StandState},
    Damagestate: {Damage:StandState, Stand:StandState},
    Downstate: {Down:StandState,Stand:StandState}

}

class Tenshi:

    def __init__(self):
        self.x, self.y = 200, 200
        self.stand = load_image('TenshiStanding-Motion.png')

        self.skill1 = load_image('TenshiSkill1-Motion.png')
        self.S1effect = load_image('TenshiSkill1.png')

        self.skill2 = load_image('TenshiSkill2-Motion.png')
        self.S2effect = load_image('TenshiSkill2-1.png')

        self.skill3 = load_image('TenshiSkill3-Motion.png')
        self.S3effect = load_image('TenshiSkill3.png')

        self.Lastspell = load_image('TenshiLastspell-Motion.png')
        self.Lasteffect = load_image('TenshiLastspell1-1.png')
        self.Lasteffect2 = load_image('TenshiLastspell1-2.png')

        self.Damage = load_image('TenshiDamage-Motion.png')

        self.Down = load_image('TenshiDown-Motion.png')

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
        if (event.type, event.button) in key_event_table:
            key_event = key_event_table[(event.type, event.button)]
            self.add_event(key_event)
        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

