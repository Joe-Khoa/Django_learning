import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','third_project.settings')
import django
django.setup()

import random
from third_app.models import AccessRecord,WebPage,Topic
from faker import Faker

faken = Faker()
topics = ['search','Social', 'Marketplace','News','Games']
def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for entry
        top = add_topic()
        fake_url = faken.url()
        fake_date = faken.date()
        fake_name= faken.company()
        # create new webpage entry/
        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        # create fake record for WebPage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating completed')
