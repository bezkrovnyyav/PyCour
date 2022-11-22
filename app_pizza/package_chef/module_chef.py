from dataclasses import dataclass
from ..package_pizzeria import Pizzeria


@dataclass            
class Chef(Pizzeria):
    chef_name: str
    qualification: int
    salary: int
    
    def get_info(self):
        return f'Hi. I am {self.chef_name} - the chef with qualification {self.qualification}'
