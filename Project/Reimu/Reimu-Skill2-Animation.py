from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
ReimuSkill2 = load_image('Reimu-Skill2-Motion.png')
ReimuSkill2effect = load_image('Reimu-Skill2.png')


def Reimu_Skill2():
        frame=[0,66,120,217,304,392,480,572,675]
        frame2=[66,54,97,87,88,88,92,103]
        i=0
        j=0
        cheak=0
        S_frame=0
        while(cheak<8):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                ReimuSkill2.clip_draw(frame[i],0,frame2[j],120,Enemy_X,200)
                #플레이어
                ReimuSkill2.clip_draw(frame[i],155,frame2[j],120,Player_X,200)
                #적스킬
                ReimuSkill2effect.clip_draw(S_frame *133,0,134,255,Player_X,260)
                #플레이어 스킬
                ReimuSkill2effect.clip_draw(S_frame *133,0,134,255,Enemy_X,260)
                i=(i+1)%9
                j=(j+1)%8
                S_frame=(S_frame+1)%8
                update_canvas()
                delay(0.1)
                cheak +=1

while(True):
    Reimu_Skill2()

close_canvas()
