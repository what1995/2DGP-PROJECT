from pico2d import *
import os
import main_state
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
import Enemy_iku
#speed
PIXEL_PER_METER=(10.0/0.3)
Damage_SPEED_KMPH = 0.1
Damage_SPEED_MPM = (Damage_SPEED_KMPH*1000.0/60.0)
Damage_SPEED_MPS=(Damage_SPEED_MPM/60.0)
Damage_SPEED_PPS=(Damage_SPEED_MPS*PIXEL_PER_METER)
attack=None
damage=0
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
        global damage
        self.Power = main_state.P_HP
        if main_state.P_HPcheak == 1:
            if damage < self.Power:
                damage += Damage_SPEED_PPS
            if int(damage) == int(self.Power):
                main_state.P_HPcheak = 0
        if main_state.P_HPinit == 1:
            damage = 0
            main_state.P_HP = 0
            main_state.P_HPinit = 0
        if damage <0:
            damage=0
        if main_state.P_HP <0:
            main_state.P_HP=0

    def draw(self):
        global damage
        self.HPBar.draw(self.x, self.y)
        self.HP.clip_draw(0, 0, 252 - int(damage), 15, self.x + (damage // 2), self.y)


