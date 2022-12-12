from dataclasses import dataclass
from copy import copy


@dataclass            
class Food():
    name: str
    price: int
    
    def __eq__(self, other):
        if not isinstance(other, (int, Food)):
            raise TypeError("Here should be int or class Food")
 
        food_price = other if isinstance(other, int) else other.price
        return self.price == food_price
    
    def __add__(self, other):
        if not isinstance(other, Food):
            raise TypeError('Here should be only class Food')
        full_price = self.price + other.price
        return full_price

    def __copy__(self):
        cls = self.__class__
        new_copy = cls.__new__(cls)
        new_copy.__dict__.update(self.__dict__)
        return new_copy
