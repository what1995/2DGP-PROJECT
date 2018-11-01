from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import game_world
import game_framework
STAND_TIME_PER_ACTION=1
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
#LAST_PER_ACTION =10
#LASTEFFECT1_PER_ACTION=4
#LASTEFFECT2_PER_ACTION=2
STAND_PER_ACTION=9
# iku Event
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
            iku.stand.clip_draw(iku.Standframe1[int(iku.frame1)], 0, iku.Standframe2[int(iku.frame2)], 130, iku.x, iku.y)

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
        if iku.skill1cheak<8:
            iku.frame1 = (iku.frame1 + 1) % 11
            iku.frame2 = (iku.frame2 + 1) % 11
        if iku.skill1cheak>=8 and iku.skill1cheak<20:
            iku.S1frame = (iku.S1frame + 1) % 12
            iku.Skill1Eframe1 = (iku.Skill1Eframe1 + 1) % 7
        if iku.skill1cheak>=20:
            iku.frame1 = (iku.frame1 + 1) % 11
            iku.frame2 = (iku.frame2 + 1) % 11
        iku.skill1cheak +=1
        if  iku.skill1cheak==23:
            iku.skill1cheak=0

            iku.add_event(Stand)


    @staticmethod
    def draw(iku):
        if iku.motion == 1:
            iku.skill1.clip_draw(iku.Skill1frame1[iku.frame1], 0, iku.Skill1frame2[iku.frame2], 145, iku.x, iku.y)
            if iku.skill1cheak >= 8 and iku.skill1cheak < 20:
                iku.S1effect.clip_draw(0, iku.S1frame * 52, 360, 52, iku.x - 200, iku.y + 10)
                iku.S1effect2.clip_draw(iku.Skill1Eframe1 * 65, 0, 68, 60,200+10, iku.y + 10)

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
        if iku.skill2cheak < 19:
            if iku.skill2cheak < 11:
                iku.frame1 = (iku.frame1 + 1) % 15
                iku.frame2 = (iku.frame2 + 1) % 15
            if iku.skill2cheak > 5 and iku.skill2cheak < 15:
                if iku.skill2cheak > 8:
                    iku.skill2Mx += 10
                    iku.skill2Px += 10
            if iku.skill2cheak >= 15:
                iku.frame1 = (iku.frame1 + 1) % 15
                iku.frame2 = (iku.frame2 + 1) % 15
                iku.skill2Px -= 10
                iku.Skill2Eframe1 = (iku.Skill2Eframe1 + 1) % 6
            iku.skill2cheak += 1
        if iku.skill2cheak == 19:
            iku.skill2cheak = 0
            iku.add_event(Stand)


    @staticmethod
    def draw(iku):
        if iku.motion == 2:
            iku.skill2.clip_draw(iku.Skill2frame1[iku.frame1], 0, iku.Skill2frame2[iku.frame2], 145,iku.x-iku.skill2Px, iku.y)
            if iku.skill2cheak > 6 and iku.skill2cheak < 15:
                iku.S2effect.clip_draw(iku.S2frame * 193, 0, 193, 60, iku.x - iku.skill2Mx, iku.y - 5)

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
        if iku.skill3cheak < 19:
            if iku.skill3cheak < 5:
                iku.frame1 = (iku.frame1 + 1) % 6
                iku.frame2 = (iku.frame2 + 1) % 6
            if iku.skill3cheak >= 5:

                iku.S3frame = (iku.S3frame + 1) % 4
                if iku.skill3cheak > 17:
                    iku.frame1 = (iku.frame1 + 1) % 6
                    iku.frame2 = (iku.frame2 + 1) % 6
            iku.skill3cheak += 1
        if iku.skill3cheak == 18:
            iku.skill3cheak = 0
            iku.add_event(Stand)

    @staticmethod
    def draw(iku):
        if iku.motion == 3:
            iku.skill3.clip_draw(iku.Skill3frame1[iku.frame1], 0, iku.Skill3frame2[iku.frame2], 145,iku.x, iku.y)
            if iku.skill3cheak >= 5:
                iku.S3effect.clip_draw(iku.S3frame * 260, 0, 260, 250, 200,  iku.y + 25)

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

        if event == Last:
            iku.motion = 4

    @staticmethod
    def exit(iku, event):
        pass

    @staticmethod
    def do(iku):
        if iku.lastcheak < 19:
            if iku.lastcheak < 8:
                iku.frame1 = (iku.frame1 + 1) % 10
                iku.frame2 = (iku.frame2 + 1) % 10
            if iku.lastcheak >= 8:
                iku.LastspellEframe1 = (iku.LastspellEframe1 + 1) % 4
                iku.Lastspelld = (iku.Lastspelld + 1) % 2
                iku.Lastspellc = (iku.Lastspellc + 1) % 1
            if iku.lastcheak >= 16:
                iku.frame1 = (iku.frame1 + 1) % 10
                iku.frame2 = (iku.frame2 + 1) % 10
            iku.lastcheak += 1
        if iku.lastcheak == 18:
            iku.lastcheak = 0
            iku.add_event(Stand)


    @staticmethod
    def draw(iku):
        if iku.motion == 4:
            iku.Lastspell.clip_draw(iku.Lastframe1[iku.frame1], 0, iku.Lastframe2[iku.frame2], 140,iku.x, iku.y)
            if iku.lastcheak >= 8:
                iku.Lasteffect2.clip_draw(iku.IkuLastX[(iku.Lastspelld + 1) % 2], 0,iku.IkuLastY[iku.Lastspellc], 255, 200 + 50, iku.y + 70)
                iku.Lasteffect2.clip_draw(iku.IkuLastX[(iku.Lastspelld + 1) % 2], 0, iku.IkuLastY[iku.Lastspellc], 255, 200- 40, iku.y + 70)
                iku.Lasteffect2.clip_draw(iku.IkuLastX[iku.Lastspelld], 0, iku.IkuLastY[iku.Lastspellc], 255,200, iku.y + 70)
                iku.Lasteffect.clip_draw(iku.LastspellEframe1 * 270, 0, 270, 255, 200 + 20, iku.y + 210)

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
        if iku.Damagecheak < 3:
            iku.frame1 = (iku.frame1 + 1) % 4
            iku.frame2 = (iku.frame2 + 1) % 3
            iku.Damagecheak += 1
        if iku.Damagecheak == 3:
            iku.Damagecheak = 0
            iku.add_event(Stand)



    @staticmethod
    def draw(iku):
        if iku.motion == 5:
            iku.Damage.clip_draw(iku.Damageframe1[iku.frame1],0,iku.Damageframe2[iku.frame2],135, iku.x, iku.y)

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
        if iku.Downcheak < 20:
            if iku.Downcheak < 6:
                iku.frame1 = (iku.frame1 + 1) % 8
                iku.frame2 = (iku.frame2 + 1) % 7
            iku.Downcheak += 1
        if iku.Downcheak == 20:
            iku.Downcheak = 0
            iku.add_event(Stand)


        iku.timer -= 1

    @staticmethod
    def draw(iku):
        if iku.motion == 6:
            iku.Down.clip_draw(iku.Downframe1[iku.frame1], 0, iku.Downframe2[iku.frame2], 105, iku.x, iku.y-30)

next_state_table = {
    StandState: {Skill1: Skill1State, Skill2: Skill2State, Skill3:Skill3State,Last:Laststate, Damage:Damagestate,Down:Downstate},
    Skill1State: {Skill1: StandState,  Stand:StandState},
    Skill2State: {Skill2: StandState, Stand:StandState},
    Skill3State: {Skill3: StandState ,Stand: StandState},
    Laststate: {Last:StandState,Stand: StandState},
    Damagestate: {Damage:StandState, Stand:StandState},
    Downstate: {Down:StandState,Stand:StandState}

}

class Enemy_Iku:

    def __init__(self):
        self.x, self.y = 600, 200
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
        if (event.type, event.button) in key_event_table:
            key_event = key_event_table[(event.type, event.button)]
            self.add_event(key_event)
        elif (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

