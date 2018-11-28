from pico2d import *
import BackgroundSelection
import PlayerHP
import EnemyHP
import main_state
class BackGround:
    def __init__(self):
        self.Shrine = load_image('./FCGimage/Hakurei Shrine.png')
        self.clock = load_image('./FCGimage/clock tower.png')
        self.bamboo = load_image('./FCGimage/bamboo.png')
        self.center =load_image('./FCGimage/center.png')
        self.KnockOut = load_image('./FCGimage/KO.png')
        self.Backtitle = load_image('./FCGimage/backtitle.png')

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
            self.KnockOut.draw(400,250)
            self.Backtitle.draw(400, 400)
            main_state.DeckShow =0
            main_state.End=True

        elif int(EnemyHP.damage) >252:
            self.KnockOut.draw(400,250)
            self.Backtitle.draw(400,400)
            main_state.End = True
