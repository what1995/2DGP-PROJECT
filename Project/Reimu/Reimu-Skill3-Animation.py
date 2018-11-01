from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200

ReimuSkill3 = load_image('Reimu-Skill3-Motion.png')
ReimuSkill3effect = load_image('Reimu-Skill3.png')


def Reimu_Skill3():
        frame=[0,105, 210,315,420, 543, 659, 775, 885, 1000,1100]
        frame2=[104,105,105,104,120,115,115,108,115,100]
        i=0
        j=0
        Px=70
        Ex=70
        S3_frame=0
        cheak=0
        
        while(cheak<24):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #플레이어
                ReimuSkill3.clip_draw(frame[i],100,frame2[j],100,Player_X,All_Y)
                #적
                ReimuSkill3.clip_draw(frame[i],0,frame2[j],100,Enemy_X,All_Y)
                
                
                if(cheak<5):
                    i=(i+1)%11
                    j=(j+1)%10
                if(cheak>=5):
                    #플레이어 공격
                    ReimuSkill3effect.clip_draw(S3_frame*117,0,117,100,Player_X+Px,All_Y)
                    Px=Px+20
                    if(cheak>=20):
                        i=(i+1)%11
                        j=(j+1)%10
                    #적 공격
                    ReimuSkill3effect.clip_draw(S3_frame*117,0,117,100,Enemy_X-Ex,All_Y)
                    Ex=Ex+20
                    if(cheak>=20):
                        i=(i+1)%11
                        j=(j+1)%10
                    
                
                update_canvas()
                
                delay(0.1)
                cheak +=1



while(True):
    Reimu_Skill3()    


close_canvas()
