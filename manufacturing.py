import pandas as pd
import random
from faker import Faker
fake = Faker()
Faker.seed(47)

class Manufacturing:

    def __init__(self, size, parts):
        self.size = size
        self.num_parts = parts
        self.role_types = ['full_time', 
                           'part_time', 
                           'intern',
                           'day_shift',
                           'night_shift',
                           'contract']
        
    def __str__(self):
        return f"size: {self.size}, parts: {self.num_parts}, roles: {self.role_types}"

    def vendors(self, size=10):
        if size < 1:
            return f'ValueError: vendor.size must be greater than 1'
        
        return pd.DataFrame({'id': random.sample(range(1000, 9999), size),
                             'name': [fake.company() for x in range(size)],
                             'street': [fake.address().split('\n')[0] for x in range(size)],
                             'city': [fake.address().split('\n')[1].split(',')[0] for x in range(size)],
                             'state': [fake.address().split('\n')[1].split(', ')[1].split(' ')[0] for x in range(size)],
                             'zipcode': [int(fake.address().split('\n')[1].split(', ')[1].split(' ')[1]) for x in range(size)]})

    def parts(self):
        part_names = 
        return pd.DataFrame({'id': random.sample(range(1000, 9999), self.num_parts),
                             'vendor_id': random.choice(self.vendors.ids),
                             'name': ,
                             'is_customizable': bool(random.getrandbits(1)),
                             'unit_cost': random.sample(range(0.001, 0.25), self.num_parts)})

    def distributors(self, size=10):
        if size < 1:
            return f'ValueError: vendor.size must be greater than 1'
        pass
    
    def employee_types(self):
        return pd.DataFrame({'id': random.sample(range(1000, 9999), len(self.role_types)),
                             'role_type': self.role_types})

    def employees(self):
        titles = {'Designer': 0.05, 
                  'Engineer': 0.4, 
                  'QA': 0.05, 
                  'Procurement': 0.1, 
                  'Wholesale': 0.1, 
                  'Driver': 0.3}
        role_ids = (self.employee_types)['id'].unique().tolist()

    def products(self):
        pass

    def delivery_services(self):
        pass

    def delivery_schedule(self):
        pass
    