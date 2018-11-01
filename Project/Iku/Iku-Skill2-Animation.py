from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuSkill2 = load_image('IkuSkill2-Motion.png')
IkuSkill2effect = load_image('IkuSkill2-1.png')

def Iku_Skill2():
        frame1 = [70,60,70,83,73,66,66,101,133,178,173,157,124,83,63]
        frame2 = [0,70,130,200,283,356,422,490,597,732,912,1087,1247,1375,1463,1520]
        cheak=0
        Px=300
        Ex=320
        S_frame=0
        S_Px=330
        S_Ex=365
        i=0
        j=0
        while(cheak<19):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuSkill2.clip_draw(frame2[i],0,frame1[j],145,Enemy_X-Ex,All_Y)
                #플레이어
                IkuSkill2.clip_draw(frame2[i],145,frame1[j],145,Player_X+Px,All_Y)
                
                if cheak<11:
                    i=(i+1)%16
                    j=(j+1)%15
                if cheak>5:
                    if(cheak<15):
                        if cheak>8:
                            #플레이어
                            IkuSkill2effect.clip_draw(S_frame *193,60,193,60,Player_X+S_Px,All_Y-5)
                            #적
                            IkuSkill2effect.clip_draw(S_frame *193,0,193,60,Enemy_X-S_Ex,All_Y-5)
                            S_Px += 10
                            S_Ex += 10
                        Px += 10
                        Ex += 10
                        
                if cheak>=15:
                    i=(i+1)%16
                    j=(j+1)%15
                    Px -= 10
                    Ex -= 10
                S_frame=(S_frame+1)%6
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Skill2()


close_canvas()
        
