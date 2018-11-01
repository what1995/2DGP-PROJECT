from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
ReimuSkill1 = load_image('Reimu-Skill1-Motion.png')
ReimuSkill1effect = load_image('Reimu-Skill1.png')

def Reimu_Skill1():
        frame=[0,108,213,327,434,541,638,787,936,1080,1215,1319,1425]
        frame2=[108,105,114,107,107,97,149,149,144,135,104,106]
        S_frame=0
        i=0
        j=0
        x = 80
        cheak=0
        while(cheak<12):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #플레이어
                ReimuSkill1.clip_draw(frame[i],110,frame2[j],110,Player_X,All_Y)
                ReimuSkill1effect.clip_draw(S_frame *70,0,80,110,Player_X+x,All_Y)
                #적
                ReimuSkill1.clip_draw(frame[i],0,frame2[j],110,Enemy_X,All_Y)
                ReimuSkill1effect.clip_draw(S_frame *70,0,80,110,Enemy_X-x,All_Y)
                
                i=(i+1)%13
                j=(j+1)%12
                S_frame=(S_frame+1)%13
                x=x+30
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
    Reimu_Skill1()

close_canvas()
