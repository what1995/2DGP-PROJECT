from pico2d import *
import os
import game_framework
import main_state
import DeckSelection
import reimu
import Enemy_reimu
import EnemyHP
#iku stand
STAND_TIME_PER_ACTION=1.2
STANDACTION_PER_TIME= 1.0/STAND_TIME_PER_ACTION
STAND_PER_ACTION=12

#skill1
SKILL1TIME_PER_ACTION=1.5
SKILL1ACTION_PER_TIME= 1.0/SKILL1TIME_PER_ACTION
SKILL1_PER_ACTION=15

#skill2
SKILL2TIME_PER_ACTION=1
SKILL2ACTION_PER_TIME= 0.8/SKILL2TIME_PER_ACTION
SKILL2_PER_ACTION=13

#skill3
SKILL3TIME_PER_ACTION=2
SKILL3ACTION_PER_TIME= 1.0/SKILL3TIME_PER_ACTION
SKILL3_PER_ACTION=25
# iku lastspell Action Speed
LASTTIME_PER_ACTION=2
LASTACTION_PER_TIME= 1.0/LASTTIME_PER_ACTION
LASTCHEAK_PER_ACTION=23
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
        self.effect_charm=None
        self.effect_shelter=None
        self.effect_jade=None
        self.effect_border=None
        self.effect_power_shelter=None
        self.effect_explosion=None
        if self.effect_charm==None:
            self.effect_charm=load_image('Reimu-Skill1.png')
        if self.effect_shelter==None:
            self.effect_shelter = load_image('Reimu-Skill2.png')
        if self.effect_jade==None:
            self.effect_jade=load_image('Reimu-Skill3.png')
        if self.effect_border==None:
            self.effect_border = load_image('Reimu-Lastspell2-1.png')
        if self.effect_power_shelter==None:
            self.effect_power_shelter = load_image('Reimu-Lastspell1.png')
        if self.effect_explosion == None:
            self.effect_explosion = load_image('Reimu-Lastspell3-2.png')



        #skill1
        self.Charm_Move= 80
        self.Charm_frame=0


        #skill2
        self.Shelter_frame=0

        
        #skill3
        self.Jade_Move=70
        self.Jade_frame=0


        #Last
        self.Explosin_PX =[580, 620, 600]
        self.Explosin_PY =[160.175, 200, 225, 250]
        self.Explosin_EX =[180, 220, 200]
        self.Explosin_X_frame=0
        self.Explosin_Y_frame=0
        self.Border_frame=0
        self.Power_Shelter_frame=0
        self.Explosin_frame=0
        self.Lastcheak=0



    def get_bb(self):
        pass


    def draw(self):
        if DeckSelection.character==0 and main_state.turn== 1 and main_state.Skill1_Start==True:
            self.effect_charm.clip_draw(int(self.Charm_frame) * 70, 0, 80, 110, 200 + self.Charm_Move, 200 + 10)
        if main_state.EnemyPlayer==0 and main_state.turn== -1 and main_state.Skill1_Start==True:
            self.effect_charm.clip_draw(int(self.Charm_frame) * 70, 0, 80, 110, 600 - self.Charm_Move, 200 + 10)
        if DeckSelection.character==0 and main_state.turn ==1 and main_state.Skill2_Start ==True:
            self.effect_shelter.clip_draw(int(self.Shelter_frame) * 133, 0, 134, 255, 600, 200 + 60)
        if main_state.EnemyPlayer==0 and main_state.turn == -1 and main_state.Skill2_Start ==True:
            self.effect_shelter.clip_draw(int(self.Shelter_frame) * 133, 0, 134, 255, 200, 200 + 60)
        if DeckSelection.character==0 and main_state.turn ==1 and main_state.Skill3_Start ==True:
            self.effect_jade.clip_draw(int(self.Jade_frame) * 117, 0, 117, 100, 200 + self.Jade_Move, 200)
        if main_state.EnemyPlayer==0 and main_state.turn == -1 and main_state.Skill3_Start ==True:
            self.effect_jade.clip_draw(int(self.Jade_frame) * 117, 0, 117, 100, 600 - self.Jade_Move, 200)
        if DeckSelection.character==0 and main_state.turn ==1 and main_state.Last_Start ==True:
            if self.Lastcheak >= 9 and self.Lastcheak<14:
                self.effect_power_shelter.clip_draw(int(self.Power_Shelter_frame) * 133, 0, 133, 207, 600, 230)
                self.effect_border.clip_draw(int(self.Border_frame) * 261, 0, 262, 126, 600 - 10, 160)
                self.effect_explosion.clip_draw(int(self.Explosin_frame) * 133, 0, 133, 126,self.Explosin_PX[int(self.Explosin_X_frame)],self.Explosin_PY[int(self.Explosin_Y_frame)])

        if main_state.EnemyPlayer==0 and main_state.turn == -1 and main_state.Last_Start ==True:
            if self.Lastcheak >= 9 and self.Lastcheak<14:
                self.effect_power_shelter.clip_draw(int(self.Power_Shelter_frame) * 133, 0, 133, 207, 200, 230)
                self.effect_border.clip_draw(int(self.Border_frame) * 261, 0, 262, 126, 200 + 10, 160)
                self.effect_explosion.clip_draw(int(self.Explosin_frame) * 133, 0, 133, 126,self.Explosin_EX[int(self.Explosin_X_frame)],self.Explosin_PY[int(self.Explosin_Y_frame)])

    def update(self):
        if main_state.Skill1_Start == True:
            if self.Charm_Move >350:
                main_state.HPcheak = 1
                main_state.reimu_skill1_atk_cheak = 1
            if self.Charm_Move>=400:
                main_state.reimu_skill1_atk_cheak = 0
            self.Charm_frame = (self.Charm_frame + SKILL1_PER_ACTION * SKILL1ACTION_PER_TIME * game_framework.frame_time) % 13
            self.Charm_Move += int(MOTION_SPEED_PPS) * 5
        if main_state.Skill1_Start == False:
            main_state.reimu_skill1_atk_cheak = 0
            self.Charm_Move=80

        if main_state.Skill2_Start ==True:
            main_state.HPcheak = 1
            main_state.reimu_skill2_atk_cheak = 1
            self.Shelter_frame = (self.Shelter_frame + SKILL2_PER_ACTION * SKILL2ACTION_PER_TIME * game_framework.frame_time) % 8
        if main_state.Skill2_Start == False:
            main_state.reimu_skill2_atk_cheak = 0
            self.Shelter_frame=0
        if main_state.Skill3_Start==True:
            if self.Jade_Move >350:
                main_state.HPcheak = 1
                main_state.reimu_skill3_atk_cheak = 1
            if self.Jade_Move>=360:
                main_state.reimu_skill3_atk_cheak = 0
            self.Jade_Move += int(MOTION_SPEED_PPS) * 5
            self.Jade_frame = (self.Jade_frame + SKILL3_PER_ACTION * SKILL3ACTION_PER_TIME * game_framework.frame_time) % 2
        if main_state.Skill3_Start == False:
            main_state.reimu_skill3_atk_cheak = 0
            self.Jade_Move=70
        if main_state.Last_Start==True:
            self.Lastcheak= (self.Lastcheak + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time)%23
            self.Power_Shelter_frame = (self.Power_Shelter_frame+ LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 13
            self.Border_frame = (self.Border_frame + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 8
            self.Explosin_frame  = (self.Explosin_frame + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 3
            if self.Lastcheak>=9:
                main_state.HPcheak = 1
                main_state.reimu_last_atk_cheak = 1
                self.Explosin_Y_frame = (self.Explosin_Y_frame + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 4
                self.Explosin_X_frame = (self.Explosin_X_frame + LASTCHEAK_PER_ACTION * LASTACTION_PER_TIME * game_framework.frame_time) % 2
        if main_state.Last_Start==False:
            main_state.reimu_last_atk_cheak = 0
            self.Explosin_X_frame = 0
            self.Explosin_Y_frame = 0
            self.Border_frame = 0
            self.Power_Shelter_frame = 0
            self.Explosin_frame = 0
            self.Lastcheak = 0
