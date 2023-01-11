from ..package_pizzeria import Pizzeria


class Waiter(Pizzeria):

    def __init__(self, waiter_name, qualification, salary):
        self.waiter_name = waiter_name
        self.qualification = qualification
        self.salary = salary

    @classmethod
    def get_new_salar(cls, waiter_name, qualification, new_salary):
        return f'I would like to have a new salary: {cls(waiter_name, qualification, new_salary).salary} dollars'

    def get_info(self):
        return f'Hi. My qualification  is {self.qualification}'
