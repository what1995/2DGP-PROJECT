from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
TenshiStanding = load_image('TenshiStanding-Motion.png')


def Tenshi_Standing():
        frame1 = [65,61,70,75,74]
        frame2 = [0,65,126,196,271,345]
        cheak=0
        i=0
        j=0
        while(cheak<5):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiStanding.clip_draw(frame2[i],0,frame1[j],115,Enemy_X,All_Y)
                #플레이어
                TenshiStanding.clip_draw(frame2[i],115,frame1[j],115,Player_X,All_Y)
                i=(i+1)%6
                j=(j+1)%5
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Standing()


close_canvas()
        

