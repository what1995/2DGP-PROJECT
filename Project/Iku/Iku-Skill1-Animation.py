from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuSkill1 = load_image('IkuSkill1-Motion.png')
IkuSkill1effect = load_image('IkuSkill1-1.png')
IkuSkill1effect2 = load_image('IkuSkill1-2.png')

def Iku_Skill1():
        frame1 = [68,65,60,66,68,59,78,74,70,63,68]
        frame2 = [0,68,133,193,259,329,390,470,543,615,680,745]
        cheak=0
        Sframe=0
        Sframe1=0
        i=0
        j=0
        while(cheak<23):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuSkill1.clip_draw(frame2[i],0,frame1[j],145,Enemy_X,All_Y)
                #플레이어
                IkuSkill1.clip_draw(frame2[i],145,frame1[j],145,Player_X,All_Y)
                if cheak<8:
                    i=(i+1)%12
                    j=(j+1)%11
                if cheak>=8:
                    if cheak<20:
                        #플레이어
                        IkuSkill1effect.clip_draw(0,Sframe*52,360,52,Player_X+200,All_Y+10)
                        IkuSkill1effect2.clip_draw(Sframe1*65,0,68,60,Enemy_X-10,All_Y+10)
                        #적
                        IkuSkill1effect.clip_draw(0,Sframe*52,360,52,Enemy_X-210,All_Y+10)
                        IkuSkill1effect2.clip_draw(Sframe1*66,0,68,60,Player_X+10,All_Y+10)
                        Sframe = (Sframe+1)%12
                        Sframe1 = (Sframe1+1)%7
                    if cheak>=20:
                        i=(i+1)%12
                        j=(j+1)%11
                        
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Skill1()


close_canvas()
        
