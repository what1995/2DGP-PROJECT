from pico2d import *
import Player

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
        self.stat =1

        self.MStanding = load_image('MarisaStanding-Motion.png')
        self.Standi = 0
        self.Standj = 0
        self.Standcheak =0

        self.MLastspell = load_image('MarisaLastspell-Motion.png')
        self.Lastspelli = 0
        self.Lastspellj = 0
        self.Lastspellcheak = 0
        self.MLastspellEffect = load_image('MarisaLastspell.png')
        self.LastspellEframe1 = 0

    def update(self):
        if self.stat==0:
            if self.Standcheak < 10:
                self.Standi = (self.Standi+1) % 11
                self.Standj = (self.Standj+1) % 10
                self.Standcheak += 1
            if self.Standcheak == 9:
                self.Standi = 0
                self.Standj= 0
                self.Standcheak = 0
        if self.stat==1:
            if self.Lastspellcheak < 18:
                self.Lastspelli = (self.Lastspelli + 1) % 17
                self.Lastspellj = (self.Lastspellj + 1) % 17
                if self.Lastspellcheak > 4:
                    if self.Lastspellcheak < 11:
                        # Player
                        self.MLastspellEffect.clip_draw(self.LastspellEframe1 * 261, 250, 260, 250, self.Player + 400,
                                                       self.All_Y - 10)
                        # Enemy
                     #   self.LastspellEffect.clip_draw(self.LastspellEframe1 * 261, 0, 260, 250, self.Enemy - 400,self.All_Y)
                        self.MLastspellEframe1 = (self.LastspellEframe1 + 1) % 7
                self.Lastspellcheak += 1

            if self.Lastspellcheak == 18:
                self.Lastspelli = 0
                self.Lastspellj = 0
                self.Lastspellcheak = 0
                marisa.stat = 0



    def Stand(self):
        if self.stat==0:
            self.Standframe1 = [0,65,126,188,250,312,372,434,495,556,618]
            self.Standframe2 = [65,61,62,62,62,60,62,61,60,62]
          #플레이어
            self.MStanding.clip_draw(self.Standframe1[self.Standi], 110, self.Standframe2[self.Standj], 110, self.Player,self.All_Y )
          #적
         #   self.Standing.clip_draw(self.Standframe1[self.Standi], 0, self.Standframe2[self.Standj], 110, self.Enemy,self.All_Y)

        if self.stat == 1:
            self.Lastframe1 = [0, 65,127,187,251,305,386,451,536,610,680,750,815,880,943,1010,1070]
            self.Lastframe2 = [65,62,60,64,55,79,62,80,72,66,66,65,63,60,59,58,58]

        # 플레이어
            self.MLastspell.clip_draw(self.Lastframe1[self.Lastspelli], 120, self.Lastframe2[self.Lastspellj], 120, self.Player+250,self.All_Y)
        # 적
         #   self.Lastspell.clip_draw(self.Lastframe1[self.Lastspelli], 0, self.Lastframe2[self.Lastspellj], 120, self.Enemy-250,self.All_Y)



class Enemy:
    def __init__(self):
        self.Enemy = 600
        self.All_Y = 200
        self.stat = 0


        self.Standing = load_image('MarisaStanding-Motion.png')
        self.Standi = 0
        self.Standj = 0
        self.Standcheak = 0

        self.Lastspell = load_image('MarisaLastspell-Motion.png')
        self.Lastspelli = 0
        self.Lastspellj = 0
        self.Lastspellcheak = 0
        self.LastspellEffect = load_image('MarisaLastspell.png')
        self.LastspellEframe1 = 0

    def update(self):
        if self.stat == 0:

            if self.Standcheak < 10:
                self.Standi = (self.Standi + 1) % 11
                self.Standj = (self.Standj + 1) % 10
                self.Standcheak += 1
            if self.Standcheak == 9:
                self.Standi = 0
                self.Standj = 0
                self.Standcheak = 0
        if self.stat == 1:
            if self.Lastspellcheak < 18:
                self.Lastspelli = (self.Lastspelli + 1) % 17
                self.Lastspellj = (self.Lastspellj + 1) % 17
                if self.Lastspellcheak > 4:
                    if self.Lastspellcheak < 11:

                            # Enemy
                        self.LastspellEffect.clip_draw(self.LastspellEframe1 * 261, 0, 260, 250, self.Enemy - 400,self.All_Y)
                        self.LastspellEframe1 = (self.LastspellEframe1 + 1) % 7
                self.Lastspellcheak += 1

            if self.Lastspellcheak == 18:
                self.Lastspelli = 0
                self.Lastspellj = 0
                self.Lastspellcheak = 0
                enemy.stat = 0

    def Stand(self):
        if self.stat == 0:
            self.Standframe1 = [0, 65, 126, 188, 250, 312, 372, 434, 495, 556, 618]
            self.Standframe2 = [65, 61, 62, 62, 62, 60, 62, 61, 60, 62]

                # 적
            self.Standing.clip_draw(self.Standframe1[self.Standi], 0, self.Standframe2[self.Standj], 110,self.Enemy, self.All_Y)

        if self.stat == 1:
            self.Lastframe1 = [0, 65, 127, 187, 251, 305, 386, 451, 536, 610, 680, 750, 815, 880, 943, 1010, 1070]
            self.Lastframe2 = [65, 62, 60, 64, 55, 79, 62, 80, 72, 66, 66, 65, 63, 60, 59, 58, 58]


                # 적
            self.Lastspell.clip_draw(self.Lastframe1[self.Lastspelli], 0, self.Lastframe2[self.Lastspellj], 120,self.Enemy - 250, self.All_Y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            marisa.stat =1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_a:
            enemy.stat = 1


open_canvas()
background=BackGround()
marisa=Marisa()
enemy=Enemy()
running=True

while running:

    handle_events()
    clear_canvas()
    #background.draw()
    #marisa.update()
    #enemy.update()
    #marisa.Stand()
    Player.Player.Stand(Player)
    #enemy.Stand()

    update_canvas()
    delay(0.1)
# finalization code
close_canvas()
