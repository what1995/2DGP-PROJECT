from pico2d import *
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import iku

attack1=1
attack2=2
attack3=3
attack4=4

class Enemy_HP:
    def __init__(self):

        self.x = 600
        self.y = 500
        self.damage = 0
        self.Power = 0
        self.HPBar = load_image('HP-Damege.png')
        self.HP = load_image('HP-HP.png')

    def update(self):
        global attack1,attack2,attack3,attack4
        if attack1 == iku.HPcheak:
            self.damage = 20
        if attack2 == iku.HPcheak:
            self.damage = 30
        if attack3 == iku.HPcheak:
            self.damage = 40
        if attack4 == iku.HPcheak:
            self.damage = 50
        if 252-self.damage< 252:
            self.damage +=1

    def draw(self):
        self.HPBar.draw(self.x, self.y)
        self.HP.clip_draw(0, 0,252-self.damage,15,self.x-(self.damage//2),self.y)

