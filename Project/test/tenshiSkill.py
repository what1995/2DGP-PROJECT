from pico2d import *
import os
import game_framework
import main_state
import DeckSelection
import tenshi
import Enemy_tenshi
import EnemyHP
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
import game_world


name = 'tenshiskill'
class TENSHI_Skill1:


    def __init__(self):
        self.hight_stone = None
        self.mini_ston=None
        if self.hight_stone==None:
            self.hight_stone=load_image('TenshiSkill1.png')
        if self.mini_ston==None:
            self.mini_ston = load_image('TenshiSkill2-1.png')



        #skill1
        self.Hight_Stone_frame=0
        self.Hight_Stone_FX_frame = 0
        self.Hight_Stone_FY_frame = 0
        self.Hight_Stone_FX = [0, 106, 235, 367, 509, 646, 746, 875]
        self.Hight_Stone_FY = [107, 129, 132, 142, 135, 98, 135]
        self.Hight_Stone_Move=160
        self.SKill1cheak=0


        #skill2
        self.Mini_Stone_frame=0
        self.Mini_Stone_First = 75
        self.Mini_Stone_Second = 95
        self.Mini_Stone_Third = 85
        self.Skill2cheak=0

        
        #skill3


        #Last



    def get_bb(self):
        pass


    def draw(self):
        if DeckSelection.character==3 and main_state.turn== 1 and main_state.Skill1_Start==True:
            if self.SKill1cheak > 7:
                self.hight_stone.clip_draw(self.Hight_Stone_FX[int(self.Hight_Stone_FX_frame)], 0,self.Hight_Stone_FY[int(self.Hight_Stone_FY_frame)], 165, 600, 200+self.Hight_Stone_Move)
        if main_state.EnemyPlayer==3 and main_state.turn== -1 and main_state.Skill1_Start==True:
            if self.SKill1cheak > 7:
                self.hight_stone.clip_draw(self.Hight_Stone_FX[int(self.Hight_Stone_FX_frame)], 0,self.Hight_Stone_FY[int(self.Hight_Stone_FY_frame)], 165, 200, 200+self.Hight_Stone_Move)
        if DeckSelection.character==3 and main_state.turn ==1 and main_state.Skill2_Start ==True:
            self.mini_ston.clip_draw(0, int(self.Mini_Stone_frame) * 50, 70, 50, 50 + self.Mini_Stone_First , 200)
            self.mini_ston.clip_draw(0, int(self.Mini_Stone_frame) * 50, 70, 50, 50 + self.Mini_Stone_Second, 200 + 25)
            self.mini_ston.clip_draw(0, int(self.Mini_Stone_frame) * 50, 70, 50, 50 + self.Mini_Stone_Third , 200 - 25)
        if main_state.EnemyPlayer==3 and main_state.turn == -1 and main_state.Skill2_Start ==True:
            self.mini_ston.clip_draw(70, int(self.Mini_Stone_frame) * 50, 70, 50, 750 - self.Mini_Stone_First, 200)
            self.mini_ston.clip_draw(70, int(self.Mini_Stone_frame) * 50, 70, 50, 750 - self.Mini_Stone_Second, 200 + 25)
            self.mini_ston.clip_draw(70, int(self.Mini_Stone_frame) * 50, 70, 50, 750 - self.Mini_Stone_Third, 200 - 25)
        if DeckSelection.character==3 and main_state.turn ==1 and main_state.Skill3_Start ==True:
            pass
        if main_state.EnemyPlayer==3 and main_state.turn == -1 and main_state.Skill3_Start ==True:
            pass
        if DeckSelection.character==3 and main_state.turn ==1 and main_state.Last_Start ==True:
            pass
        if main_state.EnemyPlayer==3 and main_state.turn == -1 and main_state.Last_Start ==True:
            pass

    def update(self):
        if main_state.Skill1_Start == True:
            self.SKill1cheak=(self.SKill1cheak + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 16
            if self.SKill1cheak > 7:
                self.Hight_Stone_FX_frame = (self.Hight_Stone_FX_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 8
                self.Hight_Stone_FY_frame = (self.Hight_Stone_FY_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 7
            if self.SKill1cheak >9:
                self.Hight_Stone_Move -= int(MOTION_SPEED_PPS) * 3
        if main_state.Skill1_Start == False:
            self.Hight_Stone_frame = 0
            self.Hight_Stone_FX_frame = 0
            self.Hight_Stone_FY_frame = 0
            self.Hight_Stone_Move = 160
            self.SKill1cheak = 0
        if main_state.Skill2_Start == False:
            self.Mini_Stone_frame=(self.Mini_Stone_frame +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 3
            self.Mini_Stone_First  = 75
            self.Mini_Stone_Second = 95
            self.Mini_Stone_Third  = 85
            self.Skill2cheak=0
        if main_state.Skill2_Start ==True:
            self.Skill2cheak=( self.Skill2cheak +  SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time)%22
            self.Mini_Stone_frame = (self.Mini_Stone_frame + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 3
            if self.Skill2cheak >2:
                self.Mini_Stone_First += int(MOTION_SPEED_PPS) * 5
            if self.Skill2cheak >4:
                self.Mini_Stone_Second += int(MOTION_SPEED_PPS) * 5
            if self.Skill2cheak >6:
                self.Mini_Stone_Third += int(MOTION_SPEED_PPS) * 5
        if main_state.Skill3_Start==True:
            pass
        if main_state.Last_Start==True:
            pass
