import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Hotellu.settings')

import django
django.setup()


#FAKE POP SCRIPT
import random
from hotellu_app.models import User#AccessRecord, WebPage, Topic
from faker import Faker


fakegen = Faker()
# topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']
'''
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
'''

#Complicated ways to create the fake models

def populate(N=5):

    for entry in range(N):

        #get the topic of the entry
        # top = add_topic()
        '''
        #Create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create new webpage entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #Create a fake access record for that WebPage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]
        '''


        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Populating complete")
