from pico2d import *
import os
import game_framework
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import game_world

STAND_TIME_PER_ACTION=1
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
#LAST_PER_ACTION =10
#LASTEFFECT1_PER_ACTION=4
#LASTEFFECT2_PER_ACTION=2
STAND_PER_ACTION=9
# marisa Event
Stand,Skill1, Skill2,Skill3, Last, Damage,Down = range(7)

key_event_table = {
(SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT): Skill1,
    (SDL_KEYDOWN, SDLK_a): Skill2,
    (SDL_KEYDOWN, SDLK_s): Skill3,
    (SDL_KEYDOWN, SDLK_d): Last,
(SDL_KEYDOWN, SDLK_z): Damage,
(SDL_KEYDOWN, SDLK_x): Down
}


# marisa States

class StandState:

    @staticmethod
    def enter(marisa, event):
        marisa.motion = 0
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
        marisa.Standframe2 = [65,61,62,62,62,60,62,61,60,62]

    @staticmethod
    def exit(marisa, event):
        pass
    @staticmethod
    def do(marisa):
        marisa.frame1 = (marisa.frame1 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 9
        marisa.frame2 = (marisa.frame2 + STAND_PER_ACTION * STANDACTION_PER_TIME * game_framework.frame_time) % 9




    @staticmethod
    def draw(marisa):
        if marisa.motion ==0:
            marisa.stand.clip_draw(marisa.Standframe1[int(marisa.frame1)], 0, marisa.Standframe2[int(marisa.frame2)], 110, marisa.x, marisa.y)

class Skill1State:

    @staticmethod
    def enter(marisa, event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.S1frame = 0
        marisa.Skill1Eframe1 = 0
        marisa.skill1cheak = 0
        marisa.Skill1frame1 = [0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        marisa.Skill1frame2 = [71, 61, 65, 65, 58, 72, 72, 66, 60]
        if event == Skill1:
            marisa.motion = 1


    @staticmethod
    def exit(marisa, event):
        pass
        #if event ==SPACE:
        #    boy.fire_ball()
    @staticmethod
    def do(marisa):
        if marisa.skill1cheak<18:
            if marisa.skill1cheak < 6:
                marisa.frame1 = (marisa.frame1 + 1) % 10
                marisa.frame2 = (marisa.frame2 + 1) % 9
            if marisa.skill1cheak >6:
                if marisa.skill1cheak < 15:
                    marisa.Skill1Eframe1 = (marisa.Skill1Eframe1 + 1) % 9
                if marisa.skill1cheak >= 15:
                    marisa.frame1 = (marisa.frame1 + 1) % 10
                    marisa.frame2 = (marisa.frame2 + 1) % 9

            marisa.skill1cheak +=1
        if marisa.skill1cheak==18:
            marisa.skill1cheak=0

            marisa.add_event(Stand)


    @staticmethod
    def draw(marisa):
        if marisa.motion == 1:
            marisa.skill1.clip_draw(marisa.Skill1frame1[marisa.frame1], 0, marisa.Skill1frame2[marisa.frame2], 105, marisa.x, marisa.y)
            if marisa.skill1cheak > 6:
                marisa.S1effect.clip_draw(marisa.Skill1Eframe1 * 260, 0, 260, 505, 200, marisa.y + 150)

class Skill2State:
    @staticmethod
    def enter(marisa,event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.skill2cheak = 0
        marisa.Skill2Ex1 = 120
        marisa.Skill2Ex2 = 100
        marisa.Skill2Ex3 = 80
        marisa.Skill2frame1 =  [0, 85, 165, 240, 318, 395, 464, 525]
        marisa.Skill2frame2 = [85, 80, 75, 78, 76, 67, 64]
        if event == Skill2:
            marisa.motion = 2

    @staticmethod
    def exit(marisa,event):
        pass
    @staticmethod
    def do(marisa):
        if marisa.skill2cheak < 7:
            marisa.frame1 = (marisa.frame1 + 1) % 8
            marisa.frame2 = (marisa.frame2 + 1) % 7
            marisa.Skill2Ex1 += 75
            marisa.Skill2Ex2 += 75
            marisa.Skill2Ex3 += 75
            marisa.skill2cheak += 1
        if marisa.skill2cheak == 7:
            marisa.skill2cheak = 0
            marisa.add_event(Stand)


    @staticmethod
    def draw(marisa):
        if marisa.motion == 2:
            marisa.skill2.clip_draw(marisa.Skill2frame1[marisa.frame1], 0, marisa.Skill2frame2[marisa.frame2], 120,marisa.x, marisa.y)
            marisa.S2effect.clip_draw(0, 0, 132, 125, marisa.x - marisa.Skill2Ex1,  marisa.y)
            marisa.S2effect.clip_draw(132, 0, 132, 125, marisa.x - marisa.Skill2Ex2,  marisa.y)
            marisa.S2effect.clip_draw(264, 0, 132, 125, marisa.x - marisa.Skill2Ex3,  marisa.y)

class Skill3State:
    @staticmethod
    def enter(marisa,event):
        marisa.frame1 = 0
        marisa.frame2 = 0
        marisa.S3frame = 0
        marisa.skill3cheak = 0
        marisa.Skill3Ex1 = 120
        marisa.Skill3frame1 = [0, 65, 125, 195, 275, 332, 412, 500, 590, 661]
        marisa.Skill3frame2 = [65, 60, 70, 80, 60, 76, 85, 89, 68, 61]
        if event == Skill3:
            marisa.motion = 3


    @staticmethod
    def exit(marisa,event):
        pass

    @staticmethod
    def do(marisa):
        if marisa.skill3cheak < 17:
            if marisa.skill3cheak < 7:
                marisa.frame1 = (marisa.frame1 + 1) % 10
                marisa.frame2 = (marisa.frame2 + 1) % 10
            if marisa.skill3cheak >= 7:
                marisa.S3frame = (marisa.S3frame + 1) % 3
                marisa.Skill3Ex1 += 80
            if marisa.skill3cheak >= 13:
                    marisa.frame1 = (marisa.frame1 + 1) % 10
                    marisa.frame2 = (marisa.frame2 + 1) % 10
            marisa.skill3cheak += 1
        if marisa.skill3cheak == 17:
            marisa.skill3cheak = 0
            marisa.add_event(Stand)

    @staticmethod
    def draw(marisa):
        if marisa.motion == 3:
            marisa.skill3.clip_draw(marisa.Skill3frame1[marisa.frame1], 0, marisa.Skill3frame2[marisa.frame2], 110,marisa.x, marisa.y)
            if marisa.skill3cheak >= 7:
                marisa.S3effect.clip_draw(marisa.S3frame * 260, 0, 260, 255,marisa.x - marisa.Skill3Ex1,  marisa.y + 25)

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
        if marisa.lastcheak < 18:
            marisa.frame1 = (marisa.frame1 + 1) % 17
            marisa.frame2 = (marisa.frame2 + 1) % 17
            if marisa.lastcheak > 4 and marisa.lastcheak<11:
                marisa.LastspellEframe1 = (marisa.LastspellEframe1 + 1) % 7

            marisa.lastcheak += 1
        if marisa.lastcheak == 18:
            marisa.lastcheak = 0
            marisa.add_event(Stand)


    @staticmethod
    def draw(marisa):
        if marisa.motion == 4:
            marisa.Lastspell.clip_draw(marisa.Lastframe1[marisa.frame1], 0, marisa.Lastframe2[marisa.frame2], 120,marisa.x-250, marisa.y)
            if marisa.lastcheak > 4 and marisa.lastcheak < 11:
                marisa.Lasteffect.clip_draw(marisa.LastspellEframe1 * 261, 0, 260, 250, marisa.x-405, marisa.y-10)

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
        if marisa.Damagecheak < 3:
            marisa.frame1 = (marisa.frame1 + 1) % 4
            marisa.frame2 = (marisa.frame2 + 1) % 3
            marisa.Damagecheak += 1
        if marisa.Damagecheak == 3:
            marisa.Damagecheak = 0
            marisa.add_event(Stand)



    @staticmethod
    def draw(marisa):
        if marisa.motion == 5:
            marisa.Damage.clip_draw(marisa.Damageframe1[marisa.frame1],0,marisa.Damageframe2[marisa.frame2],115, marisa.x, marisa.y)

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
        if marisa.Downcheak < 20:
            if marisa.Downcheak < 6:
                marisa.frame1 = (marisa.frame1 + 1) % 7
                marisa.frame2 = (marisa.frame2 + 1) % 7
            marisa.Downcheak += 1
        if marisa.Downcheak == 20:
            marisa.Downcheak = 0
            marisa.add_event(Stand)


        marisa.timer -= 1

    @staticmethod
    def draw(marisa):
        if marisa.motion == 6:
            marisa.Down.clip_draw(marisa.Downframe1[marisa.frame1], 0, marisa.Downframe2[marisa.frame2], 95, marisa.x, marisa.y-20)

next_state_table = {
    StandState: {Skill1: Skill1State, Skill2: Skill2State, Skill3:Skill3State,Last:Laststate, Damage:Damagestate,Down:Downstate},
    Skill1State: {Skill1: StandState,  Stand:StandState},
    Skill2State: {Skill2: StandState, Stand:StandState},
    Skill3State: {Skill3: StandState ,Stand: StandState},
    Laststate: {Last:StandState,Stand: StandState},
    Damagestate: {Damage:StandState, Stand:StandState},
    Downstate: {Down:StandState,Stand:StandState}

}

class Enemy_Marisa:

    def __init__(self):
        self.x, self.y = 600, 200
        self.stand = load_image('MarisaStanding-Motion.png')

        self.skill1 = load_image('MarisaSkill1-Motion.png')
        self.S1effect = load_image('MarisaSkill1.png')

        self.skill2 = load_image('MarisaSkill2-Motion.png')
        self.S2effect = load_image('MarisaSkill2.png')

        self.skill3 = load_image('MarisaSkill3-Motion.png')
        self.S3effect = load_image('MarisaSKill3.png')

        self.Lastspell = load_image('MarisaLastspell-Motion.png')
        self.Lasteffect = load_image('MarisaLastspell.png')

        self.Damage = load_image('MarisaDamage-Motion.png')

        self.Down = load_image('MarisaDown-Motion.png')

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

