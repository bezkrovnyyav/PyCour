'''
Modules & Imports
Split your class topology into python package (several packages are preferred) and configure importing between them.
Note: it's recomended to add importing data in the __init__.py file.

- Check lab_9 via flake8
'''
from app_pizza import Chef, Waiter, Client, Food


chef = Chef("Andrii", 5, 1000)
print(chef.get_info())

client = Client("Andrii", 25, 200)
print(client.make_chois("Ukrainian pizza"))

waiter = Waiter("Nikita", 5, 500)
print(waiter.get_info())

brown_sugar = Food("Brown Sugar", 10)
white_sugar = Food("White Sugar", 10)
flour = Food('Flour', 5)

# create copy brown_sugar
copy_sugar = brown_sugar.__copy__()
print(f'It is copy of class {copy_sugar}')

# full price of gray sugar and flour
print(brown_sugar + flour)

# checking the price of gray sugar is equal to the price of copy brown_sugar
print(brown_sugar == copy_sugar)
