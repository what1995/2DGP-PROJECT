from pico2d import *
import os
import game_framework
import main_state
import iku
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

name = 'ikuskill'
# Iku States
turn =None
HP=0
HPcheak=0
mouse_x,mouse_y=0,0


class IKU_Skill1:
    effect_Line = None
    effect_Ball=None

    def __init__(self):
        if IKU_Skill1.effect_Line ==None:
            IKU_Skill1.effect_Line = load_image('IkuSkill1-1.png')
        if IKU_Skill1.effect_Ball ==None:
            IKU_Skill1.effect_Ball = load_image('IkuSkill1-2.png')

        self.Line_x, self.Line_y = 400, 210
        self.Ball_x, self.Ball_y = 600-10, 210
        self.Line_frame = 0
        self.Ball_frame =0
    def get_bb(self):
        return self.Ball_x-10,self.Ball_y-25,self.Ball_x+40,self.Ball_y+25


    def draw(self):
        if iku.skillstart==1:
            self.effect_Line.clip_draw(0, int(self.Line_frame) * 52, 360, 52,self.Line_x,self.Line_y)
            self.effect_Ball.clip_draw(int(self.Ball_frame) * 65, 0, 68, 60, self.Line_x+200,self.Line_y)
            draw_rectangle(*self.get_bb())
    def update(self):
        if iku.skillstart == 1:
            self.Line_frame = (self.Line_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 12
            self.Ball_frame = (self.Ball_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 7