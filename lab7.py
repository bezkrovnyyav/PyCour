'''
Class modifications¶
Modify your existing topology classes with dataclass or any other library for simplification.
'''
from dataclasses import dataclass


class Pizzeria:
    
    restaurant_name = "Pizzeria"
    pizza = ['American pizza', 'Italian pizza']
    
    def __init__(self, personal, stars):
        self.personal = personal
        self.stars = stars
   
    @classmethod    
    def get_open(cls):
        return f'{cls.restaurant_name} is opening'
          
    def get_close(self):
        return f'{self.restaurant_name} is closing'
        
@dataclass            
class Chef(Pizzeria):
    
    chef_name: str
    qualification: int
    salary: int
    
    def create_pizza(self):
        return f'Hi. I am {self.chef_name} - the chef with qualification {self.qualification}'
    
class Waiter(Pizzeria):
    
    def __init__(self, waiter_name, qualification, salary):
        self.waiter_name = waiter_name
        self.qualification = qualification
        self.salary = salary
    
    @classmethod   
    def get_new_salar(cls, waiter_name, qualification, new_salary):
        return f'I would like to have a new salary: {cls(waiter_name, qualification, new_salary).salary} dollars'

class Client(Pizzeria):
    
    def __init__(self, client_name, age, money):
        self.client_name = client_name
        self.age = age
        self.money = money
        
    @staticmethod   
    def make_chois(client_pizza):
        return f'I would like to have {client_pizza}'


pizz = Pizzeria(5, 5)
print(pizz.get_open())

chef = Chef("Andrii", 5, 1000)
print(chef.create_pizza())

client = Client("Andrii", 25, 200)
print(client.make_chois("Ukrainian pizza"))

waiter = Waiter("Nikita", 5, 500)
print(waiter.get_new_salar("Nikita", 5, 750))
