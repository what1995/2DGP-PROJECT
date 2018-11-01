from pico2d import *
open_canvas()
BgShrine = load_image('Hakurei Shrine.png')
Player_X =200
Enemy_X=600
All_Y=200
TenshiDamage = load_image('TenshiDamage-Motion.png')


def Tenshi_Damage():
        frame=0
        cheak=0
        while(cheak<5):
                clear_canvas()
                BgShrine.clip_draw(0,0,800,600,400,300)
                #적
                TenshiDamage.clip_draw(frame*80,0,78,115,Enemy_X,All_Y)
                #플레이어
                TenshiDamage.clip_draw(frame*80,115,78,115,Player_X,All_Y)
                frame=(frame+1)%5
                update_canvas()
                delay(0.13)
                cheak +=1


while(True):
        BgShrine.clip_draw(0,0,800,600,400,300)
        Tenshi_Damage()


close_canvas()
        
