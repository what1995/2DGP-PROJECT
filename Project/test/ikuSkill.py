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
import game_world


name = 'ikuskill'
class IKU_Skill1:


    def __init__(self):
        self.effect_Line = None
        self.effect_Ball = None
        self.drill=None
        if self.effect_Line ==None:
            self.effect_Line = load_image('IkuSkill1-1.png')
        if self.effect_Ball ==None:
            self.effect_Ball = load_image('IkuSkill1-2.png')
        if self.drill ==None:
            self.drill = load_image('ikuSkill2-1.png')


        #skill1
        self.Line_Px, self.Line_Py = 400, 210
        self.Ball_Px, self.Ball_Py = 600-10, 210
        self.Line_Ex, self.Line_Ey = 390, 210
        self.Ball_Ex, self.Ball_Ey = 200 + 10, 210
        self.Line_frame = 0
        self.Ball_frame =0

        #skill2
        self.Drill_Pmove = 530
        self.Drill_Emove=270
        self.Drill_frame =0

    def get_bb(self):
        if main_state.turn == 1:
            return self.Ball_Px-20,self.Ball_Py-25,self.Ball_Px+30,self.Ball_Py+25
        if main_state.turn == -1:
            return self.Ball_Ex-20,self.Ball_Ey-25,self.Ball_Ex+30,self.Ball_Ey+25


    def draw(self):
        if main_state.turn== 1 and main_state.Skill1_Start==True:
            self.effect_Line.clip_draw(0, int(self.Line_frame) * 52, 360, 52,self.Line_Px,self.Line_Py)
            self.effect_Ball.clip_draw(int(self.Ball_frame) * 65, 0, 68, 60, self.Ball_Px,self.Ball_Py)
            draw_rectangle(*self.get_bb())
        if main_state.turn== -1 and main_state.Skill1_Start==True:
            self.effect_Line.clip_draw(0, int(self.Line_frame) * 52, 360, 52,self.Line_Ex,self.Line_Ey)
            self.effect_Ball.clip_draw(int(self.Ball_frame) * 65, 0, 68, 60, self.Ball_Ex,self.Ball_Ey)
            draw_rectangle(*self.get_bb())
        if main_state.turn ==1 and main_state.Skill2_Start ==True:
            self.drill.clip_draw(int(self.Drill_frame) * 193, 60, 193, 60, self.Drill_Pmove, 200-5)
        if main_state.turn == -1 and main_state.Skill2_Start ==True:
            self.drill.clip_draw(int(self.Drill_frame) * 193, 0, 193, 60, self.Drill_Emove, 200-5)

    def update(self):
        if main_state.Skill1_Start == True:
            self.Line_frame = (self.Line_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 12
            self.Ball_frame = (self.Ball_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 7
        if main_state.Skill2_Start == False:
            self.Drill_Pmove = 530
            self.Drill_Emove = 270
        if main_state.Skill2_Start ==True:
            if main_state.turn == 1:
                self.Drill_Pmove += int(MOTION_SPEED_PPS)
            if main_state.turn == -1:
                self.Drill_Emove -= int(MOTION_SPEED_PPS)
            self.Drill_frame = (self.Drill_frame + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 6
