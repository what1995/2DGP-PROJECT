from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =190
Enemy_X=610
All_Y=175
IkuDown = load_image('Iku-Down-Motion.png')


def Iku_Down():
        frame1 = [125,115,134,140,136,140,158]
        frame2 = [0,125,240,374,514,651,793,945]
        cheak=0
        i=0
        j=0
        while(cheak<10):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuDown.clip_draw(frame2[i],0,frame1[j],105,Enemy_X,All_Y)
                #플레이어
                IkuDown.clip_draw(frame2[i],105,frame1[j],105,Player_X,All_Y)
                if cheak <6:
                    i=(i+1)%8
                    j=(j+1)%7
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Down()


close_canvas()
        
