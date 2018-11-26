from pico2d import *
import os
import BackgroundSelection
import PlayerHP
import EnemyHP
import main_state
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
class BackGround:
    def __init__(self):
        self.Shrine = load_image('Hakurei Shrine.png')
        self.clock = load_image('clock tower.png')
        self.bamboo = load_image('bamboo.png')
        self.center =load_image('center.png')
        self.KnockOut = load_image('KO.png')

    def update(self):

        pass

    def draw(self):
        if BackgroundSelection.BGcheak==1:
            self.Shrine.draw(400, 300)
        if BackgroundSelection.BGcheak==0:
            self.bamboo.draw(400, 300)
        if BackgroundSelection.BGcheak==2:
            self.clock.draw(400, 300)
        self.center.draw(400, 500)

        if int(PlayerHP.damage) >252:
            self.KnockOut.draw(400,300)
            main_state.DeckShow =0
            main_state.End=True

        elif int(EnemyHP.damage) >252:
            self.KnockOut.draw(400,300)
            main_state.End = True
