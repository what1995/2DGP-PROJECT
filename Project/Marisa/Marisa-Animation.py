from pico2d import *


class BackGround:
    def __init__(self):
        self.x, self.y = 400, 300
        self.Shrine = load_image('Hakurei Shrine.png')

    def draw(self):
        self.Shrine.draw(self.x,self.y)

class Marisa:
    def __init__(self):
        self.Player = 200
        self.Enemy =600
        self.All_Y=200

        self.Dmage = load_image('MarisaDamage-Motion.png')
        self.Dmagei = 0
        self.Dmagej = 0
        self.Dmagecheak = 0

        self.Down = load_image('MarisaDown-Motion.png')
        self.Downi = 0
        self.Downj = 0
        self.Downcheak = 0

        self.Skill1 = load_image('MarisaSkill1-Motion.png')
        self.Skill1i =0
        self.Skill1j =0
        self.Skill1cheak=0
        self.S1Effect = load_image('MarisaSkill1.png')
        self.Skill1Ei = 0
        self.Skill1Ej = 0
        self.Skill1Eframe1 = 0

        self.Skill2 = load_image('MarisaSkill2-Motion.png')
        self.Skill2i = 0
        self.Skill2j = 0
        self.Skill2cheak=0
        self.S2Effect = load_image('MarisaSkill2.png')
        self.Skill2Ex1 = 120
        self.Skill2Ex2 = 100
        self.Skill2Ex3 = 80


        self.Skill3 = load_image('MarisaSkill3-Motion.png')
        self.Skill3i = 0
        self.Skill3j = 0
        self.Skill3cheak = 0
        self.S3Effect = load_image('MarisaSKill3.png')
        self.Skill3Eframe1 =0
        self.Skill3Ex1 = 120


        self.Lastspell = load_image('MarisaLastspell-Motion.png')
        self.Lastspelli =0
        self.Lastspellj=0
        self.Lastspellcheak=0
        self.LastspellEffect = load_image('MarisaLastspell.png')
        self.LastspellEframe1 =0

        self.Standing = load_image('MarisaStanding-Motion.png')
        self.Standi = 0
        self.Standj = 0
        self.Standcheak =0


    def update(self):
       pass


    def Damage(self):
        self.DamageFlame1 = [0, 90, 175, 240]
        self.DamageFlame2 = [90, 85, 65]
        #플레이어
        self.Dmage.clip_draw(self.DamageFlame1[self.Dmagei], 115, self.DamageFlame2[self.Dmagej],115,self.Player,self.All_Y)
        #적
        self.Dmage.clip_draw(self.DamageFlame1[self.Dmagei], 0, self.DamageFlame2[self.Dmagej], 115, self.Enemy, self.All_Y)
        if self.Dmagecheak <3:
            self.Dmagei = (self.Dmagei + 1) % 4
            self.Dmagej = (self.Dmagej + 1) % 3
            self.Dmagecheak += 1
        if self.Dmagecheak ==3:
            self.Dmagei = 0
            self.Dmagej = 0
            self.Dmagecheak=0

    def Downs(self):
        self.Downframe1 = [0,80,149,232,348,451,548,645]
        self.Downframe2 = [80,69,83,116,102,95,100]

        #플레이어
        self.Down.clip_draw(self.Downframe1[self.Downi], 95, self.Downframe2[self.Downj], 95, self.Player, self.All_Y-20)
        #적
        self.Down.clip_draw(self.Downframe1[self.Downi], 0, self.Downframe2[self.Downj], 95, self.Enemy, self.All_Y - 20)

        if self.Downcheak <7:
            self.Downi = (self.Downi + 1) % 8
            self.Downj = (self.Downj + 1) % 7
            self.Downcheak += 1
        if self.Downcheak ==7:
            self.Downi = 0
            self.Downj = 0
            self.Downcheak=0

    def Stand(self):
        self.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
        self.Standframe2 = [65,61,62,62,62,60,62,61,60,62]
        #플레이어
        self.Standing.clip_draw(self.Standframe1[self.Standi], 110, self.Standframe2[self.Standj], 110, self.Player,self.All_Y )
        #적
        self.Standing.clip_draw(self.Standframe1[self.Standi], 0, self.Standframe2[self.Standj], 110, self.Enemy,self.All_Y)

        if self.Standcheak < 10:
            self.Standi = (self.Standi+1) % 11
            self.Standj = (self.Standj+1) % 10
            self.Standcheak += 1
        if self.Standcheak == 9:
            self.Standi = 0
            self.Standj= 0
            self.Standcheak = 0

    def MSkill1(self):
        self.Skill1frame1 =[0, 71, 132, 197, 262, 322, 396, 468, 536, 600]
        self.Skill1frame2 =[71,61,65,65,58,72,72,66,60]
        #플레이어
        self.Skill1.clip_draw(self.Skill1frame1[self.Skill1i], 105, self.Skill1frame2[self.Skill1j], 105, self.Player,self.All_Y)
        #적
        self.Skill1.clip_draw(self.Skill1frame1[self.Skill1i], 0, self.Skill1frame2[self.Skill1j], 105, self.Enemy,self.All_Y)

        if self.Skill1cheak < 18:
            if self.Skill1cheak < 6:
                self.Skill1i = (self.Skill1i + 1) % 10
                self.Skill1j = (self.Skill1j + 1) % 9
            if self.Skill1cheak > 6:
                #Player
                self.S1Effect.clip_draw(self.Skill1Eframe1 * 260, 0, 260, 505, self.Enemy, self.All_Y+150)
                #Enemy
                self.S1Effect.clip_draw(self.Skill1Eframe1 * 260, 0, 260, 505, self.Player, self.All_Y + 150)
                if self.Skill1cheak < 15:
                    self.Skill1Eframe1 = (self.Skill1Eframe1 + 1) % 9
                if self.Skill1cheak >= 15:
                    self.Skill1i = (self.Skill1i + 1) % 10
                    self.Skill1j = (self.Skill1j + 1) % 9
            self.Skill1cheak += 1

        if self.Skill1cheak == 18:
            self.Skill1i =0
            self.Skill1j =0
            self.Skill1cheak=0
            self.Skill1Eframe1=0

    def MSkill2(self):
        self.Skill2frame1 = [0, 85, 165, 240, 318, 395, 464, 525]
        self.Skill2frame2 = [85, 80, 75, 78, 76, 67, 64]

        # 플레이어
        self.Skill2.clip_draw(self.Skill2frame1[self.Skill2i], 120, self.Skill2frame2[self.Skill2j], 120, self.Player,self.All_Y)
        # 적
        self.Skill2.clip_draw(self.Skill2frame1[self.Skill2i], 0, self.Skill2frame2[self.Skill2j], 120, self.Enemy,self.All_Y)

        if self.Skill2cheak < 7:
            self.Skill2i = (self.Skill2i + 1) % 8
            self.Skill2j = (self.Skill2j + 1) % 7
            #Player
            self.S2Effect.clip_draw(0, 125, 132, 125, self.Player + self.Skill2Ex1, self.All_Y)
            self.S2Effect.clip_draw(132, 125, 132, 125, self.Player + self.Skill2Ex2, self.All_Y)
            self.S2Effect.clip_draw(264, 125, 132, 125, self.Player + self.Skill2Ex3, self.All_Y)
            #Enemy
            self.S2Effect.clip_draw(0, 0, 132, 125, self.Enemy - self.Skill2Ex1, self.All_Y)
            self.S2Effect.clip_draw(132, 0, 132, 125, self.Enemy - self.Skill2Ex2, self.All_Y)
            self.S2Effect.clip_draw(264, 0, 132, 125, self.Enemy - self.Skill2Ex3, self.All_Y)
            self.Skill2Ex1 += 75
            self.Skill2Ex2 += 75
            self.Skill2Ex3 += 75
            self.Skill2cheak += 1

        if self.Skill2cheak == 7:
            self.Skill2i = 0
            self.Skill2j = 0
            self.Skill2Ex1 = 120
            self.Skill2Ex2 = 100
            self.Skill2Ex3 = 80
            self.Skill2cheak =0

    def MSkill3(self):
        self.Skill3frame1 = [0, 65,125,195,275,332,412,500,590,661]
        self.Skill3frame2 = [65,60,70,80,60,76,85,89,68,61]

        # 플레이어
        self.Skill3.clip_draw(self.Skill3frame1[self.Skill3i], 110, self.Skill3frame2[self.Skill3j], 110, self.Player,self.All_Y)
        # 적
        self.Skill3.clip_draw(self.Skill3frame1[self.Skill3i], 0, self.Skill3frame2[self.Skill3j], 110, self.Enemy,self.All_Y)

        if self.Skill3cheak < 17:
            if self.Skill3cheak<7:
                self.Skill3i = (self.Skill3i + 1) % 10
                self.Skill3j = (self.Skill3j + 1) % 10
            if self.Skill3cheak>=7:
                self.S3Effect.clip_draw(self.Skill3Eframe1*260, 255, 260, 255, self.Player + self.Skill3Ex1, self.All_Y)
                self.Skill3Eframe1 = (self.Skill3Eframe1+1)%3
                self.Skill3Ex1 += 80
            if self.Skill3cheak >=13:
                self.Skill3i = (self.Skill3i + 1) % 10
                self.Skill3j = (self.Skill3j + 1) % 10
            self.Skill3cheak += 1

        if self.Skill3cheak == 17:
            self.Skill3i = 0
            self.Skill3j = 0
            self.Skill3Ex1= 120
            self.Skill3cheak = 0

    def MLastspell(self):
        self.Lastframe1 = [0, 65,127,187,251,305,386,451,536,610,680,750,815,880,943,1010,1070]
        self.Lastframe2 = [65,62,60,64,55,79,62,80,72,66,66,65,63,60,59,58,58]

        # 플레이어
        self.Lastspell.clip_draw(self.Lastframe1[self.Lastspelli], 120, self.Lastframe2[self.Lastspellj], 120, self.Player+250,self.All_Y)
        # 적
        self.Lastspell.clip_draw(self.Lastframe1[self.Lastspelli], 0, self.Lastframe2[self.Lastspellj], 120, self.Enemy-250,self.All_Y)

        if self.Lastspellcheak < 18:
            self.Lastspelli = (self.Lastspelli + 1) % 17
            self.Lastspellj = (self.Lastspellj + 1) % 17
            if self.Lastspellcheak > 4:
                if self.Lastspellcheak < 11:
                    #Player
                    self.LastspellEffect.clip_draw(self.LastspellEframe1 * 261, 250, 260, 250, self.Player + 400,self.All_Y-10)
                    #Enemy
                    self.LastspellEffect.clip_draw(self.LastspellEframe1 * 261, 0, 260, 250, self.Enemy - 400, self.All_Y )
                    self.LastspellEframe1=(self.LastspellEframe1+1)%7
            self.Lastspellcheak += 1

        if self.Lastspellcheak == 18:
            self.Lastspelli = 0
            self.Lastspellj = 0
            self.Lastspellcheak = 0






def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False




open_canvas()
background=BackGround()
marisa=Marisa()
running=True

while running:
    handle_events()
    clear_canvas()
    background.draw()
    marisa.update()
    #marisa.Damage()
    #marisa.Downs()
    #marisa.Stand()
    #marisa.MSkill1()
    #marisa.MSkill2()
    #marisa.MSkill3()
    marisa.MLastspell()
    update_canvas()
    delay(0.1)
# finalization code
close_canvas()
