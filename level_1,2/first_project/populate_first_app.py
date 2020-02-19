# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
#
# import django
# django.setup()
#
# import random
# from first_app.models import AccessRecord,Webpage,Topic
# from faker import Faker # will work ??
#
# faken = Faker()
# topics = ['Search', 'Social','MaketPlace','News','Games']
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t
# def populate(N=5):
#     for entry in range(N):
#         # for topic
#         top = add_topic()
#         #for Webpage and general
#         fake_url = faken.url()
#         fake_date = faken.date()
#         fake_name= faken.company()
#         # Webpage
#         webpg = Webpage.objects.get_or_create(topic =top, url = fake_url,name = fake_name)[0]
#         acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]
#
# if __name__ == '__main__':
#     print('populating...')
#     populate(30)
#     print('populating completed!')











import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()

import random
from first_app.models import AccessRecord,Webpage,Topic
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
        # create new Webpage entry/
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        # create fake record for Webpage
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]

if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating completed')
