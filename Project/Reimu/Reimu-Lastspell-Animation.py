from pico2d import *

open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200

ReimuLastSpell = load_image('Reimu-Last Spell-Motion.png')
ReimuLastSpelleffect1 = load_image('Reimu-Lastspell1.png')
ReimuLastSpelleffect2 = load_image('Reimu-Lastspell2-1.png')
ReimuLastSpelleffect3 = load_image('Reimu-Lastspell3-2.png')


def Reimu_LastSpell():
        frame=[0,105, 209,311,414, 517, 620, 724, 822, 910, 995,1068,1145,1242,1345,1445]
        frame2=[105,104,102,103,104,103,104,98,88,85,74,77,97,103,100]
        PSx = [580, 620, 600]
        SSy = [160.175,200,225,250]
        ESx = [180,220,200]
        
        i=0
        j=0
        c=0
        d=0
        cheak=0
        S_frame=0
        S1_frame=0
        S2_frame=0
        while(cheak<22):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #플레이어
                ReimuLastSpell.clip_draw(frame[i],130,frame2[j],130,Player_X,All_Y)
                #적
                ReimuLastSpell.clip_draw(frame[i],0,frame2[j],130,Enemy_X,All_Y)
                if (cheak<9):
                   i=(i+1)%16
                   j=(j+1)%15
                if cheak>=9:
                    if cheak<14:
                        #플레이어 공격
                        ReimuLastSpelleffect1.clip_draw(S_frame *133,0,133,207,Enemy_X,230)
                        ReimuLastSpelleffect2.clip_draw(S1_frame *261,0,262,126,Enemy_X-10,160)
                        ReimuLastSpelleffect3.clip_draw(S2_frame *133,0,133,126,PSx[c],SSy[d])
                        #적 공격
                        ReimuLastSpelleffect1.clip_draw(S_frame *133,0,133,207,Player_X,230)
                        ReimuLastSpelleffect2.clip_draw(S1_frame *261,0,262,126,Player_X-10,160)
                        ReimuLastSpelleffect3.clip_draw(S2_frame *133,0,133,126,ESx[c],SSy[d])
                        c =(c+1)%2
                        d=(d+1)%4
                if cheak>=16:
                    
                    i=(i+1)%16
                    j=(j+1)%15
                
                S_frame=(S_frame+1)%13
                S1_frame=(S1_frame+1)%8
                S2_frame=(S1_frame+1)%3
                update_canvas()
                
                delay(0.1)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Reimu_LastSpell()

close_canvas()
