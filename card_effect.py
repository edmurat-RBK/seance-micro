from abc import ABC, abstractmethod

class CardEffect(ABC):
    def __init__(self,description):
        self.description_text = description
        
    @abstractmethod
    def apply_effect(self,values=(),targets=()):
        pass
    

