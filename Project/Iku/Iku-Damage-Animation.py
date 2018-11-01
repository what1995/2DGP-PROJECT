from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuDamage = load_image('IkuDamage-Motion.png')


def Iku_Damage():
        frame2 = [94,80,73]
        frame1 = [0,94,174,245]
        cheak=0
        i=0
        j=0
        while(cheak<3):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuDamage.clip_draw(frame1[i],0,frame2[j],135,Enemy_X,All_Y)
                #플레이어
                IkuDamage.clip_draw(frame1[i],135,frame2[j],135,Player_X,All_Y)
                i=(i+1)%4
                j=(j+1)%3
                update_canvas()
                delay(0.2)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Damage()


close_canvas()
        
