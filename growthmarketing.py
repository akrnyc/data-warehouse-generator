import pandas as pd
import numpy as np
import random
import barnum
from faker import Faker
fake = Faker()
Faker.seed(47)

class Growth:
    def __init__(self):
        self.role_types = ['full_time', 
                           'part_time', 
                           'intern',
                           'day_shift',
                           'night_shift',
                           'contract']
        
    def __str__(self):
        return f"roles: {self.role_types}"
    
    def leads():
        pass

    def opportunities():
        pass

    def members():
        pass

    def digital():
        pass

    def digital_spend():
        pass

    def affiliates():
        pass

    def affiliate_spend():
        pass

    def other_ads():
        pass

    def other_ad_spend():
        pass

    def surveys():
        pass

    def survey_responses():
        pass
