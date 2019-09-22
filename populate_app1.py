# pylint: disable=no-member
import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto1.settings')

import django
django.setup()

import random
from app1.models import AccessRecord, Topic, Webpage
from faker import Faker






fakegen = Faker()

topics = ['Games', 'Music', 'Art', 'News', 'Social', 'People']

def add_topic():

    '''
    Agrega topicos al modelo topic
    '''

    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N = 5):

    '''
    Genera valores falsos a los modelos
    '''
    
    for entry in range(N):

        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
 

if __name__ == '__main__':
    print('script para poblar datos')
    populate(20)
    print('poblacion de datos creada')