'''
Class topology
Choose any existing topology of objects that soround us and represent it via classes.
Imlement class hierarchy that will use different relations between objects.
Use classmethods and staticmethods.
Create UML diagram to represent the topology and relations inside of it.
Note: Create at least 3 classes
'''


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
        
            
class Chef(Pizzeria):
    
    def __init__(self, chef_name, qualification, salary):
        self.chef_name = chef_name
        self.qualification = qualification
        self.salary = salary
    
    def create_pizza(self):
        return f'I can create {self.pizza[0]} or {self.pizza[1]}'
    
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
