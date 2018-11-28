from pico2d import *
import BackgroundSelection
class BG_Music:
    def __init__(self):
        if BackgroundSelection.BGcheak==0:
            self.bgm = load_music('./FCGimage/Background/bamboo.mp3')
            self.bgm.set_volume(25)
            self.bgm.repeat_play()
        if BackgroundSelection.BGcheak==1:
            self.bgm = load_music('./FCGimage/Background/shrine.mp3')
            self.bgm.set_volume(25)
            self.bgm.repeat_play()
        if BackgroundSelection.BGcheak==2:
            self.bgm = load_music('./FCGimage/Background/clocktower.mp3')
            self.bgm.set_volume(25)
            self.bgm.repeat_play()

    def update(self):

        pass

    def draw(self):
       pass
