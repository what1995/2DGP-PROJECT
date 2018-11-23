from pico2d import *
import os
import main_state
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import iku

attack1=1
attack2=2
attack3=3
attack4=4
damage = 0
Damagecheak=0
#speed
PIXEL_PER_METER=(10.0/0.3)
Damage_SPEED_KMPH = 0.1
Damage_SPEED_MPM = (Damage_SPEED_KMPH*1000.0/60.0)
Damage_SPEED_MPS=(Damage_SPEED_MPM/60.0)
Damage_SPEED_PPS=(Damage_SPEED_MPS*PIXEL_PER_METER)
class Enemy_HP:
    def __init__(self):

        self.x = 600
        self.y = 500
        self.Power = 0
        self.Damage=0
        self.HPBar = load_image('HP-Damege.png')
        self.HP = load_image('HP-HP.png')

    def update(self):
        global attack1, attack2, attack3, attack4,damage
        self.Power = main_state.HP
        if main_state.HPcheak==1:
            if damage < self.Power:
                damage +=Damage_SPEED_PPS
            if int(damage) == int(self.Power):
                main_state.HPcheak=0
        if main_state.HPinit==1:
            damage=0


    def draw(self):
        global damage
        self.HPBar.draw(self.x, self.y)
        self.HP.clip_draw(0, 0,252-int(damage),15,self.x-(damage//2),self.y)

