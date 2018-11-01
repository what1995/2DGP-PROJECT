from pico2d import *
import os
import main_state
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import Enemy_iku
attack=None
class Player_HP:
    def __init__(self):
        global attack
        self.x = 200
        self.y = 500
        self.damage=0
        self.Power= 1
        self.stop=0
        self.HPBar = load_image('HP-Damege.png')
        self.HP = load_image('HP-HP.png')

    def update(self):
        global attack
        #attack = iku.HP
        if self.Power <10:
            self.damage -=2
            self.Power+=1

    def draw(self):
        self.HPBar.draw(self.x, self.y)

        self.HP.clip_draw(0, 0,252+self.damage,15,self.x-(self.damage/2),self.y)


