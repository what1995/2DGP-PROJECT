from pico2d import *
import os
import BackgroundSelection
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage\\Background')
class BackGround:
    def __init__(self):
        self.Shrine = load_image('Hakurei Shrine.png')
        self.clock = load_image('clock tower.png')
        self.bamboo = load_image('bamboo.png')
        self.center =load_image('center.png')
        self.bgm_shrine = load_music('shrine.mp3')
        #self.bgm_shrine.set_volume(50)

    def update(self):
        #if BackgroundSelection.BGcheak == 1:
            #self.bgm_shrine.repeat_play()
        pass

    def draw(self):
        if BackgroundSelection.BGcheak==1:
            self.Shrine.draw(400, 300)
        if BackgroundSelection.BGcheak==0:
            self.bamboo.draw(400, 300)
        if BackgroundSelection.BGcheak==2:
            self.clock.draw(400, 300)
        self.center.draw(400, 500)
