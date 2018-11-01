from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
TenshiSkill2 = load_image('TenshiSkill2-Motion.png')
TenshiSkill2effect = load_image('TenshiSkill2-1.png')


def Tenshi_Skill2():
        frame1 = [70,79,79,77,73,69,68,67,70,69,66,69,66,60,60]
        frame2 = [0,70,149,228,305,378,448,520,590,664,740,814,888,960,1026,1100]
        cheak=0
        frame=0
        i=0
        j=0
        Px1=75
        Px2=75
        Px3=75
        while(cheak<21):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiSkill2.clip_draw(frame2[i],0,frame1[j],115,Enemy_X,All_Y)
                #플레이어
                TenshiSkill2.clip_draw(frame2[i],115,frame1[j],115,Player_X,All_Y)
                if cheak<10:
                    i=(i+1)%16
                    j=(j+1)%15
                if cheak>=10:
                    #플레이어
                    TenshiSkill2effect.clip_draw(0,frame*50,70,50,Player_X+Px1,All_Y)
                    TenshiSkill2effect.clip_draw(0,frame*50,70,50,Player_X+Px2,All_Y+25)
                    TenshiSkill2effect.clip_draw(0,frame*50,70,50,Player_X+Px3,All_Y-25)
                    #적
                    TenshiSkill2effect.clip_draw(70,frame*50,70,50,Enemy_X-Px1,All_Y)
                    TenshiSkill2effect.clip_draw(70,frame*50,70,50,Enemy_X-Px2,All_Y+25)
                    TenshiSkill2effect.clip_draw(70,frame*50,70,50,Enemy_X-Px3,All_Y-25)
                    frame=(frame+1)%3
                    if cheak <21:
                        Px1 += 50
                        Px2 += 75
                        Px3 += 90
                    if cheak >=16:
                        i=(i+1)%16
                        j=(j+1)%15
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Skill2()


close_canvas()
        
