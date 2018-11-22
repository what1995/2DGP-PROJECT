from pico2d import *
import os
import game_framework
import main_state
import reimu
import Enemy_reimu
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


name = 'reimuskill'
class REIMU_Skill1:


    def __init__(self):
        pass



        #skill1


        #skill2

        
        #skill3


        #Last



    def get_bb(self):
        pass


    def draw(self):
        if main_state.turn== 1 and main_state.Skill1_Start==True:
            pass
        if main_state.turn== -1 and main_state.Skill1_Start==True:
            pass
        if main_state.turn ==1 and main_state.Skill2_Start ==True:
            pass
        if main_state.turn == -1 and main_state.Skill2_Start ==True:
            pass
        if main_state.turn ==1 and main_state.Skill3_Start ==True:
            pass
        if main_state.turn == -1 and main_state.Skill3_Start ==True:
            pass
        if main_state.turn ==1 and main_state.Last_Start ==True:
            pass
        if main_state.turn == -1 and main_state.Last_Start ==True:
            pass

    def update(self):
        if main_state.Skill1_Start == True:
            pass
        if main_state.Skill2_Start == False:
            pass
        if main_state.Skill2_Start ==True:
            pass
        if main_state.Skill3_Start==True:
            pass
        if main_state.Last_Start==True:
            pass
