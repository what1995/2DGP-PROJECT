from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuSkill3 = load_image('IkuSkill3-Motion.png')
IkuSkill3effect = load_image('IkuSkill3-1.png')


def Iku_Skill3():
        frame1 = [64,62,70,72,67,68]
        frame2 = [0,64,126,196,268,338,405]
        cheak=0
        S_frame=0
        i=0
        j=0
        while(cheak<19):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuSkill3.clip_draw(frame2[i],0,frame1[j],145,Enemy_X,All_Y)
                #플레이어
                IkuSkill3.clip_draw(frame2[i],145,frame1[j],145,Player_X,All_Y)
                if cheak<5:
                    i=(i+1)%7
                    j=(j+1)%6
                if cheak >=5:
                    #플레이어
                    IkuSkill3effect.clip_draw(S_frame *260,0,260,250,Enemy_X,All_Y+25)
                    #적
                    IkuSkill3effect.clip_draw(S_frame *260,0,260,250,Player_X,All_Y+25)
                    S_frame =(S_frame+1)%4
                    if cheak >17:
                        i=(i+1)%7
                        j=(j+1)%6
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Skill3()


close_canvas()
        
