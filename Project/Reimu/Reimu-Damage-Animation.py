from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
ReimuDamage = load_image('ReimuDamage-Motion.png')


def Reimu_Damage():
        frame = 0
        cheak=0
        while(cheak<3):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                ReimuDamage.clip_draw(frame *109,0,110,90,Enemy_X,All_Y)
                #플레이어
                ReimuDamage.clip_draw(frame *112,90,110,90,Player_X,All_Y)
                frame=(frame+1)%3
                update_canvas()
                delay(0.2)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Reimu_Damage()


close_canvas()
        
