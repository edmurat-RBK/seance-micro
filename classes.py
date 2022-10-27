from enums import (
    ChapterType, 
    ActionCategory, 
    ActionRarity,
    CharacterClass
)

from csv import reader
from datetime import datetime
import random
from uuid import uuid4



class Playtest:
    def __init__(self):
        self.uuid = uuid4()
        self.start_time = datetime.now()
        self.game = Game()
        for _ in range(3):
            self.game.connect_player(Player())



class Player:
    players = {}
    
    def __init__(self):
        self.uuid = uuid4()
        Player.players[str(self.uuid)] = self



class Game:
    games = {}
    
    def __init__(self):
        self.uuid = uuid4()
        self.players = [None, None, None]
        Game.games[str(self.uuid)] = self
        self.chapters = ChapterDeck()
        
    def connect_player(self,player):
        for i in range(len(self.players)):
            if self.players[i] is None:
                self.players[i] = player
                break
    


class Avatar:
    def __init__(self,player,character_class):
        self.player = player
        
        if character_class == "Warrior":
            self.character_class = CharacterClass.WARRIOR
        elif character_class == "Mage":
            self.character_class = CharacterClass.MAGE
        elif character_class == "Ranger":
            self.character_class = CharacterClass.RANGER
        else:
            self.character_class = CharacterClass.UNDEFINED
        
        self.deck = ActionDeck()
        self.health = Dice(20,20)
        self.armor = Dice(20,0)



class ChapterDeck:
    def __init__(self):
        self.deck = []
        self.discard = []
        
    def build_deck(self):
        self.deck = [card for card in ChapterCard.chapters.values()]
        
    def shuffle_deck(self):
        random.shuffle(self.deck)
        
    def draw_next(self):
        if self.deck:
            next_chapter = self.deck.pop(0)
            self.discard.append(next_chapter)
            return next_chapter
        else:
            return None



class ChapterCard:
    chapters = {}
    
    def __init__(self,type,name):
        self.uuid = uuid4()
        ChapterCard.chapters[self.uuid] = self
        
        if type == "Encounter":
            self.type = ChapterType.ENCOUNTER
        elif type == "Event":
            self.type = ChapterType.EVENT
        else:
            self.type = ChapterType.UNDEFINED

        self.name = name
        
    def load_cards():
        with open("data/chapter_card_list.csv","r",encoding="utf-8") as csv_file:
            csv_reader = reader(csv_file)
            next(csv_reader)    # Skip headers
            for row in csv_reader:
                if row[1] == "Encounter":
                    EncounterCard(
                        row[2],
                        int(row[4]),
                        int(row[5]),
                        int(row[6])
                    )
                elif row[1] == "Event":
                    EventCard(row[2])



class EncounterCard(ChapterCard):
    def __init__(self,name,health,armor,strength):
        super().__init__("Encounter",name)
        self.health = health
        self.armor = armor
        self.strength = strength
        


class EventCard(ChapterCard):
    def __init__(self,name):
        super().__init__("Event",name)



class ActionDeck:
    starter_warrior = []
    starter_mage = []
    starter_ranger = []
    
    def __init__(self):
        self.deck = []
        self.discard = []



class ActionCard:
    cards = {}
    
    def __init__(self,name,category,rarity,effect):
        self.uuid = uuid4()
        ChapterCard.chapters[self.uuid] = self
        
        if category == "Physique":
            self.category = ActionCategory.PHYSIQUE
        elif category == "Intelligence":
            self.category = ActionCategory.INTELLIGENCE
        elif category == "Dextérité":
            self.category = ActionCategory.DEXTERITE
        else:
            self.category = ActionCategory.UNDEFINED
            
        if rarity == "Common":
            self.rarity = ActionRarity.COMMON
        elif rarity == "Uncommon":
            self.rarity = ActionRarity.UNCOMMON
        elif rarity == "Rare":
            self.rarity = ActionRarity.RARE
        else:
            self.rarity = ActionRarity.UNDEFINED

        self.name = name
        
    def __repr__(self):
        return f"<{self.category.name[:3]}> {self.name}"
        
    def load_cards():
        with open("data/action_card_list.csv","r",encoding="utf-8") as csv_file:
            csv_reader = reader(csv_file)
            next(csv_reader)    # Skip headers
            for row in csv_reader:
                card = ActionCard(
                    row[1],
                    row[2],
                    row[3],
                    None
                )
                if row[9]:
                    for _ in range(int(row[9])):
                        ActionDeck.starter_warrior.append(card)
                if row[10]:
                    for _ in range(int(row[10])):
                        ActionDeck.starter_mage.append(card)
                if row[11]:
                    for _ in range(int(row[11])):
                        ActionDeck.starter_ranger.append(card)



class Hand:
    def __init__(self):
        self.hand = []



class Dice:
    def __init__(self,size,default):
        self.max_value = size
        self.value = default



if __name__ == "__main__":
    ChapterCard.load_cards()
    ActionCard.load_cards()