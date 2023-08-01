import pandas as pd
import numpy as np
import random
import barnum
from faker import Faker
fake = Faker()
Faker.seed(47)

class Growth:
    def __init__(self):
        self.digital_ads = ['facebook',
                            'google',
                            'twitter',
                            'adobe',
                            'instagram']
        
        #https://www.quicksprout.com/best-lead-generation-companies/
        self.partners = ['callbox',
                         'leadgeneration',
                         'webimax']
        
        self.other_ads = ['mailchimp',
                          'directmail',
                          'referral',
                          'webflow']
        
        self.campaigns = ['holiday_sale',
                          'seasonal_sale',
                          'influencer',
                          'initial_sign_up',
                          'inactive_member']
        
    def __str__(self):
        return f"digital_ads: {self.digital_ads}, partners: {self.partners}, other_ads: {self.other_ads}"
    
    def digital(self):
        pass

    def digital_spend(self):
        pass

    def affiliates(self):
        pass

    def affiliate_spend(self):
        pass

    def other_ads(self):
        pass

    def other_ad_spend(self):
        pass

    def leads(self, size=10):
        addresses = [barnum.create_city_state_zip() for x in range(size)]
        phones = [barnum.create_phone(x[0]) for x in addresses]
        
        return pd.DataFrame({'id': random.sample(range(1000, 9999), size),
                             'first_name': [fake.first_name() for x in range(size)],
                             'last_name': [fake.last_name() for x in range(size)],
                             'street': [fake.address().split('\n')[0] for x in range(size)],
                             'city': [x[1] for x in addresses],
                             'state': [x[2] for x in addresses],
                             'zipcode': [int(x[0]) for x in addresses],
                             'email': [fake.ascii_free_email() for x in range(size)],
                             'phone': phones,
                             'utm_source': ,
                             'ad_id': 
                             })

    def opportunities(self):
        pass

    def members(self):
        pass

    def surveys(self):
        pass

    def survey_responses(self):
        pass
