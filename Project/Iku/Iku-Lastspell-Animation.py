from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
IkuLastspell = load_image('IkuLastspell-Motion.png')
IkuLastspelleffect1 = load_image('IkuLastspell1-1.png')
IkuLastspelleffect2 = load_image('IkuLastspell1-2.png')


def Iku_Lastspell():
        frame1 = [60,60,60,63,72,125,130,130,125,120]
        frame2 = [0,60,120,180,243,315,440,570,700,825,945,1035]
        cheak=0
        S_frame=0
        S2_frame1=[120,75]
        S2_frame2=[0,120,75]
        i=0
        j=0
        s=0
        c=0
        while(cheak<19):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                IkuLastspell.clip_draw(frame2[i],0,frame1[j],140,Enemy_X,All_Y)
                #플레이어
                IkuLastspell.clip_draw(frame2[i],140,frame1[j],140,Player_X,All_Y)
                if cheak<8:
                    i=(i+1)%10
                    j=(j+1)%9
                if cheak>=8:
                    #플레이어
                    IkuLastspelleffect2.clip_draw(S2_frame2[(s+1)%2],0,S2_frame1[c],255,Enemy_X-50,All_Y+70)
                    IkuLastspelleffect2.clip_draw(S2_frame2[(s+1)%2],0,S2_frame1[c],255,Enemy_X+40,All_Y+70)
                    IkuLastspelleffect2.clip_draw(S2_frame2[s],0,S2_frame1[c],255,Enemy_X,All_Y+70)
                    IkuLastspelleffect1.clip_draw(S_frame *270,0,270,255,Enemy_X+15,All_Y+210)
                    #적
                    #IkuLastspelleffect2.clip_draw(S2_frame2[(s+1)%2],0,S2_frame1[c],255,Player_X+50,All_Y+70)
                    #IkuLastspelleffect2.clip_draw(S2_frame2[(s+1)%2],0,S2_frame1[c],255,Player_X-40,All_Y+70)
                    #IkuLastspelleffect2.clip_draw(S2_frame2[s],0,S2_frame1[c],255,Player_X,All_Y+70)
                    #IkuLastspelleffect1.clip_draw(S_frame *270,0,270,255,Player_X+25,All_Y+210)
                    S_frame= (S_frame+1)%4
                    s=(s+1)%2
                    c=(c+1)%1
                if cheak>=16:
                    i=(i+1)%10
                    j=(j+1)%10
                update_canvas()
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Iku_Lastspell()


close_canvas()
        
