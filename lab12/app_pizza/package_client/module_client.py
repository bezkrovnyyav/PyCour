from ..package_pizzeria import Pizzeria


class Client(Pizzeria):

    def __init__(self, client_name, age, money):
        self.client_name = client_name
        self.age = age
        self.money = money

    @staticmethod
    def make_chois(client_pizza):
        return f'I would like to have {client_pizza}'

    def get_info(self):
        return f'Hi. My name is {self.client_name}'
