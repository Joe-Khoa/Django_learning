import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','third_project.settings')
import django
django.setup()

import random
from third_app.models import User
from faker import Faker

faken = Faker()
# first_name_s  = ['john','abe','eliot','lanana','minamino']
def add_first_name():
    t = User.objects.get_or_create(first_name = random.choice(first_name_s))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range (N):
        f_name = faken.name()
        l_name = faken.name()
        email_fake = faken.email()
        user_ = User.objects.get_or_create(first_name = f_name,last_name = l_name,email = email_fake)[0]
if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('populating completed')
