import game_framework
import random
from pico2d import *
import CharacterSelection
import DeckSelection
import main_state
import os

os.chdir('C:\\2DGP\\2015180012-2DGP-PROJECT\\2DGP-PROJECT\\Project\\FCGimage')
#import CharacterSelection
import game_world

name = "deck"
image = None
next = None
Enemycharacter=None
Enemycharacter=None
mouse_x,mouse_y=0,0
PlayerDeck=[0,0,0,0,0,0,0,0,0,0,0,0]
temp=0
s1=0
s2=0
def shuffle():
    global PlayerDeck,temp,s1,s2

    for i in range(0,12):
        PlayerDeck[i]=DeckSelection.Decklist[i]

    for s in range(0,50):
        s1 = random.randint(0, 11)
        s2 = random.randint(0, 11)

        temp = PlayerDeck[s1]
        PlayerDeck[s1] = PlayerDeck[s2]
        PlayerDeck[s2] = temp


class PlayDeck:
    def __init__(self):
        shuffle()
        self.x, self.y = 100, 100
        self.ikuDeck= load_image('IkuSpellCard.png')
        self.reimuDeck= load_image('RimuSpellCard.png')
        self.marisaDeck= load_image('MarisaSpellCard.png')
        self.tenshiDeck= load_image('TenshiSpellCard.png')
        self.Deckimage=load_image('Deck.png')
    def update(self):
        pass

    def draw(self):
        if CharacterSelection.character==0:
            for i in range(0,12):
                if PlayerDeck[i]==1:
                    self.reimuDeck.clip_draw(0, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==2:
                    self.reimuDeck.clip_draw(45, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==3:
                    self.reimuDeck.clip_draw(90, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==4:
                    self.reimuDeck.clip_draw(135, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==5:
                    self.reimuDeck.clip_draw(0, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==6:
                    self.reimuDeck.clip_draw(45, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==7:
                    self.reimuDeck.clip_draw(90, 65, 45, 65, self.x+(50*i), self.y)
        if CharacterSelection.character==1:
            for i in range(0,12):
                if PlayerDeck[i]==1:
                    self.marisaDeck.clip_draw(0, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==2:
                    self.marisaDeck.clip_draw(45, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==3:
                    self.marisaDeck.clip_draw(90, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==4:
                    self.marisaDeck.clip_draw(135, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==5:
                    self.marisaDeck.clip_draw(0, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==6:
                    self.marisaDeck.clip_draw(45, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==7:
                    self.marisaDeck.clip_draw(90, 65, 45, 65, self.x+(50*i), self.y)
        if CharacterSelection.character==2:
            for i in range(0,12):
                if PlayerDeck[i]==1:
                    self.Deckimage.draw(self.x + (50 * i), self.y)
                    self.ikuDeck.clip_draw(0, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==2:
                    self.ikuDeck.clip_draw(45, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==3:
                    self.ikuDeck.clip_draw(90, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==4:
                    self.ikuDeck.clip_draw(135, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==5:
                    self.ikuDeck.clip_draw(0, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==6:
                    self.ikuDeck.clip_draw(45, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==7:
                    self.ikuDeck.clip_draw(90, 65, 45, 65, self.x+(50*i), self.y)

        if CharacterSelection.character==3:
            for i in range(0,12):
                if PlayerDeck[i]==1:
                    self.tenshiDeck.clip_draw(0, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==2:
                    self.tenshiDeck.clip_draw(45, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==3:
                    self.tenshiDeck.clip_draw(90, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==4:
                    self.tenshiDeck.clip_draw(135, 0, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==5:
                    self.tenshiDeck.clip_draw(0, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==6:
                    self.tenshiDeck.clip_draw(45, 65, 45, 65, self.x+(50*i), self.y)
                if PlayerDeck[i]==7:
                    self.tenshiDeck.clip_draw(90, 65, 45, 65, self.x+(50*i), self.y)


    def handle_event(self, event):
        pass