import pandas as pd
import numpy as np
import random
import barnum
from faker import Faker
fake = Faker()
Faker.seed(47)

class Manufacturing:
    def __init__(self):
        self.role_types = ['full_time', 
                           'part_time', 
                           'intern',
                           'day_shift',
                           'night_shift',
                           'contract']
        
    def __str__(self):
        return f"roles: {self.role_types}"

    def vendors(self, size=10):
        if size < 1:
            return f'ValueError: vendor.size must be greater than 1'
        
        addresses = [barnum.create_city_state_zip() for x in range(size)]
        
        return pd.DataFrame({'id': random.sample(range(1000, 9999), size),
                             'name': [fake.company() for x in range(size)],
                             'street': [fake.address().split('\n')[0] for x in range(size)],
                             'city': [x[1] for x in addresses],
                             'state': [x[2] for x in addresses],
                             'zipcode': [int(x[0]) for x in addresses]
                             })

    def parts(self, size=10):
        if size < 1:
            return f'ValueError: vendor.size must be greater than 1'
        
        return pd.DataFrame({'id': random.sample(range(1000, 9999), size),
                             'vendor_id': [random.choice(self.vendors.ids) for x in range(size)],
                             'name': [fake.license_plate() for x in range(size)],
                             'is_customizable': [bool(random.getrandbits(1)) for x in range(size)],
                             'unit_cost': list(np.random.uniform(0.001, 0.25, size))
                             })

    def distributors(self, size=10):
        if size < 1:
            return f'ValueError: vendor.size must be greater than 1'
        
        addresses = [barnum.create_city_state_zip() for x in range(size)]
        
        return pd.DataFrame({'id': random.sample(range(1000, 9999), size),
                             'name': [fake.company() for x in range(size)],
                             'street': [fake.address().split('\n')[0] for x in range(size)],
                             'city': [x[1] for x in addresses],
                             'state': [x[2] for x in addresses],
                             'zipcode': [int(x[0]) for x in addresses]
                             })
    
    def employee_types(self):
        return pd.DataFrame({'id': random.sample(range(1000, 9999), len(self.role_types)),
                             'role_type': self.role_types
                             })

    def employees(self, role_weights=None):
        titles = {'Designer': 0.05, 
                  'Engineer': 0.4, 
                  'QA': 0.05, 
                  'Procurement': 0.1, 
                  'Wholesale': 0.1, 
                  'Driver': 0.3
                  }
        role_ids = (self.employee_types)['id'].unique().tolist()
        pass

    def products(self):
        pass

    def delivery_services(self):
        pass

    def delivery_schedule(self):
        pass
    