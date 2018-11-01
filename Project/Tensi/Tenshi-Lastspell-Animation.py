from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
TenshiLastspell = load_image('TenshiLastspell-Motion.png')
TenshiLastspelleffect = load_image('TenshiLastspell1-1.png')
TenshiLastspelleffect2 = load_image('TenshiLastspell1-2.png')


def Tenshi_Lastspell():
        frame1 = [72,70,124,169,142,137,124,85,132,131,124,96,109,95,145,167,155,150,90,72]
        frame2 = [0,72,142,266,435,577,715,842,928,1064,1200,1328,1430,1540,1640,1790,1965,2130,2295,2395,2465]
        cheak=0
        S_frame=0
        i=0
        j=0
        while(cheak<20):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiLastspell.clip_draw(frame2[i],0,frame1[j],165,Enemy_X-200,All_Y)
                #플레이어
                TenshiLastspell.clip_draw(frame2[i],165,frame1[j],165,Player_X+200,All_Y)
                i=(i+1)%21
                j=(j+1)%20
                if cheak >3:
                    #플레이어
                    TenshiLastspelleffect2.clip_draw(0,0,250,250,Enemy_X,All_Y)
                    #적
                    TenshiLastspelleffect2.clip_draw(0,0,250,250,Player_X,All_Y)
                    if cheak >4:
                        #플레이어
                        TenshiLastspelleffect.clip_draw(S_frame*260,0,260,250,Enemy_X,All_Y)
                        #적
                        TenshiLastspelleffect.clip_draw(S_frame*260,0,260,250,Player_X,All_Y)
                        if cheak ==9:
                            S_frame +=1
                        if cheak ==15:
                            S_frame +=1
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Lastspell()


close_canvas()
        
