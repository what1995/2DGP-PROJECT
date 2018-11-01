from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =400
Enemy_X=400
All_Y=200
TenshiSkill3 = load_image('TenshiSkill3-Motion.png')
TenshiSkill3effect = load_image('TenshiSkill3.png')


def Tenshi_Skill3():
        frame1 = [77,78,83,99,80,98,178,160,70,70,63,68]
        frame2 = [0,77,155,240,340,425,528,710,876,960,1040,1110,1190]
        cheak=0
        i=0
        j=0
        frame=0
        while(cheak<13):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiSkill3.clip_draw(frame2[i],0,frame1[j],115,Enemy_X,All_Y)
                #플레이어
                TenshiSkill3.clip_draw(frame2[i],115,frame1[j],115,Player_X,All_Y)
                if cheak <11:
                    i=(i+1)%13
                    j=(j+1)%12
                if cheak >6:
                    #플레이어
                    TenshiSkill3effect.clip_draw(frame*260,107,260,120,Player_X+150,All_Y-10)
                    #적
                    TenshiSkill3effect.clip_draw(frame*260,0,260,107,Enemy_X-150,All_Y)
                    frame= (frame+1)%7
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Skill3()


close_canvas()
        
