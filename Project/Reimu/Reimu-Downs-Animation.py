from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=175
ReimuDowns = load_image('Reimu-Downs-Motion.png')


def Reimu_Down():
        frame=[0,92, 172,272,369, 465, 576, 683, 784, 889, 970]
        frame2=[92,80,100,97,96,110,105,102,105,103,130]
        i=0
        j=0
        cheak=0
        while(cheak<13):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #플레이어
                ReimuDowns.clip_draw(frame[i],65,frame2[j],65,Player_X,All_Y)
                #적
                ReimuDowns.clip_draw(frame[i],0,frame2[j],65,Enemy_X,All_Y)
                if(cheak<9):
                    i=(i+1)%11
                    j=(j+1)%10
                update_canvas()
                delay(0.3)
                cheak +=1


while(True):
    Reimu_Down()

close_canvas()
