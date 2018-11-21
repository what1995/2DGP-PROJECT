from pico2d import *
import BackgroundSelection
class BG_Music:
    def __init__(self):
        if BackgroundSelection.BGcheak==0:
            self.bgm = load_music('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage\\Background\\bamboo.mp3')
            self.bgm.set_volume(25)
            self.bgm.repeat_play()
        if BackgroundSelection.BGcheak==1:
            self.bgm = load_music('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage\\Background\\shrine.mp3')
            self.bgm.set_volume(25)
            self.bgm.repeat_play()
        if BackgroundSelection.BGcheak==2:
            self.bgm = load_music('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage\\Background\\clocktower.mp3')
            self.bgm.set_volume(25)
            self.bgm.repeat_play()

    def update(self):

        pass

    def draw(self):
       pass
