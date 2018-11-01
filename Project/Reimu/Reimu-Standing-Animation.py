from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
ReimuStanding = load_image('Reimu-Standing-Motion.png')


def Reimu_Standing():
        frame = 0
        cheak=0
        while(cheak<11):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                ReimuStanding.clip_draw(frame *100,0,97,105,Enemy_X,All_Y)
                #플레이어
                ReimuStanding.clip_draw(frame *100,105,97,105,Player_X,All_Y)
                frame=(frame+1)%11
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Reimu_Standing()


close_canvas()
        
