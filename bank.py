import pandas as pd
import numpy as np
import random
import barnum
from faker import Faker
fake = Faker()
Faker.seed(47)

class Bank:
    def __init__(self):
        self.role_types = ['full_time', 
                           'part_time', 
                           'intern',
                           'day_shift',
                           'night_shift',
                           'contract']
        
    def __str__(self):
        return f"roles: {self.role_types}"
    
    def accounts():
        pass

    def account_types():
        pass

    def customers():
        pass

    def merchants():
        pass

    def transaction_types():
        pass

    def transactions():
        pass

    def officers():
        pass

    def services():
        pass

    def officer_schedule():
        pass

    def service_schedule():
        pass
