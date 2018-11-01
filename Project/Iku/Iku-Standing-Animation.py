from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuStanding = load_image('Iku-Standing-Motion.png')


def Iku_Standing():
        frame1 = [74,64,60,62,58,59,63,65,70]
        frame2 = [0,73, 140, 200, 265,324, 385, 446, 510, 580]
        cheak=0
        i=0
        j=0
        while(cheak<9):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuStanding.clip_draw(frame2[i],0,frame1[j],130,Enemy_X,All_Y)
                #플레이어
                IkuStanding.clip_draw(frame2[i],130,frame1[j],130,Player_X,All_Y)
                i=(i+1)%10
                j=(j+1)%9
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Standing()


close_canvas()
        
