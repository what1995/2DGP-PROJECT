from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import iku

attack1=1
attack2=2
attack3=3
attack4=4
damage = 0
Damagecheak=0
class Enemy_HP:
    def __init__(self):

        self.x = 600
        self.y = 500
        self.Power = 0
        self.Damage=0
        self.HPBar = load_image('HP-Damege.png')
        self.HP = load_image('HP-HP.png')

    def update(self):
        global attack1, attack2, attack3, attack4,damage,Damagecheak
        self.Power = iku.HP
        Damagecheak =iku.skillcheak
        if damage < self.Power:
            damage +=0.1


    def draw(self):
        global damage
        self.HPBar.draw(self.x, self.y)
        self.HP.clip_draw(0, 0,252-int(damage),15,self.x-(damage//2),self.y)

