from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
TenshiDown = load_image('TenshiDown-Motion.png')


def Tenshi_Down():
        frame1 = [120,115,115,120,125]
        frame2 = [0,120,235,350,470,595]
        cheak=0
        i=0
        j=0
        while(cheak<9):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiDown.clip_draw(frame2[i],0,frame1[j],75,Enemy_X,All_Y-30)
                #플레이어
                TenshiDown.clip_draw(frame2[i],75,frame1[j],75,Player_X,All_Y-30)
                if cheak<4:
                    i=(i+1)%6
                    j=(j+1)%5
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Down()


close_canvas()
        

