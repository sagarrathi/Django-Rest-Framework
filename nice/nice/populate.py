import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","dsmonk.settings")

import django
django.setup()


## FAKE POP SCRIPT

import random
from social.models import AccessRecord, Topic, Users, Webpage
from faker import Faker

fakegen =Faker()
topics=["Search","Social","Marketplace","News","Games"]

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for enter in range(N):
        # TOPIC FOR THEENTRY
        top=add_topic()
        fake_url=fakegen.url
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        ## Create new webpage entry 
        webp=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        acc_rec=AccessRecord.objects.get_or_create(name=webp, date=fake_date,)



def populate_user(N=5):
    for i in range(N):
        fake_first_name=fakegen.name()
        fake__second_name=fakegen.name()
        fake_email=fakegen.email()

        user_ob=Users.objects.get_or_create(first_name=fake_first_name,
                                            second_name=fake__second_name,
                                            email_id=fake_email)


if __name__=="__main__":
    print("Population script")
    # populate(10)
    populate_user(10)
    print("Population completed")

