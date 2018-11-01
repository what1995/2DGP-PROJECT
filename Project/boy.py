from pico2d import *

# Boy Event
# fill here
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP ,DASH_DOWN,DASH_UP,Stand= range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_a): DASH_DOWN,
    (SDL_KEYUP, SDLK_a): DASH_UP,

}



# Boy States
class IdleState:
    @staticmethod
    def enter(boy):
        boy.frame1 = 0
        boy.frame2 = 0
        boy.Standframe1 = [0, 73, 140, 200, 265, 324, 385, 446, 510, 580]
        boy.Standframe2 = [74, 64, 60, 62, 58, 59, 63, 65, 70]
        boy.timer=1000

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        boy.frame1 = (boy.frame1 + 1) % 9
        boy.frame2 = (boy.frame2 + 1) % 9
        if boy.velocity==2:
            boy.add_event(RIGHT_DOWN)
        delay(0.1)

    @staticmethod
    def draw(boy):
        if boy.dir ==1:
            boy.stand.clip_draw(boy.Standframe1[boy.frame1], 130, boy.Standframe2[boy.frame2], 130, boy.x, boy.y)
        #else:
        #    boy.image.clip_draw(boy.frame * 100, 200, 100, 100, boy.x, boy.y)


class RunState:
    @staticmethod
    def enter(boy):
        boy.frame1=0
        boy.frame2=0
        boy.S1frame = 0
        boy.Skill1Eframe1 = 0
        boy.skill1cheak = 0
        boy.Standframe1 = [0,68,133,193,259,329,390,470,543,615,680,745]
        boy.Standframe2 = [68,65,60,66,68,59,78,74,70,63,68]
        #boy.dir = boy.velocity

    @staticmethod
    def exit(boy):
        pass

    @staticmethod
    def do(boy):
        if boy.skill1cheak<8:
            boy.frame1 = (boy.frame1 + 1) % 11
            boy.frame2 = (boy.frame2 + 1) % 11
        if boy.skill1cheak>=8 and boy.skill1cheak<20:
            boy.S1effect.clip_draw(0, boy.S1frame * 52, 360, 52, boy.x + 200, boy.y + 10)
            boy.S1effect2.clip_draw(boy.Skill1Eframe1 * 65, 0, 68, 60, 600 - 10, boy.y + 10)
            boy.S1frame = (boy.S1frame + 1) % 12
            boy.Skill1Eframe1 = (boy.Skill1Eframe1 + 1) % 7
        if boy.skill1cheak>=20:
            boy.frame1 = (boy.frame1 + 1) % 11
            boy.frame2 = (boy.frame2 + 1) % 11
        boy.skill1cheak +=1
        if  boy.skill1cheak==23:
            boy.skill1cheak=0
            boy.add_event(Stand)


        delay(0.1)
        #if boy.skill1cheak == 22:

        #boy.x += boy.velocity
        boy.x= clamp(25,boy.x,800-25)

    @staticmethod
    def draw(boy):
        if boy.velocity == 1:
            boy.skill1.clip_draw(boy.Standframe1[boy.frame1], 145, boy.Standframe2[boy.frame2], 145, boy.x, boy.y)
            if boy.skill1cheak >= 8 and boy.skill1cheak < 20:
                boy.S1effect.clip_draw(0, boy.S1frame * 52, 360, 52, boy.x + 200, boy.y + 10)
                boy.S1effect2.clip_draw(boy.Skill1Eframe1 * 65, 0, 68, 60, 600 - 10, boy.y + 10)



        #else:
        #    boy.image.clip_draw(boy.frame * 100, 0, 100, 100, boy.x, boy.y)


# fill here




next_state_table = {
    IdleState: {RIGHT_UP:RunState,LEFT_UP:RunState,RIGHT_DOWN:RunState,LEFT_DOWN:RunState,DASH_DOWN:RunState,DASH_UP:RunState},
    RunState:{RIGHT_UP:RunState,LEFT_UP:IdleState,LEFT_DOWN:IdleState,RIGHT_DOWN:IdleState,DASH_DOWN:IdleState,DASH_UP:IdleState,Stand:IdleState}
# fill here
}







class Boy:

    def __init__(self):
        self.x, self.y = 200, 200
        self.stand = load_image('Iku-Standing-Motion.png')
        self.skill1=load_image('IkuSkill1-Motion.png')
        self.S1effect = load_image('IkuSkill1-1.png')
        self.S1effect2 = load_image('IkuSkill1-2.png')
        self.dir = 1
        self.velocity = 0
        self.event_que = []
        self.cur_state=IdleState
        self.cur_state.enter(self)
        # fill here
        pass


    def change_state(self,  state):
        self.cur_state.exit(self)
        self.cur_state = state
        self.cur_state.enter(self)
        # fill here



    def add_event(self, event):
        self.event_que.insert(0,event)


    def update(self):
        self.cur_state.do(self)
        if len(self.event_que)>0:
            event=self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])




    def draw(self):
        self.cur_state.draw(self)


    def handle_event(self, event):
        if(event.type,event.key) in key_event_table:
            key_event = key_event_table[(event.type,event.key)]
            if key_event ==RIGHT_DOWN:
                self.velocity =1
            elif key_event ==LEFT_DOWN:
                self.velocity -=1
           # elif key_event == RIGHT_UP:
           #     self.velocity -=1
            elif key_event==LEFT_UP:
                self.velocity +=1
            elif key_event==DASH_DOWN:
                self.velocity -=5
            elif key_event == DASH_UP:
                self.velocity += 5
            self.add_event(key_event)
        if SDL_MOUSEBUTTONDOWN and SDL_BUTTON_LEFT:
            self.velocity = 2

