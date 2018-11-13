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
character = None
Enemycharacter=None
Enemycharacter=None
Deckcheak1=0
Deck1=0
Deckcheak2=0
mouse_x,mouse_y=0,0
PlayerDeck=[0,0,0,0,0,0,0,0,0,0,0,0]
temp=0
def shuffle():
    global PlayerDeck,temp

    for i in range(0,11):
        PlayerDeck[i]=DeckSelection.Decklist[i]

    for i in range(0,50):
        s1=random.randint(0,11)
        s2=random.randint(0,11)

        temp = PlayerDeck[s1]
        PlayerDeck[s1]=PlayerDeck[s2]
        PlayerDeck[s2]=temp


class PlayDeck:
    def __init__(self):
        shuffle()
        self.x, self.y = 300, 100
        self.ikuDeck= load_image('IkuSpellCard.png')
    def update(self):
        pass

    def draw(self):
        self.ikuDeck.clip_draw(45, 0, 45, 65, self.x, self.y)


    def handle_event(self, event):
        pass