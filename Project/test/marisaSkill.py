from pico2d import *
import os
import game_framework
import main_state
import DeckSelection
import marisa
import Enemy_marisa
import EnemyHP
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


name = 'marisaskill'
class MARISA_Skill1:


    def __init__(self):
        self.effect_Boom =None
        self.effect_Balls=None
        self.effect_MagicShot=None
        self.effect_Lazer=None
        if self.effect_Boom==None:
            self.effect_Boom = load_image('MarisaSkill1.png')
        if self.effect_Balls==None:
            self.effect_Balls = load_image('MarisaSkill2.png')
        if self.effect_MagicShot==None:
            self.effect_MagicShot = load_image('MarisaSKill3.png')
        if self.effect_Lazer==None:
            self.effect_Lazer = load_image('MarisaLastspell.png')

        #skill1
        self.Boom_Px = 600
        self.Boom_Ex = 200
        self.Boom_frame=0
        #skill2
        self.Balls_First = 120
        self.Balls_Second = 100
        self.Balls_Third =80
        #skill3
        self.MagicShot_Fly =120
        self.MagicShot_frame = 0
        #Last
        self.Lazer_frame=0



    def get_bb(self):
        pass


    def draw(self):
        if DeckSelection.character==1 and main_state.turn== 1 and main_state.Skill1_Start==True:
            self.effect_Boom.clip_draw(int(self.Boom_frame) * 260, 0, 260, 505, self.Boom_Px, 200+150)
        if main_state.EnemyPlayer==1 and main_state.turn== -1 and main_state.Skill1_Start==True:
            self.effect_Boom.clip_draw(int(self.Boom_frame) * 260, 0, 260, 505,self.Boom_Ex, 200+150)
        if DeckSelection.character==1 and main_state.turn ==1 and main_state.Skill2_Start ==True:
            self.effect_Balls.clip_draw(0, 125, 132, 125, 200 + self.Balls_First, 200)
            self.effect_Balls.clip_draw(132, 125, 132, 125, 200 + self.Balls_Second, 200)
            self.effect_Balls.clip_draw(264, 125, 132, 125, 200 + self.Balls_Third,200)
        if main_state.EnemyPlayer==1 and main_state.turn == -1 and main_state.Skill2_Start ==True:
            self.effect_Balls.clip_draw(0, 125, 132, 125, 600 - self.Balls_First, 200)
            self.effect_Balls.clip_draw(132, 125, 132, 125, 600 - self.Balls_Second, 200)
            self.effect_Balls.clip_draw(264, 125, 132, 125, 600 - self.Balls_Third, 200)
        if DeckSelection.character==1 and main_state.turn ==1 and main_state.Skill3_Start ==True:
            self.effect_MagicShot.clip_draw(int(self.MagicShot_frame) * 260, 255, 260, 255, 200 + self.MagicShot_Fly,200 + 25)
        if main_state.EnemyPlayer==1 and main_state.turn == -1 and main_state.Skill3_Start ==True:
            self.effect_MagicShot.clip_draw(int(self.MagicShot_frame) * 260, 0, 260, 255, 600 - self.MagicShot_Fly,200 + 25)
        if DeckSelection.character==1 and main_state.turn ==1 and main_state.Last_Start ==True:
            self.effect_Lazer.clip_draw(int(self.Lazer_frame) * 261, 250, 260, 250, 200 + 405, 200 - 10)
        if main_state.EnemyPlayer==1 and main_state.turn == -1 and main_state.Last_Start ==True:
            self.effect_Lazer.clip_draw(int(self.Lazer_frame) * 261, 0, 260, 250, 600 - 405, 200 - 10)

    def update(self):
        if main_state.Skill1_Start == True:
            main_state.marisa_skill1_atk_cheak=1
            self.Boom_frame = (self.Boom_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 9
        if main_state.Skill1_Start==False:
            main_state.marisa_skill1_atk_cheak = 0
            self.Boom_frame=0
        if main_state.Skill2_Start ==True:
            if self.Balls_First >350 and self.Balls_First<360:
                main_state.marisa_skill2_atk_cheak=1
            if self.Balls_First>=360:
                main_state.marisa_skill2_atk_cheak=0
            self.Balls_First  += int(MOTION_SPEED_PPS) * 5
            self.Balls_Second += int(MOTION_SPEED_PPS) * 5
            self.Balls_Third  += int(MOTION_SPEED_PPS) * 5
        if main_state.Skill2_Start ==False:
            main_state.marisa_skill2_atk_cheak = 0
            self.Balls_First  = 120
            self.Balls_Second = 100
            self.Balls_Third  = 80
        if main_state.Skill3_Start==True:
            if self.MagicShot_Fly >350 and self.MagicShot_Fly<360:
                main_state.marisa_skill3_atk_cheak=1
            if self.MagicShot_Fly>=360:
                main_state.marisa_skill3_atk_cheak=0
            self.MagicShot_frame = (self.MagicShot_frame + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 3
            self.MagicShot_Fly += int(MOTION_SPEED_PPS) * 5
        if main_state.Skill3_Start==False:
            main_state.marisa_skill3_atk_cheak = 0
            self.MagicShot_Fly = 120
        if main_state.Last_Start==True:
            main_state.marisa_last_atk_cheak = 1
            self.Lazer_frame = (self.Lazer_frame + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 7
        if main_state.Last_Start==False:
            main_state.marisa_last_atk_cheak = 0
