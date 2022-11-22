from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass 
class Pizzeria(ABC):
    restaurant_name = "Pizzeria"
    pizza = ['American pizza', 'Italian pizza']
    
    def __init__(self, personal, stars):
        self.personal = personal
        self.stars = stars
   
    @classmethod    
    def get_open(cls):
        return f'{cls.restaurant_name} is opening'
    
    @abstractmethod
    def get_info(self):
        raise NotImplemented
        