from pico2d import *
import os
import BackgroundSelection
os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage\\Background')
class BG_Music:
    def __init__(self):
        if BackgroundSelection.BGcheak==0:
            self.bgm = load_music('bamboo.mp3')
            self.bgm.set_volume(30)
            self.bgm.repeat_play()
        if BackgroundSelection.BGcheak==1:
            self.bgm = load_music('shrine.mp3')
            self.bgm.set_volume(30)
            self.bgm.repeat_play()
        if BackgroundSelection.BGcheak==2:
            self.bgm = load_music('clocktower.mp3')
            self.bgm.set_volume(30)
            self.bgm.repeat_play()

    def update(self):

        pass

    def draw(self):
       pass
