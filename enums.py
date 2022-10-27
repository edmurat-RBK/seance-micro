from enum import Enum



class ChapterType(Enum):
    UNDEFINED = 0
    ENCOUNTER = 1
    EVENT = 2
    BOSS = 3
    


class ActionCategory(Enum):
    UNDEFINED = 0
    PHYSIQUE = 1
    INTELLIGENCE = 2
    DEXTERITE = 3



class ActionRarity(Enum):
    UNDEFINED = 0
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    


class CharacterClass(Enum):
    UNDEFINED = 0
    WARRIOR = 1
    MAGE = 2
    RANGER = 3